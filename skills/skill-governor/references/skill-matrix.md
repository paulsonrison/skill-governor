# Routing matrix

Select 2–4 relevant automatic skills for the current phase; user locks are additional and never dropped to satisfy the cap. Tools are selected separately. Read installed contracts before activating them.

Never combine plan-no-code with one-step or mutation. Diagnose with why-not-fix before any patch. If user-locked contracts conflict, preserve both selections, describe the conflict and ask for ordering.

Bundle aliases identify covered capabilities, not separate SKILL.md files. Load the provider contract and activate only relevant rules. Provider rubric differences must be disclosed: verification-before-completion alone does not prove adversarial testing.

## Grill me (`grill-me`)

Phase: Before Code

Adversarial interview skill that stress-tests assumptions, edge cases, and design choices before writing any code.

Trigger: Ambiguous prompts, greenfield architecture, or underspecified feature requests.

Sources: `mattpocock/skills` (sub-skill: `grill-me`) | Fallbacks: `robmitt/grill-me-skill`, `shaugupt/grill-me-cursor`

## read first (`read-first`)

Phase: Before Code

Codifies the "read before write" rule, forcing agents to inspect existing files, conventions, and dependencies prior to modifying code.

Trigger: Any task touching an existing repository or file.

Sources: `multica-ai/andrej-karpathy-skills` & `TODAQmicro/qatom-skill`

## plan, no code (`plan-no-code`)

Phase: Before Code

Enforces an explicit planning gate where the agent outputs a step-by-step implementation plan without writing executable code until approved.

Trigger: Multi-file changes, refactors, or new feature designs prior to user sign-off.

Sources: `Flashmind` (`plan-first`)

## smallest version (`smallest-version`)

Phase: Before Code

Enforces minimal vertical slices and rejects speculative abstractions, premature generalization, or unrequested configurability.

Trigger: Feature scoping, MVP builds, or prompts prone to over-engineering.

Sources: `multica-ai/andrej-karpathy-skills` (Rule 2: "Simplicity First") & `JuliusBrussee/cavekit`

## one step (`one-step`)

Phase: While Building

Restricts the agent to executing one task item per prompt, verifying test output before advancing to the next step.

Trigger: Approved multi-step implementation plans.

Sources: `Flashmind` (`plan-first` / Step-by-Step)

## stay in scope (`stay-in-scope`)

Phase: While Building

Prevents unsolicited refactoring, drive-by formatting, or touching files outside the explicit task boundary.

Trigger: All code modification and feature implementation turns.

Sources: `multica-ai/andrej-karpathy-skills` (Rule 3: "Surgical Changes") & `JordanNewell/wranglebot` (`scope-guard`)

## what changed (`what-changed`)

Phase: While Building

Requires a concise diff summary stating exactly what files and lines were altered and why after every edit pass.

Trigger: Every turn that mutates files.

Sources: `mishgoldenberg/claude-mods` (`changes`) & `KattyFury/tool_seismic_seismiclogo`

## remember this (`remember-this`)

Phase: While Building

Long-term memory protocol that records corrections, project idioms, and past mistakes directly into `CLAUDE.md` (or memory store) to prevent recurring errors.

Trigger: Whenever a user corrects the agent, establishes a repo convention, or resolves a non-obvious project quirk.

Sources: `thedaviddias/claude-mem` & `alirezarezvani/claude-skills` (`agent-memory`)

## Why, not fix (`why-not-fix`)

Phase: When It Breaks

Requires conducting a root-cause diagnosis (5 Whys) rather than applying blind, speculative patches.

Trigger: Bug reports, broken builds, or test failures.

Sources: `multica-ai/andrej-karpathy-skills` & `g-shevchenko/agent-failure-loop-breaker`

## explain the error (`explain-the-error`)

Phase: When It Breaks

Forces decomposition of stack traces, explanation of failure mechanisms, and isolation of the failing component before proposing a solution.

Trigger: Prompts containing stack traces, compiler errors, runtime exceptions, or crash logs.

Sources: `the-senior-dev/senior-dev-skills`

## add logs (`add-logs`)

Phase: When It Breaks

Mandates inserting diagnostic logging and reproducible test assertions to verify runtime state with empirical evidence.

