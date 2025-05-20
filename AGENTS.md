# Install type checker
pip install pyright                 # Adds static type checking

# Install dependencies (runtime + dev + test extras)
poetry install --with dev,test      # Installs all Python deps, incl. dev + tests
pnpm install                        # Installs Node deps if a lockfile/package.json exists

# Run static analysis
pyright cli/ tests/                 # Type-check CLI package and test suite
ruff check .                        # Lint the entire repository
black --check .                     # Verify Black code style (non-destructive)

# Run unit tests
pytest -q                           # Execute tests quietly, fail on first error
