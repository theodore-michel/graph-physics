#!/bin/bash
#
#SBATCH --job-name=predict
#SBATCH --output=predict.log
#
#SBATCH --nodes 1
#SBATCH --ntasks 8 
#SBATCH --ntasks-per-node=8
#SBATCH --ntasks-per-core=1
#SBATCH --threads-per-core=1
#SBATCH --partition=GPU
#SBATCH --qos=gpu
#SBATCH --nodelist=node-99
#SBATCH --gres=gpu:1g.5gb:1

# Set environment variable for OpenMP
export OMP_PROC_BIND=true

# Set wand offline
export WANDB_MODE=offline

# Execute MPI run
python -m graphphysics.predict \
            --predict_parameters_path=predict_config/panels.json \
            --no_edge_feature \
            --model_path=/model.ckpt \
