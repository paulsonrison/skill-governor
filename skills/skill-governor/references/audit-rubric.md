# Compliance audit

Audit active skills only. PASS requires observable evidence against the actual loaded contract and the applicable capability check below. Use FAIL for an actual applicable contract violation, UNVERIFIED for missing evidence, and NOT_RUN when no obligation was exercised in this segment; never invent tool use. Cite file paths, commands, results or user decisions. For external skills derive the rubric from their own instructions, flag ambiguity, and never replace it with a baseline approximation.

## grill-me

Did the agent challenge assumptions and ask targeted architectural/edge-case questions before proposing code?

## read-first

Were file-read/search tools executed on target files and dependencies *before* any plan or edit was emitted?

## plan-no-code

Did the output contain a structured step-by-step plan and ZERO executable implementation code blocks?

## smallest-version

Were speculative abstractions stripped out in favor of the smallest working vertical slice?

## one-step

Did the agent execute strictly ONE plan item and verify its result before stopping?

## stay-in-scope

Were 100% of modified lines directly required by the prompt, with zero drive-by formatting or unrelated file edits?

## what-changed

Does the response conclude with an explicit file-by-file, line-level summary of what changed and why?

## remember-this

Was the new rule, correction, or project idiom persisted to `CLAUDE.md` / agent memory?

## why-not-fix

Did the agent complete a 5-Whys root-cause chain and prove *why* the bug happens before proposing a fix?

## explain-the-error

Was the stack trace decomposed into exact failure mechanism and isolated component prior to solutioning?

## add-logs

Were targeted diagnostic logs or failing reproduction tests added and evaluated empirically?

## loop-breaker

Did the agent halt repetitive edits, reset its assumptions, and present a fundamentally different approach or escalate to the user?

## security-pass

Was an explicit OWASP/secret/access-control audit executed across all modified files?

## break-it

Were concrete adversarial edge cases, boundary inputs, and race conditions tested against the implementation?

## senior-review

Did the output deliver an uncompromising Staff-level critique covering architecture, maintainability, and production readiness?

## superpower

Select and load the applicable native sub-skill without duplicating its workflow.

## andrej-karpathy

Show evidence of explicit assumptions, minimal scope and outcome verification.

## rea

Use authorized target artifacts and cite inspection evidence.

## agent-reach

Cite retrieved platform content and keep actions read-only unless separately authorized.

## replica

Show authorized reference inspection and fidelity verification.

## context-7

Retrieve documentation for the correct library and version; connect it to the decision.

## chrome-devtool-mcp

Inspect the relevant browser runtime and report concrete observations.

For an actual violation, explain the instruction and effect, then repair reversible work within existing authorization. Ask only for a missing decision or authorization, or when another applicable contract requires it. Expected red tests are product evidence, not automatic skill failures. Unknown evidence stays UNVERIFIED until recovered. Keep installation retry bounds and host denial rules. Never treat an audit as independent proof of correctness.
