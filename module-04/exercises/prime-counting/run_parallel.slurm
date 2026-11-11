#!/bin/bash
# Parallel Prime Counting - Slurm Batch Script
#
# Submit a multiprocessing Python program to Perlmutter.
#
# Slurm allocates CPU resources, while Python's
# multiprocessing module creates worker processes.
#
# The number of requested CPUs is passed to Python using
# the environment variable SLURM_CPUS_PER_TASK.
#
# Example submissions:
#
#   sbatch -A <account> --cpus-per-task=2 run_parallel.slurm
#   sbatch -A <account> --cpus-per-task=4 run_parallel.slurm
#   sbatch -A <account> --cpus-per-task=8 run_parallel.slurm
#
# All workers run on the same compute node.
# This example does not use MPI or multiple nodes.

# 1. Slurm job configuration

#SBATCH --job-name=prime-parallel

# Run on a Perlmutter CPU node.
#SBATCH --constraint=cpu

# Use the shared queue for a small CPU job.
#SBATCH --qos=shared

# Keep the multiprocessing workload on one node.
#SBATCH --nodes=1

# Start one main Python application.
# The application creates its own worker processes.
#SBATCH --ntasks=1

# Reserve two logical CPUs by default.
# Override this value when submitting the job.
#SBATCH --cpus-per-task=2

# Maximum allowed job runtime: 5 minutes.
#SBATCH --time=00:05:00

# Write output to a file containing the Slurm job ID.
#SBATCH --output=prime-parallel-%j.out

# 2. Prepare the execution environment

set -euo pipefail

cd "$SLURM_SUBMIT_DIR"

# 3. Configure the parallel application

# Slurm defines SLURM_CPUS_PER_TASK based on the CPU request.
#
# For example:
#   --cpus-per-task=4
#   SLURM_CPUS_PER_TASK=4
#
# We pass this value to Python as --workers.
#
# This connection is explicit: Slurm does NOT automatically
# launch the Python multiprocessing workers.

WORKERS="${SLURM_CPUS_PER_TASK}"

# 4. Run the parallel application

python3 prime-counting_parallel.py \
    --limit 2000000 \
    --workers="$WORKERS"
