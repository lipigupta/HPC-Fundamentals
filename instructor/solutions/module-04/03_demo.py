#!/usr/bin/env python
"""
Lightweight CPU scaling demo.

This script creates many independent short tasks. It uses the number of CPUs
requested from Slurm via SLURM_CPUS_PER_TASK.
"""
import os
import time
from multiprocessing import Pool
TASKS = 32
SLEEP_SECONDS = 1
def work(task_id):
    time.sleep(SLEEP_SECONDS)
    return task_id
if __name__ == "__main__":
    cpus = int(os.environ.get("SLURM_CPUS_PER_TASK", "1"))
    print(f"SLURM_CPUS_PER_TASK={cpus}")
    print(f"Running {TASKS} independent tasks using {cpus} worker process(es)...")
    start = time.time()
    with Pool(processes=cpus) as pool:
        results = pool.map(work, range(TASKS))
    end = time.time()
    print(f"Completed {len(results)} tasks.")
    print(f"Runtime: {end - start:.2f} seconds")
