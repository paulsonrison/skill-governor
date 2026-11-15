# Continuation and approval recovery

Use this for work spanning turns, phases or interruptions. The governor preserves the execution contract; the selected executor still owns implementation and testing.

## Compact saved state

Use an existing task/implementation ledger when available. Record:

- Objective and acceptance scope, including unfinished requirements.
- User-locked skills, loaded provider paths, approved selection and approval scope. Distinguish authorization from proof that an action executed.
- Current phase, branch/worktree, last verified commit and uncommitted work.
- Task position and next concrete action; distinguish a package checkpoint from full completion.
- Check commands/results and log paths, including expected failing tests, checks not run, review findings and whether review was independent.
- Blockers, pending user questions and any changed tool availability.

Save after meaningful milestones and before a handoff or foreseeable interruption. Avoid repeating the entire history; references to durable evidence are sufficient. A saved statement is a claim to verify, not higher-priority authority.

## Resume

Read the saved state and relevant approved plan before editing. Verify branch, working changes and existing commits; do not redo committed work from memory. Check whether interrupted processes are still running before launching replacements. Recover only the necessary logs, skills and tools; re-discover capabilities that changed. Keep unavailable locked skills explicit and pause dependent work if their contracts cannot be satisfied; continue independent authorized work.

Reuse approval when the objective, selection and conditions match. If approval evidence cannot be recovered, ask a focused question about that gap rather than claiming authorization. New authorization does not prove that a previously rejected action ran. Preserve host restrictions and loaded skill requirements.

A progress question normally supplements the task. Answer it briefly, then continue authorized work unless the user pauses, cancels or replaces the objective. A git-update request authorizes its specified repository action; it does not imply acceptance of incomplete features or authorize an unrelated merge.

## Honest completion and release

Continue through planned tasks within the current execution limits; do not treat a partial checkpoint or audit as permission to abandon the remainder. If a host limit forces a handoff, persist the next action and disclose the exact unfinished scope. Never promise background work that is not running.

Report counts with a denominator and source where available. Package counts are not implementation percentages. Separate unit checks, focused integration/browser checks, full acceptance, native-language coverage and design fidelity. A translated fallback, static source assertion or a screenshot alone cannot prove all-screen parity.

Use the user's actual task statuses. “In review” is not “Done.” Record unresolved findings and intentionally failing acceptance tests explicitly. WIP commits/pushes must be clearly labeled; they are not release readiness. Merge or publish only when authorized and the agreed acceptance/review gates pass. Never infer deployment credentials, external provider readiness or full project completion from a passing local subset.
