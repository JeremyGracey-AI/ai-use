# AI-USE.md — Specification v0.1

## Purpose

A single file at project root that declares how AI was used in the project. Machine-checkable header, human-readable statement. The declaration is a claim of fact, not a values statement: every line must be checkable against the actual work.

## File

`AI-USE.md` at the repository root. One file per project.

## Format

YAML frontmatter (checked by CI) followed by a freeform statement (read by humans).

```markdown
---
ai_use_version: "0.1"
assisted: [drafting, diagrams, code-scaffolding]
human: [architecture, opinions, final-edit, decisions]
review: full
accountable: Jeremy Gracey
updated: 2026-08-20
---

Freeform statement here — what the fields mean for THIS project,
in plain language. Required. No length rules.
```

## Required fields

Four content fields, two metadata fields. There is deliberately no fifth content field.

| Field | Type | Meaning |
|---|---|---|
| `assisted` | list | What AI touched. Suggested terms: `drafting`, `diagrams`, `code-scaffolding`, `tests`, `research`, `refactoring`, `copy-editing` |
| `human` | list | What stayed human. Suggested terms: `architecture`, `opinions`, `decisions`, `final-edit`, `data`, `conclusions` |
| `review` | enum | How much of the AI-touched output a human read: `full` \| `sampled` \| `none` |
| `accountable` | string | A person's name. Not a team, not a company. Errors land on this person. |
| `ai_use_version` | string | Spec version this file follows |
| `updated` | date | `YYYY-MM-DD`. The declaration covers the artifact as of this date. |

## Review levels

- **`full`** — a human read every AI-touched line and could defend it.
- **`sampled`** — a human reviewed representative portions; unreviewed output may exist.
- **`none`** — published without human review. Declaring this honestly is the point; hiding it is the failure mode this spec exists for.

## Semantics

1. **Staleness is falsehood.** The declaration covers the project at `updated`. If how AI is used changes materially, bump `updated` in the same change. An out-of-date declaration is a false declaration — CI treats stale as failing.
2. **The statement binds the header.** The freeform statement must be consistent with the fields. `review: full` plus a statement admitting unreviewed output is invalid (human judgment; CI cannot catch this).
3. **Scope is the whole artifact.** If parts of the project differ materially (e.g., docs vs. core engine), say so in the statement rather than adding fields.
4. **Forks own their declarations.** A fork inherits the file format, never the claims. First commit to a fork should rewrite AI-USE.md or delete it.

## Non-goals

- Not a provenance standard. For cryptographic provenance of media, use C2PA Content Credentials. Nothing here proves anything; it stakes a name on a claim.
- Not a compliance instrument. This makes no attempt to satisfy the EU AI Act or any platform's disclosure policy, though it may overlap.
- Not a metric. `review: full` is not "better" than `sampled` — accurate is better than inaccurate.
