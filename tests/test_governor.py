import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


scanner = load('scanner', ROOT / 'skills/skill-governor/scripts/scan_skills.py')
hooks = load('hooks', ROOT / 'hooks/governance.py')


class GovernorTests(unittest.TestCase):
    def test_unknown_skill_and_bundle_resolution(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            for name in ('custom-capability', 'karpathy-guidelines'):
                skill = base / '.claude/skills' / name / 'SKILL.md'
                skill.parent.mkdir(parents=True)
                skill.write_text('---\nname: ' + name + '\ndescription: >-\n  Useful custom\n  capability\n---\n', encoding='utf-8')
            result = scanner.scan(base, base)
            self.assertIn('custom-capability', [s['name'] for s in result['skills']])
            caps = {c['id']: c for c in result['capabilities']}
            self.assertEqual(caps['read-first']['status'], 'bundle-covered')
            self.assertEqual(caps['one-step']['status'], 'not-observed')
            self.assertEqual(len(result['skills']), 2)

    def test_malformed_and_secret_redaction(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            (base / '.mcp.json').write_text(json.dumps({'mcpServers': {'context7': {'env': {'TOKEN': 'SECRET-SENTINEL'}}}}))
            skill = base / '.claude/skills/broken/SKILL.md'
            skill.parent.mkdir(parents=True)
            skill.write_text('not frontmatter')
            result = scanner.scan(base, base)
            self.assertTrue(result['errors'])
            self.assertNotIn('SECRET-SENTINEL', json.dumps(result))
            self.assertEqual(result['mcp_servers'][0]['status'], 'configured-unverified')

    def test_prompt_recovers_existing_approval_and_scope(self):
        message = hooks.respond({'hook_event_name': 'UserPromptSubmit'})['hookSpecificOutput']['additionalContext']
        self.assertIn('ledger', message)
        self.assertIn('checkpoint', message)
        self.assertIn('status', message)

    def test_stop_distinguishes_unknown_evidence_from_violation(self):
        message = hooks.respond({'hook_event_name': 'Stop'})['reason']
        self.assertIn('UNVERIFIED', message)
        self.assertIn('No new execution', message)
        self.assertNotIn('ask permission to retry and stop', message)

    def test_resume_command_links_to_existing_guidance(self):
        command = ROOT / 'commands/govern.md'
        self.assertIn('../skills/skill-governor/references/continuation.md', command.read_text(encoding='utf-8'))
        self.assertTrue((command.parent / '../skills/skill-governor/references/continuation.md').is_file())

    def test_release_versions_and_continuation_reference(self):
        plugin = json.loads((ROOT / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
        self.assertEqual(plugin['version'], '1.1.0')
        self.assertEqual(plugin['version'], market['plugins'][0]['version'])
        skill = ROOT / 'skills/skill-governor'
        self.assertIn('references/continuation.md', (skill / 'SKILL.md').read_text(encoding='utf-8'))
        self.assertTrue((skill / 'references/continuation.md').is_file())
        self.assertEqual(market['plugins'][0]['source'], './')

    def test_hook_continuation_is_bounded(self):
        self.assertEqual(hooks.respond({'hook_event_name': 'Stop'})['decision'], 'block')
        self.assertEqual(hooks.respond({'hook_event_name': 'Stop', 'stop_hook_active': True}), {})
        output = hooks.respond({'hook_event_name': 'UserPromptSubmit'})
        self.assertEqual(output['hookSpecificOutput']['hookEventName'], 'UserPromptSubmit')

    def test_non_object_configuration_does_not_abort_scan(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            (base / '.mcp.json').write_text('[]')
            manifest = base / '.claude/plugins/bad/plugin.json'
            manifest.parent.mkdir(parents=True)
            manifest.write_text('[]')
            result = scanner.scan(base, base)
            self.assertEqual(len(result['errors']), 3)  # home and project config plus manifest
            self.assertEqual(len(result['capabilities']), 22)

    def test_complex_yaml_requires_host_parser(self):
        self.assertIsNone(scanner.metadata('---\nname: [not-a-scalar]\ndescription: text\n---\n'))
        self.assertIsNone(scanner.metadata('---\nname: test\ndescription: {invalid: mapping}\n---\n'))

    def test_registry_complete_and_install_gaps_explicit(self):
        data = json.loads(scanner.REGISTRY.read_text(encoding='utf-8'))
        self.assertEqual(len(data['skills']), 22)
        self.assertEqual(len({s['id'] for s in data['skills']}), 22)
        for skill in data['skills']:
            self.assertTrue(skill['audit'])
            self.assertTrue(skill['trigger'])
            self.assertTrue(skill['sources'] or skill['install_note'].startswith('BLOCKED'))


if __name__ == '__main__':
    unittest.main()
