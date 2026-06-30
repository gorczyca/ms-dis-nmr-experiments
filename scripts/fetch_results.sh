#!/usr/bin/env bash
# Run locally. Pulls results/*.csv back from the HPC workspace.
set -euo pipefail

REMOTE_HOST="hpc"
REMOTE_BASE="/data/horse/ws/pigo271b-thesis_experiments"
LOCAL_RESULTS="$(cd "$(dirname "$0")/../.." && pwd)/results"

mkdir -p "$LOCAL_RESULTS"
rsync -avz "$REMOTE_HOST:$REMOTE_BASE/ms-dis-nmr-experiments/results/" "$LOCAL_RESULTS/"
