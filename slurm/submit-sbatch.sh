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
    "abagraph-st-aspforaba.sh" 
    "abagraph-st-flexable.sh" 
    "abagraph-st-flexable-sws.sh" 
    "abagraph-st-msdis.sh" 
    "iccma-st-aspforaba.sh" 
    "iccma-st-flexable.sh" 
    "iccma-st-flexable-sws.sh" 
    "iccma-st-msdis.sh" 
    "abagraph-adm-aspforaba.sh" 
    "abagraph-adm-flexable.sh" 
    "abagraph-adm-msdis.sh" 
    "iccma-adm-aspforaba.sh" 
    "iccma-adm-flexable.sh" 
    "iccma-adm-msdis.sh" 
    # Singleshot
    "iccma-adm-msdis-singleshot.sh" 
    "abagraph-adm-msdis-singleshot.sh" 
    # Approx
    "iccma-adm-flexable-ap-05.sh"
    "iccma-adm-flexable-ap-10.sh"
    "iccma-adm-flexable-ap-25.sh"
    "iccma-adm-flexable-ap-50.sh"
    "iccma-adm-flexable-ap-60.sh"
    "iccma-adm-flexable-ap-70.sh"
    "iccma-adm-flexable-ap-80.sh"
    "iccma-adm-flexable-ap-90.sh"
    "iccma-adm-msdis-ap-05.sh"
    "iccma-adm-msdis-ap-10.sh"
    "iccma-adm-msdis-ap-25.sh"
    "iccma-adm-msdis-ap-50.sh"
    "iccma-adm-msdis-ap-100.sh"
    "iccma-adm-msdis-ap-200.sh"
)

for FILE in "${FILES[@]}"; do
    sbatch "$FILE"
done