#!/usr/bin/env bash
set -euo pipefail

# Upgrade pip and install Python tooling
python -m pip install --quiet --upgrade pip
pip install --quiet pyright ruff black poetry

# Install project dependencies (runtime + dev + test extras)
poetry install --with dev,test

# Install Node dependencies if the project uses them
if [ -f "pnpm-lock.yaml" ] || [ -f "package.json" ]; then
  pnpm install --frozen-lockfile
fi
