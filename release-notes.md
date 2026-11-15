Skill Governor coordinates the skills an AI coding assistant uses: it discovers available capabilities, preserves explicit user choices, proposes an approved workflow and audits actual compliance. It delegates execution to the selected skills and respects host permissions.

Version 1.1.0 improves long-running work:

- Recover approved scope, branch, task position, evidence and next actions after interruption.
- Reuse valid approvals; status questions and package checkpoints do not restart or complete the project.
- Distinguish actual violations from unused obligations and missing proof with PASS, FAIL, NOT_RUN and UNVERIFIED.
- Keep expected failing tests and WIP checkpoints separate from acceptance and release readiness.
- Repair authorized reversible work without blanket permission stops, while retaining explicit locks and host/loaded-contract requirements.
- Clarify the README, command guidance, marketplace description and limitations.

Validation: 10 Python tests pass, isolated scanner smoke check passes, and independent scenario review/rereview is clear. Live Claude CLI validation was not available and is not claimed. See VALIDATION.md for scope.

Install in Claude Code:
```text
/plugin marketplace add paulsonrison/skill-governor
/plugin install skill-governor@skill-governor-marketplace
```

For Codex, copy skills/skill-governor into your configured skills directory and restart discovery; Claude hooks do not run in Codex. Existing Claude users should refresh their marketplace and installed plugin through their host's update controls.

The attached ZIP contains the versioned plugin and Codex skill. This is a self-hosted marketplace release, not an official directory endorsement or a security boundary.
