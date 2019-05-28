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
#moduule load keras
python setup.py build_ext --inplace
pip install -e .
pip install .
python flow --model cfg/yoloCustom.cfg --load weights/yolo.weights --train --annotation train/Annotations --dataset train/Images --epoch 300
