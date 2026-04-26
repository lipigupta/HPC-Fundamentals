#!/bin/bash
#SBATCH --job-name=scale-8cpu
#SBATCH --time=00:05:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --output=slurm-%x-%j.out
# NERSC users may need project/account/QOS/constraint directives.
# Example placeholders:
# #SBATCH --account=<your_project>
# #SBATCH --qos=<debug_or_reservation_qos>
# #SBATCH --constraint=cpu

echo "Job started on $(date)"
echo "Running on host: $(hostname)"
echo "Working directory: $(pwd)"
echo "SLURM_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK"
echo

python ../python_black_box/scale_demo.py

echo
echo "Job ended on $(date)"
