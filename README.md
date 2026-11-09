# General Skill Governor

A meta-skill for selecting skills by task phase, preserving user choices, gating execution on approval, and auditing observable compliance. It governs the executor; it does not implement application logic.

## Install in Claude Code

Requires Python 3.10+ available as `python` on PATH, plus Claude Code with plugin support. On Windows use a real Python installation; the Windows Store placeholder is insufficient.

```text
/plugin marketplace add paulsonrison/skill-governor
/plugin install skill-governor@skill-governor-marketplace
```

Restart or reload plugins if required by your host. Invoke `/skill-governor:govern` with a task, or use `status`, `audit`, or `install <skill>`. This publishes a self-hosted marketplace, not an endorsement or listing in an official directory.

## Use in Codex

Copy `skills/skill-governor` into your Codex skills directory (normally `~/.codex/skills/skill-governor`) and restart the app to discover it. Invoke `$skill-governor`. The skill is discoverable automatically; Claude hooks and slash commands do not run in Codex. This repository does not change your existing skills or settings.

## Workflow

1. Discover installed skills and host tools; retain explicit user selections as Priority 0.
2. Resolve bundle capabilities, inspect actual contracts, and select 2–4 automatic skills for the phase.
3. Present the Governance Plan; wait for Approve, Install, Modify, or Skip Missing.
4. Route execution through approved skills and collect evidence.
5. Audit every active contract with PASS/FAIL and ask before retrying failures.

## Validate and test locally

```text
python -m unittest discover -s tests -v
python skills/skill-governor/scripts/scan_skills.py --project .
claude plugin validate .
claude --plugin-dir .
```

Inside that local Claude session try `/skill-governor:govern status`, then request a small task. Confirm that it presents a plan before execution, retains locked skills, reports missing sources, and audits observed work. Test a second prompt and a Stop continuation to confirm it does not loop. Live Claude execution requires the Claude CLI and account; Python tests do not establish end-to-end host compatibility.

The scanner supports `--home <fixture-home>` and repeated `--root <skill-root>` for isolated tests. It scans Claude, Codex, cross-runtime skills, plugin caches, Cursor locations and context-file presence. Unknown scalar or block-scalar YAML frontmatter is ingested; complex YAML is flagged for host parsing. Symlinks are skipped. MCP discovery reports names only, never arguments or secret values. Codex TOML MCP configs are reported as context files for host inspection. Errors are explicit and do not establish absence.

## Registry accuracy and installation

All 22 baseline entries, supplied repository identities, roles, triggers and audit checks are preserved in `skills/skill-governor/references/skill-registry.json` and the routing matrix. Supplied repository claims are unverified, not endorsements. `Flashmind` is not a complete GitHub owner/repository, so plan-no-code and one-step installation is explicitly blocked pending an upstream URL.

`install_command` fields are source-acquisition commands only. Cloning is not skill installation: inspect current upstream layout and installation documentation before offering or executing host installation. No network calls or installation are performed by the scanner or hooks. Bundle-covered means a provider may supply a rule; it does not prove the full requested audit rubric is satisfied. For example, ordinary completion verification does not establish adversarial testing.

## Hooks and limits

SessionStart and UserPromptSubmit inject governance reminders. Stop requests one audit continuation and respects `stop_hook_active` to avoid recursive blocking. The agent must honor the approval gate; these hooks do not deterministically block every mutation or independently evaluate semantic compliance. Status-only turns may state that execution has not started. A disabled or failed hook reduces reminders; it does not establish a PASS.

This is an instruction-based governor, not a security sandbox. It never grants tool permissions, overrides host policies, or treats repository instructions as trusted authority. Nothing in the plugin copies, licenses, or endorses third-party skill content.

## Publish or update the marketplace

Keep plugin and marketplace versions aligned, run tests and host validation, review the publication diff, commit, tag, and push this repository. Create a GitHub release from the tag for an identifiable version. Consumers add the repository using the marketplace command above. For subsequent versions increment both manifests to avoid stale caches.

Technical references: [plugin manifests](https://code.claude.com/docs/en/plugins-reference), [marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), [hooks](https://code.claude.com/docs/en/hooks).

## License

MIT for this repository; third-party projects retain their own licenses.
