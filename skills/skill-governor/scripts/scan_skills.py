"""Read-only capability discovery. Python 3.10+; no third-party dependencies."""
import argparse
import json
import os
from pathlib import Path
import re

REGISTRY = Path(__file__).resolve().parents[1] / 'references' / 'skill-registry.json'
SKIP = {'.git', 'node_modules', '.venv', '__pycache__'}


def metadata(text):
    """Read scalar YAML name/description; flag advanced YAML for host parsing."""
    match = re.match(r'\A\ufeff?---\s*\n(.*?)\n---(?:\s*\n|$)', text, re.S)
    if not match:
        return None
    fields = {}
    lines = match[1].splitlines()
    for i, line in enumerate(lines):
        field = re.match(r'^(name|description):\s*(.*)$', line)
        if not field:
            continue
        key, value = field.groups()
        if value.startswith(('[', '{', '&', '*', '!', '|+', '>+')):
            return None
        if value in ('|', '>', '|-', '>-'):
            parts = []
            for continuation in lines[i + 1:]:
                if continuation and not continuation[0].isspace():
                    break
                parts.append(continuation.strip())
            value = ('\n' if value.startswith('|') else ' ').join(parts).strip()
        elif value.startswith('"'):
            try:
                value = json.loads(value)
            except ValueError:
                return None
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        else:
            value = value.split(' #', 1)[0].strip()
        fields[key] = value
    return fields if fields.get('name') and fields.get('description') else None


def scan(project, home, roots=None):
    registry = json.loads(REGISTRY.read_text(encoding='utf-8'))
    project, home = Path(project).resolve(), Path(home).resolve()
    locations = roots if roots is not None else [
        home / '.claude/skills', home / '.claude/plugins', home / '.codex/skills',
        home / '.codex/plugins/cache', home / '.agents/skills',
        project / '.claude/skills', project / '.claude/plugins', project / '.claude-plugin',
        project / '.cursor/rules', project / '.agents/skills', project / '.codex/skills']
    found, errors, providers, manifests = [], [], set(), []
    seen = set()
    for location in locations:
        location = Path(location)
        if not location.exists():
            continue
        def walk_error(error):
            errors.append({'path': str(error.filename), 'error': type(error).__name__})
        for folder, dirs, files in os.walk(location, followlinks=False, onerror=walk_error):
            dirs[:] = [d for d in dirs if d not in SKIP and not (Path(folder) / d).is_symlink()]
            for filename in files:
                if filename not in ('SKILL.md', 'plugin.json', 'marketplace.json', 'installed_plugins.json'):
                    continue
                file = Path(folder) / filename
                if file.is_symlink() or file.resolve() in seen:
                    continue
                seen.add(file.resolve())
                try:
                    if file.stat().st_size > 2_000_000:
                        errors.append({'path': str(file), 'error': 'oversized'})
                        continue
                    text = file.read_text(encoding='utf-8-sig')
                    if filename == 'SKILL.md':
                        fields = metadata(text)
                        if fields:
                            found.append(dict(fields, path=str(file)))
                        else:
                            errors.append({'path': str(file), 'error': 'frontmatter-needs-host-parser'})
                    else:
                        data = json.loads(text)
                        if not isinstance(data, dict):
                            raise ValueError('manifest must be an object')
                        # Only inspect identity fields, never output arbitrary config values.
                        identity = {k: data[k] for k in ('name', 'repository') if isinstance(data.get(k), str)}
                        manifests.append({'path': str(file), **identity})
                        for bundle in registry['bundles']:
                            if bundle['repo'] in identity.values() or 'https://github.com/' + bundle['repo'] in identity.values():
                                providers.add(bundle['repo'])
                except (OSError, UnicodeError, ValueError) as error:
                    errors.append({'path': str(file), 'error': type(error).__name__})
    names = {item['name'] for item in found}
    for bundle in registry['bundles']:
        if names.intersection(bundle['names']):
            providers.add(bundle['repo'])
    capabilities = []
    for entry in registry['skills']:
        matches = [item['path'] for item in found if item['name'] == entry['id']]
        covering = [b['repo'] for b in registry['bundles'] if b['repo'] in providers and entry['id'] in b['skills']]
        capabilities.append({'id': entry['id'], 'status': 'installed' if matches else 'bundle-covered' if covering else 'not-observed', 'paths': matches, 'providers': covering, 'contract_review_required': bool(covering)})
    mcp, context = [], []
    for base in (home, project):
        for relative in ('.mcp.json', '.claude/settings.json', '.claude.json'):
            file = base / relative
            if file.is_file():
                try:
                    data = json.loads(file.read_text(encoding='utf-8-sig'))
                    if not isinstance(data, dict):
                        raise ValueError('MCP config must be an object')
                    servers = data.get('mcpServers', {})
                    if isinstance(servers, dict):
                        mcp.extend({'name': name, 'source': str(file), 'status': 'configured-unverified'} for name in servers)
                except (OSError, UnicodeError, ValueError) as error:
                    errors.append({'path': str(file), 'error': type(error).__name__})
        for relative in ('CLAUDE.md', 'AGENTS.md', '.codex/config.toml'):
            if (base / relative).is_file():
                context.append(str(base / relative))
    return {'skills': found, 'capabilities': capabilities, 'manifests': manifests, 'mcp_servers': mcp,
            'context_files': sorted(set(context)), 'errors': errors,
            'limitations': ['Read detected context files with host tools as needed.', 'MCP runtime availability must be confirmed with host tools.', 'Bundle aliases require provider contract inspection.', 'Complex YAML requires the host YAML parser.', 'Symlinked skill trees are skipped; supplement using host inventory.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=Path.cwd())
    parser.add_argument('--home', type=Path, default=Path.home())
    parser.add_argument('--root', type=Path, action='append', help='Override skill scan roots; repeatable')
    args = parser.parse_args()
    print(json.dumps(scan(args.project, args.home, args.root), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
