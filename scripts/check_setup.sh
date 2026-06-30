#!/usr/bin/env bash
# Sanity-checks the solver setup by running all 3 solvers on one small instance.
# Usage: check_setup.sh [local|hpc]   (default: local)
set -euo pipefail

SETUP="${1:-local}"
DIR="$(cd "$(dirname "$0")" && pwd)"

PYTHON_BIN="python3"
if [ "$SETUP" = "local" ] && [ -x /home/piotr/anaconda3/envs/potassco_env/bin/python ]; then
    PYTHON_BIN=/home/piotr/anaconda3/envs/potassco_env/bin/python
fi

"$PYTHON_BIN" "$DIR/check_setup.py" "$SETUP"
