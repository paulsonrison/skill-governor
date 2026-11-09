"""Lifecycle reminders; never executes task code or installs dependencies."""
import json
import sys


def respond(event):
    name = event.get('hook_event_name')
    if name in ('SessionStart', 'UserPromptSubmit'):
        return {'hookSpecificOutput': {'hookEventName': name, 'additionalContext':
            'Use skill-governor: read its SKILL.md, preserve explicit skill locks, inspect capabilities, '
            'and present the Governance Plan. Wait for approval before execution. Reuse explicit '
            'approval for an unchanged plan. Do not implement business logic in the governor. '
            'After execution audit every active skill with concrete evidence.'}}
    if name == 'Stop' and not event.get('stop_hook_active'):
        # One bounded continuation requests the audit. It is not a semantic validator.
        return {'decision': 'block', 'reason':
            'Before finishing, provide the skill-governor compliance table for active skills with '
            'observed PASS/FAIL evidence. If this was only planning, status, or approval, say '
            'execution has not started. If a skill failed, ask permission to retry and stop. '
            'Do not repeat task execution or invent evidence.'}
    return {}


if __name__ == '__main__':
    try:
        payload = json.load(sys.stdin)
        print(json.dumps(respond(payload)))
    except (ValueError, AttributeError) as error:
        print('skill-governor: invalid hook payload: ' + type(error).__name__, file=sys.stderr)
        sys.exit(1)
