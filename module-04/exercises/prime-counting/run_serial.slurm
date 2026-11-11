#!/bin/bash
# Sequential Prime Counting - Slurm Batch Script

# Submit a sequential Python program to a Perlmutter CPU node.
#
# This job requests one Slurm task and one CPU per task.
# The Python program itself uses only one worker process.
#
# To show that additional CPU allocations do not
# automatically parallelize sequential code, submit the
# same script with different CPU requests:
#
#   sbatch -A <account> --cpus-per-task=1 run_serial.slurm
#   sbatch -A <account> --cpus-per-task=8 run_serial.slurm
#
# Replace <account> with your NERSC project account.
# Both submissions execute the SAME sequential Python code.
#



# 1. Slurm job configuration

#SBATCH --job-name=prime-serial

# Run on a Perlmutter CPU node, not a GPU node.
#SBATCH --constraint=cpu

# Use the shared queue for a small CPU job.
#SBATCH --qos=shared

# Request resources on one compute node.
#SBATCH --nodes=1

# Launch one application task (one Python program).
#SBATCH --ntasks=1

# Reserve one logical CPU for the task by default.
# This value can be overridden with sbatch.
#SBATCH --cpus-per-task=1

# Maximum allowed job runtime: 5 minutes.
#SBATCH --time=00:05:00

# Write stdout and stderr to a job-specific output file.
# %j is replaced with the Slurm job ID.
#SBATCH --output=prime-serial-%j.out

# 2. Prepare the execution environment

# Stop on command errors, unset variables, or pipeline errors.
set -euo pipefail

# Execute from the directory where sbatch was submitted.
cd "$SLURM_SUBMIT_DIR"

# 3. Run the sequential application

# Only one Python process performs the prime counting,
# regardless of how many CPUs Slurm allocated.
python3 prime-counting_serial.py --limit 2000000
