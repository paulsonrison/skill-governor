"""Lifecycle reminders; never executes task code or installs dependencies."""
import json
import sys


def respond(event):
    name = event.get('hook_event_name')
    if name in ('SessionStart', 'UserPromptSubmit'):
        return {'hookSpecificOutput': {'hookEventName': name, 'additionalContext':
            'Use skill-governor: read its SKILL.md and recover the approved plan and ledger. '
            'Preserve explicit locks and reuse unchanged approval. Present a new Governance Plan '
            'only when required scope or selection changes. Answer a status question briefly '
            'without dropping the task. A package checkpoint is not project completion. '
            'Route implementation to the approved executor, then audit applicable actions with evidence.'}}
    if name == 'Stop' and not event.get('stop_hook_active'):
        # One reminder only: the hook cannot verify compliance or task completion.
        return {'decision': 'block', 'reason':
            'Before finishing, provide a compact audit of applicable skills using PASS, FAIL, '
            'NOT_RUN or UNVERIFIED with observed evidence. Missing evidence is not a proven violation. '
            'For a status-only turn say No new execution this turn and retain prior progress. '
            'Do not rerun work or tools merely to fill rows. Persist unfinished scope and next action '
            'in the ledger; an audit or checkpoint does not complete the whole task. '
            'Repair reversible violations within authorization; honor host and loaded-contract approval rules.'}
    return {}


if __name__ == '__main__':
    try:
        payload = json.load(sys.stdin)
        print(json.dumps(respond(payload)))
    except (ValueError, AttributeError) as error:
        print('skill-governor: invalid hook payload: ' + type(error).__name__, file=sys.stderr)
        sys.exit(1)
