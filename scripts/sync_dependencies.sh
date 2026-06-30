#!/usr/bin/env bash
# Run locally. Syncs dependencies/ (solvers + instances) to the HPC workspace,
# since dependencies/ is gitignored and not part of this repo.
set -euo pipefail

REMOTE_HOST="hpc"
REMOTE_BASE="/data/horse/ws/pigo271b-thesis_experiments"
LOCAL_DEPENDENCIES="$(cd "$(dirname "$0")/../.." && pwd)/dependencies"

rsync -avz --delete "$LOCAL_DEPENDENCIES/" "$REMOTE_HOST:$REMOTE_BASE/dependencies/"
