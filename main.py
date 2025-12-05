import os, sys
import subprocess
import time
from pathlib import Path

from config import CONFIG
from cmdParser import CustomParser

import pandas as pd
from alive_progress import alive_bar

RESULTS_PATH = 'results'
TIMEOUT = 600



def get_subprocess_answer(command_str):
    start_time = time.time()
    try:
        output = subprocess.check_output(args=[command_str], shell=True, stderr=subprocess.STDOUT, timeout=TIMEOUT)
        time_needed = time.time() - start_time
        result = output.decode().strip()
        return result, round(time_needed, 2)
        
    except subprocess.TimeoutExpired:
        return None, float(TIMEOUT)

   
if __name__ == '__main__':
    parser = CustomParser()
    args = parser.parse_args()
    
    instances_subpath = CONFIG[args.solver]['instances']
    base_dependency_path = Path(__file__).parent.parent / 'dependencies' 
    # /home/piotr/Dresden/ms-dis-nmr-experiments/nmr-experiments/dependencies
    
    reference_df = pd.read_csv(str(base_dependency_path / 'instances/instances_metadata.csv'))
    run_id = f'{args.solver}'
    inst_path = base_dependency_path / instances_subpath
    
    output_path = f'{RESULTS_PATH}/{run_id}.csv'
    os.makedirs(RESULTS_PATH, exist_ok=True)

    if os.path.isfile(output_path):
        outputs_df = pd.read_csv(output_path)
    else:
        outputs_df = pd.DataFrame(columns=['id', 'instance', 'goal', 'standpoint', 'result', 'duration'])

    total_size = len(reference_df)
    inc_count = 0

    with alive_bar(total_size, dual_line=True, title=f'Run ID: {run_id}') as bar:
        for i, (index, row) in enumerate(reference_df.iterrows(), start=1):

            if ((outputs_df['instance'] == row.instance) & (outputs_df['goal'] == row.goal) & (outputs_df['standpoint'] == row.standpoint)).any():
                print(f'Solved for: {row.instance}, goal: {row.goal}, standpoint: {row.standpoint}')
                bar()
                continue

            instance_path =  str(inst_path / row.instance)
            command_str = CONFIG[args.solver][args.setup].format(instance=instance_path)
            res, duration = get_subprocess_answer(command_str)

            row_to_append = pd.DataFrame({
                'id': [int(i)],
                'instance': [row.instance],
                'goal': [row.goal],
                'standpoint': [row.standpoint],
                'result': [res],
                'duration': [duration]                         
            })

            outputs_df = pd.concat([outputs_df, row_to_append], ignore_index=True)
            outputs_df.to_csv(output_path, index=False)
            bar()
