#!/bin/bash

# List of files to submit
# FILES=(
#     "abagraph-st-aspforaba.sh" 
#     "abagraph-st-flexable.sh" 
#     "abagraph-st-flexable-sws.sh" 
#     "abagraph-st-msdis.sh" 
#     "iccma-st-aspforaba.sh" 
#     "iccma-st-flexable.sh" 
#     "iccma-st-flexable-sws.sh" 
#     "iccma-st-msdis.sh" 
#     "abagraph-adm-aspforaba.sh" 
#     "abagraph-adm-flexable.sh" 
#     "abagraph-adm-msdis.sh" 
#     "iccma-adm-aspforaba.sh" 
#     "iccma-adm-flexable.sh" 
#     "iccma-adm-msdis.sh" 
# )

# APPROX
FILES=(
    "msdis-adm-s.sh" 
    "msdis-st-s.sh" 
    "nmsl-s.sh" 
)

for FILE in "${FILES[@]}"; do
    sbatch "$FILE"
done