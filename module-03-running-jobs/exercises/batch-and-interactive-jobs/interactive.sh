#!/bin/bash
# This file is not submitted with sbatch.
# It contains commands learners can copy/paste during the interactive allocation activity.

# Example:
# salloc --account=ntrain1 --constraint cpu --qos interactive --nodes 1 --ntasks 1 --cpus-per-task 8 --time=00:10:00 --reservation=hpcfun
# Once inside the allocation:
# module load python
# python workload.py
# srun python workload.py

# When done:
# exit
