# AI-USE.md

**A LICENSE-style file that declares how AI was used in a project — plus a checker that keeps the declaration honest.**

[![AI-USE: declared](https://img.shields.io/badge/AI--USE-declared-2ea44f)](./AI-USE.md)

## The stance

Yes, AI is part of how I work. Teaching people to build with AI is my job — it would be odd if it wasn't. Here is the actual split: I build the thing first. AI helps me draft from my own notes and past writing, and helps me build the diagrams. Then I edit until it sounds like me, which usually takes a few passes. I read and approve everything before it goes out.

The projects are mine. The opinions are mine. If something is wrong, that is on me.

I hold my agents to a declared-vs-actual standard — approved baseline, verifiable evidence, human gate. This repo applies the same standard to my own output.

## What this is (and isn't)

This is **my** disclosure practice: versioned, public, forkable. It is not "the" standard, and I'm not asking anyone to adopt it. If it's useful, fork it and make it yours. What makes it more than a values page is the checker: CI fails when a repo stops declaring, or when the declaration goes stale.

## Quick start

1. Copy `AI-USE.md` from this repo (or an [example](./examples/)) to your project root.
2. Fill the four fields: **assisted**, **human**, **review**, **accountable**.
3. Add the check to CI:

```yaml
# .github/workflows/ai-use.yml
name: AI-USE
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: JeremyGracey-AI/ai-use/check@main
        with:
          max-age-days: 180
```

Full format: [SPEC.md](./SPEC.md). This repo declares itself: [AI-USE.md](./AI-USE.md).

## The three tiers

The full statement doesn't fit everywhere. Three sizes, one source of truth:

| Tier | Words | Where |
|---|---|---|
| Badge | ~8 | texts, Slack, bios, slide corners |
| Signature | ~30 | email, doc footers, READMEs |
| Full statement | ~120 | jeremygracey.ai/ai, this repo, long-form posts |

Wording for each tier: [TIERS.md](./TIERS.md).

## Content-specific declarations

The general statement covers projects. Some content types carry a stricter,
more specific declaration:

- **[WRITING.md](./WRITING.md)** — the written word. Thoughts, feelings, and
  beliefs are mine; AI never drafts, never writes in my voice, never produces
  an argument presented as my own idea. It scans subjects, argues with
  structure, and proofreads. First drafts are spoken (Wispr Flow), not
  generated.

## Adopters

- [governance-drift-researcher](https://github.com/JeremyGracey-AI/governance-drift-researcher)
- triton-kernel-lab
- nexus-neuromirror
- llm-council-mcp
- marketing-copy-audit

(Prefilled declarations for these live in [adoption/](./adoption/).)

## License

MIT. The spec text is yours to fork without attribution — the point is the practice, not the credit.
