#!/bin/bash
#
#SBATCH --job-name=GAN
#SBATCH --output=ResultGANTest
#SBATCH --cpus-per-task=32
#SBATCH --mem 250000
#SBATCH --ntasks=1
#SBATCH --time=100:00:00#!/bin/bash
#
#
conda activate Development
echo hello
python test.py --dataroot ./datasets/customDS --name custom_pix2pix --model pix2pix --direction BtoA --gpu_ids -1
