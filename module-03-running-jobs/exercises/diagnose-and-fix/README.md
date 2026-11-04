# Diagnose and fix an application error

A collaborator's script does not always work the first time. In this activity, you will submit a job with an intentional application error, read the output carefully, and try again after fixing it.

<br>

## 1. Submit the job

Start from the repository root (`HPC-Fundamentals`) on the training system. If you are coming from the previous exercise directory, `cd ../../..` returns you to the repository root.

```bash
cd module-03-running-jobs/exercises/diagnose-and-fix
cat batch.slurm
```

Add the account, QOS, constraint, and reservation directives supplied by your instructor. Submit from this directory so the batch script can find `workload.py`:

```bash
sbatch batch.slurm
squeue -u "$USER"
```

This job may finish quickly. Save the job ID printed by `sbatch` so you can find its output.

<br>

## 2. Read the Slurm output carefully

```bash
ls slurm-01_demo-*.out
```

Open the matching file with `less`. For example, if the job ID was `12345`:

```bash
less slurm-01_demo-12345.out
```

In `less`:

- Spacebar moves down.
- `b` moves back up.
- `/Traceback` searches for “Traceback.”
- `q` quits.

Look for output like this (the path and line number may differ):

```text
Training complete.
Traceback (most recent call last):
  ...
    print(result)
NameError: name 'result' is not defined
```

The important lesson:

> Slurm launched the job. The Python application crashed.

Find the failing line in `workload.py`. What variable is the program trying to print? Compare that name with the variable defined above it.

The current batch script prints “Job ended” after Python exits, even if the application failed. That ending message alone does not prove success. Read the application output and traceback.

<br>

## 3. Fix the Python error, then test it interactively

Use your preferred text editor to correct the variable name in your copy of `workload.py`.

Obtain an interactive allocation using the command supplied by your instructor. From this exercise directory, run:

```bash
module load python
srun python workload.py
```

This time, the script should finish with a final results dictionary and no Python traceback. When you are done with the allocation:

```bash
exit
```

<br>

## 4. Resubmit the fixed job

From this exercise directory:

```bash
sbatch batch.slurm
squeue -u "$USER"
ls slurm-01_demo-*.out
```

Use the new job ID to identify and open the new output file with `less`. Check that the corrected script finishes without the traceback.

If you need a working version for comparison, see the neighboring [batch and interactive jobs exercise](../batch-and-interactive-jobs/README.md).

You are finished when you can explain the error, show the corrected result, and distinguish application output from scheduler information.

<br>

<br>

## Navigation

- **Next:** [Module 4: Using Resources Effectively](../../../module-04-using-resources-effectively/README.md)
- **Previous:** [Batch and interactive jobs](../batch-and-interactive-jobs/README.md)
- **Module:** [Module 3: Running Jobs](../../README.md)
- **Course:** [Course Home](../../../README.md)
