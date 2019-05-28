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
conda activate Development
echo hello
#module load keras
flow --model cfg/yoloCustom.cfg --load 125

