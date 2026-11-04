# Batch and interactive jobs

## 1. Move to the Python workload

Start from the repository root (`HPC-Fundamentals`) on the training system:

```bash
cd module-03/exercises/batch-and-interactive-jobs
pwd
ls
cat workload.py
cat batch.slurm
```

You should see `README.md`, `workload.py`, `batch.slurm`, and `interactive.sh`. The Python file contains the work to be done. The batch script describes the resources requested and the commands to run.

Before submitting, add the account, QOS, constraint, and reservation directives supplied by your instructor. Submit from this exercise directory so the script can find `workload.py`.

<br>

## 2. Submit the job

```bash
sbatch batch.slurm
squeue -u "$USER"
```

`sbatch` submits the batch script and prints a job ID. `squeue -u "$USER"` shows your jobs in the queue.

This job may finish quickly. If it disappears from the queue, it is no longer listed there; check the output to find out what happened.

<br>

## 3. Try an interactive allocation

Your instructor will provide the exact `salloc` command for the training system or reservation. Read `interactive.sh` for an example of the commands involved. It is a command reference, not a script to submit with `sbatch`.

Once your allocation is ready, make sure you are still in this exercise directory, then launch the workload:

```bash
module load python
srun python workload.py
```

The difference between direct execution and a Slurm job step is:

```text
python workload.py        # runs Python on the current host
srun python workload.py   # asks Slurm to launch Python using allocated resources
```

An allocation alone does not mean a direct Python command runs on a compute node. Use the instructor's guidance about where to run commands.

When you are done with the interactive allocation:

```bash
exit
```

<br>

## 4. Read the output

Back in the exercise directory, find your batch output:

```bash
ls slurm-02_demo-*.out
```

The filename includes the job ID printed by `sbatch`. Open the matching file with `less`. For example, if the job ID was `12345`:

```bash
less slurm-02_demo-12345.out
```

In `less`:

- Spacebar moves down.
- `b` moves back up.
- `/Training` searches for “Training.”
- `q` quits.

You should see five epochs followed by a final results dictionary. The values may vary. Inspect the application output rather than relying only on whether the job has left the queue.

You are finished when you can locate your batch output and explain the difference between submitting a batch job and launching a step inside an interactive allocation.

<br>

<br>

## Navigation

- **Next:** [Diagnose and fix](../diagnose-and-fix/README.md)
- **Previous:** [Organize a project](../../../module-02/exercises/organize-a-project/README.md)
- **Module:** [Module 3: Running Jobs](../../README.md)
- **Course:** [Course Home](../../../README.md)
