#!/usr/bin/env bash
# One-time: init and publish this repo.
set -euo pipefail
git init -b main
git add -A
git commit -m "AI-USE.md v0.1 — spec, checker, and my own declaration"
gh repo create JeremyGracey-AI/ai-use --public --source=. --push
echo "Live: https://github.com/JeremyGracey-AI/ai-use"
