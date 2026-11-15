# 1.1.0 validation

- Ten Python unittest cases pass, covering scanner behavior, secret redaction, malformed config, bounded Stop continuation, approval/ledger reminders, audit applicability, manifest alignment and the resume link.
- New reminder tests first failed against 1.0.0. Initial restricted Windows fixtures also encountered filesystem permission errors; the normal authorized test run passed. Tests read UTF-8 explicitly on Windows.
- Isolated scanner smoke test completed with no errors and preserved all 22 registry capabilities.
- An independent baseline reader identified ambiguous missing-evidence failure handling and absent durable continuation rules. A fresh release reviewer exercised resumed status, expected red tests, urgent WIP shipment and ambiguous tool-execution scenarios under 1.1.0.
- Review found a broken resume guidance path. A failing regression reproduced it; the path was fixed and all ten tests passed. Independent rereview reported no remaining actionable findings.
- Manifest and marketplace structure were checked against the official Claude plugin/marketplace documentation. The Claude CLI is unavailable in this environment, so `claude plugin validate` and live Claude hook integration were not run. This release does not claim live compatibility verification or deterministic enforcement.

These checks establish the tested behavior and instruction interpretation, not a guarantee that every model or host will comply.
