#!/usr/bin/env python3
"""Validate an AI-USE.md declaration. Dependency-free (stdlib only).

Usage: check_ai_use.py [PATH] [--max-age-days N]
  PATH            directory containing AI-USE.md (default: .)
  --max-age-days  fail if `updated` is older than N days (default: 365; 0 disables)

Exit codes: 0 ok, 1 invalid, 2 missing file.
Spec: https://github.com/JeremyGracey-AI/ai-use/blob/main/SPEC.md
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

REQUIRED = ["ai_use_version", "assisted", "human", "review", "accountable", "updated"]
LIST_FIELDS = ["assisted", "human"]
REVIEW_LEVELS = {"full", "sampled", "none"}

def parse_frontmatter(text):
    """Minimal YAML-subset parser: scalars, inline flow lists, dash lists."""
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", text, re.DOTALL)
    if not m:
        return None, None
    fields, current_list_key = {}, None
    for raw in m.group(1).splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        dash = re.match(r"\s+-\s+(.*)", line)
        if dash and current_list_key:
            fields[current_list_key].append(dash.group(1).strip().strip("'\""))
            continue
        kv = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)", line)
        if not kv:
            return None, f"unparseable line in frontmatter: {line!r}"
        key, value = kv.group(1), kv.group(2).strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip("'\"") for v in value[1:-1].split(",")]
            fields[key] = [v for v in items if v]
            current_list_key = None
        elif value == "":
            fields[key] = []
            current_list_key = key  # expect dash list
        else:
            fields[key] = value.strip("'\"")
            current_list_key = None
    return fields, None

def check(directory, max_age_days):
    path = Path(directory) / "AI-USE.md"
    if not path.is_file():
        print(f"FAIL: {path} not found — this project does not declare its AI use")
        return 2
    text = path.read_text(encoding="utf-8")
    fields, err = parse_frontmatter(text)
    errors = []
    if fields is None:
        print(f"FAIL: {err or 'no YAML frontmatter block (--- ... ---) at top of AI-USE.md'}")
        return 1

    for key in REQUIRED:
        if key not in fields:
            errors.append(f"missing required field: {key}")
    for key in LIST_FIELDS:
        if key in fields:
            if not isinstance(fields[key], list) or not fields[key]:
                errors.append(f"{key} must be a non-empty list")
    review = fields.get("review")
    if review is not None and review not in REVIEW_LEVELS:
        errors.append(f"review must be one of {sorted(REVIEW_LEVELS)}, got {review!r}")
    acct = fields.get("accountable")
    if isinstance(acct, str) and not acct.strip():
        errors.append("accountable must name a person")

    updated = fields.get("updated")
    if updated is not None and not isinstance(updated, list):
        try:
            when = datetime.date.fromisoformat(str(updated))
            age = (datetime.date.today() - when).days
            if age < 0:
                errors.append(f"updated is in the future: {updated}")
            elif max_age_days and age > max_age_days:
                errors.append(
                    f"declaration is stale: updated {updated} is {age} days old "
                    f"(max {max_age_days}) — a stale declaration is a false declaration"
                )
        except ValueError:
            errors.append(f"updated must be YYYY-MM-DD, got {updated!r}")

    m = re.match(r"\A---\s*\n.*?\n---\s*\n(.*)\Z", text, re.DOTALL)
    if m and not m.group(1).strip():
        errors.append("freeform statement after frontmatter is required")

    if errors:
        print(f"FAIL: {path}")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {path}")
    print(f"  assisted:    {', '.join(fields['assisted'])}")
    print(f"  human:       {', '.join(fields['human'])}")
    print(f"  review:      {fields['review']}")
    print(f"  accountable: {fields['accountable']} (updated {fields['updated']})")
    return 0

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("--max-age-days", type=int, default=365)
    args = ap.parse_args()
    sys.exit(check(args.path, args.max_age_days))

if __name__ == "__main__":
    main()
