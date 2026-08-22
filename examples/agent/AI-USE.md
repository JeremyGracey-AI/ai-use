---
ai_use_version: "0.1"
assisted: [runtime-generation, drafting, code-scaffolding]
human: [approval-gate, baseline, escalation-policy, accountable-outputs]
review: sampled
accountable: Jane Operator
updated: 2026-08-20
---

This project IS an AI agent, so the declaration covers two layers. Build
layer: I designed the agent; AI scaffolded code that I fully reviewed.
Runtime layer: the agent generates output autonomously within an approved
baseline; outputs are sampled against that baseline rather than individually
reviewed, and anything outside the envelope escalates to me before shipping.
`review: sampled` refers to the runtime layer — declared honestly rather
than hidden. Drift between declared and actual behavior is treated as an
incident, not a footnote.
