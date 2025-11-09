#!/usr/bin/env bash
set -euo pipefail

# Lightweight check for Poetry. This script intentionally exits 0 so
# a container postinstall or postCreateCommand doesn't fail if Poetry
# is not present. It prints helpful instructions instead.

if command -v poetry >/dev/null 2>&1; then
  echo "Poetry found: $(poetry --version 2>/dev/null || true)"
  exit 0
fi

cat <<'MSG'
Warning: Poetry not found in PATH.

This repository uses Poetry for Python dependency management (see api/pyproject.toml).
Install Poetry to enable Python package commands and local development.

Install instructions:
  - Recommended: https://python-poetry.org/docs/#installation
  - Quick (one-line):
      curl -sSL https://install.python-poetry.org | python3 -

If you're running inside a devcontainer, ensure the container has Poetry installed
or the devcontainer's postCreateCommand installs it.

Continuing without Poetry (this check is non-fatal).
MSG

exit 0
