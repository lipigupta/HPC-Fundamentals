# HPC Fundamentals: First Job on a Shared System

## Story for this training

You are a new student or intern joining a research project. A collaborator has given you a messy project directory that contains data files, scripts, notes, old job outputs, and temporary files.

Your job is to log in, copy the inherited project into your own workspace, use terminal commands to inspect and organize the files, run a small Python workload, submit it through Slurm, read the job output carefully when something fails, fix the application error, and see a small example of how requesting more CPUs can speed up a parallel workload.

The Python examples are intentionally simple. You do **not** need to understand machine learning or PyTorch for this session. The Python script is the “payload” for the job.

## Learning outcomes

By the end of this session, you should be able to:

- Use basic terminal commands to navigate and organize files.
- Copy an inherited project into your own workspace.
- Recognize that shared systems have storage limits and quotas.
- Submit a simple batch job using Slurm.
- Use an interactive allocation to test a command.
- Read Slurm output files and distinguish application errors from scheduler messages.
- Recognize that resource requests should match what your code can use.

## 0. Before the workshop

You should already be able to log in to the NERSC system before this session starts. We will not spend much time troubleshooting accounts, MFA, or SSH setup during the workshop.

## 1. Log in and create a workspace

```bash
mkdir -p ~/hpc_fundamentals
cd ~/hpc_fundamentals
pwd
```

Your instructor will tell you where the shared training files are located. Copy them into your workspace.

```bash
cp -r /path/to/shared/hpc_fundamentals_training_scaffold/* ~/hpc_fundamentals/
ls
```

You should see:

```text
README.md
environment/
instructor/
messy_project/
python_black_box/
slurm_scripts/
```

## 2. The inherited messy project

```bash
cd ~/hpc_fundamentals/messy_project
pwd
ls
ls -l
ls results_old
ls temp
find . -maxdepth 3 -type d
```

This directory represents a common situation: someone has shared a project directory with you, but it is not organized for your new work yet.

## 3. Organize the project enough to work with it

This is not about designing the perfect file structure. The goal is to practice terminal basics and get the directory into a usable state.

```bash
mkdir data scripts results logs notes archive
mv data_final_FINAL.txt data/data_final.txt
mv data1.txt data/data_raw.txt
mv script.sh scripts/
mv slurm-10101.out results/
mv slurm-10102.out results/
mv notes.txt notes/
mv random_notes/meeting_notes.txt notes/
mv README_old.md archive/
mv backup/data_copy.txt archive/backup_data_copy.txt
rmdir backup
rmdir random_notes
find . -maxdepth 2
```

Your organization may look different from someone else’s. That is okay.

## 4. A quick note about storage and quotas

On a shared HPC system, storage is not unlimited. Storage limits are often called **quotas**. We will cover storage systems and quota policies in more detail in New User Training. For today, just notice that you can check how much space files use.

```bash
du -sh .
du -sh *
```

The point for today is simple: organized files are easier to understand, easier to debug, and easier to clean up when you are working on a shared system.

## 5. Move to the Python workload

```bash
cd ~/hpc_fundamentals
ls python_black_box
```

You should see:

```text
run_broken.py
run_success.py
scale_demo.py
```

The broken script is meant to fail. It produces output that looks successful at first, then crashes because of a small Python error.

## 6. Submit the broken batch job

```bash
cd ~/hpc_fundamentals/slurm_scripts
cat 01_broken_batch.slurm
sbatch 01_broken_batch.slurm
squeue -u $USER
```

This job may finish quickly. If it disappears from the queue, that usually means it is no longer running.

## 7. While the batch job runs: interactive allocation

Your instructor will provide the exact `salloc` command for the training system or reservation. A generic example looks like this:

```bash
salloc --nodes=1 --ntasks=1 --cpus-per-task=1 --time=00:05:00
```

Once inside the allocation, try running the broken script directly:

```bash
python ../python_black_box/run_broken.py
```

Then try running it through Slurm:

```bash
srun python ../python_black_box/run_broken.py
```

For this simple example, the output may look very similar.

```text
python run.py        # runs Python directly where you are
srun python run.py   # asks Slurm to launch Python using allocated resources
```

When you are done with the interactive allocation:

```bash
exit
```

## 8. Read the Slurm output carefully

```bash
ls slurm-*.out
less slurm-broken-python-<jobid>.out
```

In `less`:

- Spacebar moves down.
- `b` moves back up.
- `/Traceback` searches for the word `Traceback`.
- `q` quits.

Look for this pattern:

```text
Training complete.

Traceback (most recent call last):
  File "../python_black_box/run_broken.py", line 26, in <module>
    print(result)
NameError: name 'result' is not defined
```

You may also see Slurm-related messages after the Python error.

Important lesson:

> Slurm launched the job. The Python application crashed.

The actual problem is not “Slurm failed.” The application failed, and Slurm reported that the task exited with an error code.

## 9. Fix the Python error

```bash
nano ../python_black_box/run_broken.py
```

Find this line:

```python
print(result)
```

Change it to:

```python
print(results)
```

Save and exit, then test it interactively:

```bash
python ../python_black_box/run_broken.py
```

## 10. Resubmit the fixed job

```bash
sbatch 01_broken_batch.slurm
squeue -u $USER
ls slurm-*.out
less slurm-broken-python-<jobid>.out
```

Or submit the provided fixed version:

```bash
sbatch 02_fixed_batch.slurm
```

This time, the script should finish without the Python traceback.

## 11. Optional: CPU scaling demo

This short example shows that requesting more CPUs can reduce runtime **if the code is written to use those CPUs**.

```bash
sbatch 04_scale_1_cpu.slurm
sbatch 05_scale_8_cpu.slurm
sbatch 06_scale_32_cpu.slurm
```

When they finish, compare the output files:

```bash
grep Runtime slurm-scale-*.out
```

Expected pattern:

```text
1 CPU    -> slowest
8 CPUs   -> faster
32 CPUs  -> fastest
```

The exact times may vary.

Important lesson:

> Asking for more resources only helps if your application can use them.

## Command reference

### Navigation

```bash
pwd
ls
ls -l
cd directory_name
cd ..
```

### File and directory operations

```bash
mkdir new_directory
mv oldname newname
mv file directory/
cp source destination
cp -r source_directory destination_directory
rmdir empty_directory
rm filename
```

Be careful with `rm -r directory_name`: it removes a directory and everything inside it.

### Inspecting files

```bash
cat filename
less filename
head filename
tail filename
```

### Disk usage

```bash
du -sh .
du -sh *
```

### Slurm basics

```bash
sbatch job_script.slurm
squeue -u $USER
srun command
salloc --time=00:05:00 --nodes=1 --ntasks=1 --cpus-per-task=1
```

## Big idea

This session is not about memorizing every command. The goal is to practice a common HPC workflow:

> Access the system, understand your files, run your code, read the output, fix errors, and try again.
