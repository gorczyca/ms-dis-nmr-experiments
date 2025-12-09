import copy



OPTIONS = {
    'instances': '',
    'local': '',
    'hpc': '',
}

CONFIG = {
    'msdis-adm': copy.deepcopy(OPTIONS),
    'msdis-st': copy.deepcopy(OPTIONS),
    'nmsl': copy.deepcopy(OPTIONS)
}


# msdis-adm
CONFIG['msdis-adm']['local'] = '/home/piotr/anaconda3/envs/potassco_env/bin/python /home/piotr/Dresden/ms-dis-nmr-experiments/dependencies/solvers/MS-DIS/msdis.py -p {instance} -b "tt(ta). at(dabf)." -f aba'
CONFIG['msdis-adm']['hpc'] = '/data/horse/ws/pigo271b-nmr/nmr-exp/conda_envs/msdis_env/bin/python /data/horse/ws/pigo271b-nmr/nmr-exp/dependencies/solvers/MS-DIS/msdis.py -p {instance} -b "tt(ta). at(dabf)." -f aba'
CONFIG['msdis-adm']['instances'] = 'instances/msdis'

# msdis-st
CONFIG['msdis-st']['local'] = '/home/piotr/anaconda3/envs/potassco_env/bin/python /home/piotr/Dresden/ms-dis-nmr-experiments/dependencies/solvers/MS-DIS/msdis.py -p {instance} -b "tt(ta). at(dabf)." -f aba'
CONFIG['msdis-st']['hpc'] = '/data/horse/ws/pigo271b-nmr/nmr-exp/conda_envs/msdis_env/bin/python /data/horse/ws/pigo271b-nmr/nmr-exp/dependencies/solvers/MS-DIS/msdis.py -p {instance} -b "tt(ta). at(dabf)." -f aba'
CONFIG['msdis-st']['instances'] = 'instances/msdis'

# nmsl
CONFIG['nmsl']['local'] = '/home/piotr/Dresden/ms-dis-nmr-experiments/dependencies/solvers/nm-s4fsl-asp/run.sh /home/piotr/anaconda3/envs/potassco_env/bin/clingo {instance}'
CONFIG['nmsl']['hpc'] = '/data/horse/ws/pigo271b-nmr/nmr-exp/dependencies/solvers/nm-s4fsl-asp/run.sh /data/horse/ws/pigo271b-nmr/nmr-exp/conda_envs/msdis_env/bin/clingo {instance}'
CONFIG['nmsl']['instances'] = 'instances/nmsl'


# nmsl
# /data/horse/ws/pigo271b-nmr/nmr-exp/dependencies/solvers/nm-s4fsl-asp/run.sh /dev/shm/conda_envs_pigo271b/potassco_env/bin/clingo /data/horse/ws/pigo271b-nmr/nmr-exp/dependencies/instances/nmsl/instance_1_goal-s1-a2.lp