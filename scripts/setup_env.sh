#!/usr/bin/env bash
# Run ON the HPC login node. Creates the conda env the slurm jobs and config.py
# 'hpc' commands expect at conda_envs/msdis_env: clingo (MS-DIS + nm-s4f-sl) and
# pandas/alive_progress (main.py orchestrator).
set -euo pipefail

# Uncomment/adjust if your cluster needs an explicit module load for conda:
# module load Miniconda3

REMOTE_BASE="/data/horse/ws/pigo271b-thesis_experiments"
ENV_DIR="$REMOTE_BASE/conda_envs/msdis_env"
ENV_YML="$REMOTE_BASE/dependencies/solvers/MS-DIS/environment.yml"

conda env create -p "$ENV_DIR" -f "$ENV_YML"
conda run -p "$ENV_DIR" pip install pandas alive_progress