Trigger: Non-trivial bugs, state mutations, async/race conditions, or unverified hypotheses.

Sources: `obra/superpowers` (sub-skill: `systematic-debugging`)

## loop breaker (`loop-breaker`)

Phase: When It Breaks

Active monitor that intercepts recursive retry loops (3+ failed attempts on the same file/bug) and forces the agent to switch strategies or request human input.

Trigger: 2+ consecutive failed fix attempts on the same error or file.

Sources: `g-shevchenko/agent-failure-loop-breaker` & `Fallsnacode13/cursor-composer-loop-breaker`

## security pass (`security-pass`)

Phase: Before Launch

Runs an OWASP-aligned audit across modified files to flag hardcoded secrets, injection vectors, and broken access controls.

Trigger: Pre-PR/launch checks, or any change touching auth, APIs, user input, DB queries, or secrets.

Sources: `PeterPonyu/oh-my-cursor` (`security-review`) & `borghei/Claude-Skills` (`senior-secops`)

## break it (`break-it`)

Phase: Before Launch

Adversarial red-team review attempting to crash the feature using malicious inputs, edge values, and race conditions.

Trigger: Feature completion, pre-launch verification, or test-suite hardening.

Sources: `SirRuggie/claude-code-orchestration-kit` & `obra/superpowers` (sub-skill: `verification-before-completion`)

## senior review (`senior-review`)

Phase: Before Launch

Adversarial review simulating a Staff/Senior Engineer evaluating architecture, code clarity, and adherence to production best practices.

Trigger: Final pre-merge/pre-launch quality gate or explicit review requests.

Sources: `JuliusBrussee/skills` (`junior-to-senior`) & `the-senior-dev/senior-dev-skills`

## superpower (`superpower`)

Phase: Cross-Cutting

Jesse Vincent's comprehensive agentic skills framework and software development workflow plugin for Claude Code.

Trigger: Coordinate when `obra/superpowers` is installed so its sub-skills (`systematic-debugging`, `verification-before-completion`, `test-driven-development`, `brainstorming`) are leveraged natively without duplication.

Sources: `obra/superpowers`

## Andrej Karpathy (`andrej-karpathy`)

Phase: Cross-Cutting

Implements Andrej Karpathy's 4 core guidelines for coding agents (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution).

Trigger: Active baseline coding philosophy across all planning and implementation turns.

Sources: `multica-ai/andrej-karpathy-skills`

## REA (`rea`)

Phase: Cross-Cutting

"Reverse Engineer Anything" suite of agent skills and MCP tools that inspect and reconstruct software directly from binaries and assets without source code.

Trigger: Tasks involving compiled binaries, decompilation, protocol inspection, APK/executable analysis, or closed-source asset reconstruction.

Sources: `morluto/rea`

## Agent Reach (`agent-reach`)

Phase: Cross-Cutting

Open-source CLI and MCP tool providing zero-fee search and extraction across 13+ web platforms (Twitter/X, Reddit, GitHub, YouTube, etc.).

Trigger: Tasks requiring external web research, community thread lookup, GitHub issue mining, or live platform extraction.

Sources: `Panniantong/agent-reach`

## Replica (`replica`)

Phase: Cross-Cutting

Inspects live URLs, screenshots, or videos to rebuild UI and verify fidelity across layout, style, pixels, and motion.

Trigger: Frontend cloning, screenshot-to-code, design-to-UI implementation, or visual fidelity verification.

Sources: `Jakeschincariol/replica-skill`

## Context 7 (`context-7`)

Phase: Cross-Cutting

Upstash's documentation platform and MCP server delivering real-time, version-specific library docs and code examples into coding agents.

Trigger: Any task importing or configuring external libraries, SDKs, or frameworks where API accuracy matters.

Sources: `upstash/context7`

## chrome devTool mcp (`chrome-devtool-mcp`)

Phase: Cross-Cutting

Official Chrome DevTools Protocol MCP server allowing AI coding agents to inspect DOM, monitor network traffic, record traces, and debug live browser sessions.

Trigger: Frontend debugging, DOM/CSS layout inspection, network waterfall analysis, console error triage, or runtime performance tracing.

Sources: `ChromeDevTools/chrome-devtools-mcp`
