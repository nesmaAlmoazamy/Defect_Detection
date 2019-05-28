#!/bin/bash
#
#SBATCH --job-name=imageCaptioning
#SBATCH --output=ResultsHalfMInconf
#SBATCH --cpus-per-task=32
#SBATCH --mem 250000
#SBATCH --ntasks=1
#SBATCH --time=100:00:00#!/bin/bash
#
#
cd mask_rcnn_damage_detection
conda activate Development
echo hello
#moduule load keras
python custom.py train --dataset=customImages --weights=coco
