#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=32000
#SBATCH --job-name=msdis-adm
#SBATCH --mail-type=end
#SBATCH --mail-user=pigo271b@tu-dresden.de



srun --exclusive --ntasks=1 /data/horse/ws/pigo271b-nmr/nmr-exp/conda_envs/msdis_env/bin/python /data/horse/ws/pigo271b-nmr/nmr-exp/ms-dis-nmr-experiments/main.py -s msdis-adm -u hpc

echo "waiting for all jobs to complete"
wait
echo "all parallel tasks finished"