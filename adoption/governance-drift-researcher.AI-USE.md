---
ai_use_version: "0.1"
assisted: [code-scaffolding, drafting, diagrams, tests]
human: [architecture, detection-logic, opinions, final-edit]
review: full
accountable: Jeremy Gracey
updated: 2026-08-20
---

The premise — deployed agents drift from their approved baseline, and every
finding needs verifiable evidence plus a human approval gate — is mine. AI
scaffolded code and drafted docs from my design notes. I reviewed every line
before release, including the PyPI package (governance-drift).

TODO(jeremy): confirm the assisted list matches how this repo was actually
built (tests? diagrams?) before committing.
