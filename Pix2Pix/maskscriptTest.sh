#!/bin/bash
#
#SBATCH --job-name=GANMask
#SBATCH --output=ResultGANTestMask
#SBATCH --cpus-per-task=32
#SBATCH --mem 250000
#SBATCH --ntasks=1
#SBATCH --time=100:00:00#!/bin/bash
#
#
conda activate Development
echo hello
python test.py --dataroot ./datasets/customDSMask --name custom_pix2pixMask --model pix2pix --direction AtoB --gpu_ids -1
