#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=4000
#SBATCH --job-name=msdis-st
#SBATCH --mail-type=end
#SBATCH --mail-user=pigo271b@tu-dresden.de



srun --exclusive --ntasks=1 /dev/shm/conda_envs_pigo271b/potassco_env/bin/python /data/horse/ws/pigo271b-nmr/nmr-exp/ms-dis-nmr-experiments/main.py -s msdis-st -u hpc

echo "waiting for all jobs to complete"
wait
echo "all parallel tasks finished"