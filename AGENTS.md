# Environment bootstrap for YouTube Codex CLI

# Upgrade pip and install Poetry (if not present)

python -m pip install --quiet --upgrade pip
pip install --quiet poetry

# Install type checker

pip install --quiet pyright

# Install lint/format tools

pip install --quiet ruff black

# Install project dependencies (runtime + dev + test extras)

poetry install --with dev,test

# (Optional) Node dependencies — uncomment if you rely on them

# pnpm install

# Static analysis

pyright cli/ tests/

# Style checks

ruff check .
black --check .

# Run unit tests

pytest -q
