# 1.1.0 implementation and validation

1. Inspect the 1.0.0 contracts and baseline pressure scenario against a resumed multi-package project.
2. Add failing hook reminder regressions for ledger recovery, checkpoint scope and honest unknown evidence.
3. Clarify continuation, approval reuse and audit applicability without replacing executor or host rules.
4. Explain purpose, installation and limitations in README; align both manifests to 1.1.0.
5. Run unit/scanner/manifest checks, repeat the pressure scenario, obtain independent review and fix findings.
6. Commit the reviewed version, merge locally to main, push, update repository description and publish a tagged GitHub release.

Baseline: two new hook tests fail on 1.0.0. A separate agent identifies the ambiguous missing-evidence→FAIL→permission-stop behavior and absence of durable recovery/checkpoint rules. Automated text checks test reminders, not semantic host enforcement. Live Claude execution is separately reported as tested or unavailable.
