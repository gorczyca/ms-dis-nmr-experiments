#!/usr/bin/env bash
# Run locally. Syncs dependencies/, pulls latest code on HPC, submits the slurm jobs.
set -euo pipefail

REMOTE_HOST="hpc"
REMOTE_BASE="/data/horse/ws/pigo271b-thesis_experiments"
DIR="$(cd "$(dirname "$0")" && pwd)"

"$DIR/sync_dependencies.sh"

ssh "$REMOTE_HOST" "cd $REMOTE_BASE/ms-dis-nmr-experiments && git pull && cd slurm && bash submit-sbatch.sh"
