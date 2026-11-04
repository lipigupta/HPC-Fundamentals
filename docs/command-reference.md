# Command Reference

This course is not about memorizing every command. Use this sheet when you need a reminder of how to move around, inspect files, or run a job.

<br>

## Terminal Basics

- Replace example names such as `filename`, `directory_name`, and `job_script.slurm` with your own file or directory names.
- Commands use your **current directory** unless you give another path. Use `pwd` to check where you are.
- A relative path, such as `results_old`, starts from your current directory. An absolute path starts with `/`.
- `.` means the current directory, `..` means its parent, and `~` means your home directory. `~/messy_project` only works if that directory is actually in your home directory.
- Put paths containing spaces in quotes, for example `cd "my project"`.
- Options such as `-l` change what a command does. `*` matches names in the current directory; by default, it does not include names beginning with a dot.

<br>

## Navigate directories

| Command | What it does | Example |
|---|---|---|
| `pwd` | Prints the full path to your current directory. | `pwd` |
| `ls` | Lists files and directories. | `ls` |
| `ls -l` | Shows permissions, owner, size in bytes, and modification time. | `ls -l` |
| `ls directory_name` | Lists a directory's contents without moving into it. | `ls results_old` |
| `cd directory_name` | Changes your current directory. | `cd messy_project` |
| `cd ..` | Moves up one directory level. | `cd ..` |
| `cd ~` | Moves to your home directory. | `cd ~` |
| `find . -maxdepth 3 -type d` | Finds directories starting here, up to three levels down. | `find . -maxdepth 3 -type d` |

<br>

## Manage files

| Command | What it does | Example |
|---|---|---|
| `mkdir directory_name` | Creates a directory. | `mkdir results` |
| `mv oldname newname` | Renames a file or directory. | `mv data_final_FINAL.txt data_final.txt` |
| `mv filename directory_name/` | Moves a file into a directory. | `mv data_final.txt data/` |
| `cp source destination` | Copies a file. | `cp notes.txt notes_backup.txt` |
| `cp -R source_directory destination_directory` | Copies a directory and its contents. | `cp -R messy_project messy_project_backup` |
| `rmdir directory_name` | Removes an empty directory. | `rmdir empty_directory` |
| `rm filename` | Deletes a file. | `rm unwanted_file.txt` |

Check source and destination names before copying or moving: existing files can be overwritten. For the directory-copy example above, `messy_project_backup` is a new destination; if it already exists as a directory, the source directory is copied inside it.

Be careful with `rm -r directory_name`: it removes the directory and everything inside it. Terminal deletion does not normally move files to the Trash.

<br>

## Inspect files

| Command | What it does | Example |
|---|---|---|
| `cat filename` | Prints a file's contents. | `cat batch.slurm` |
| `less filename` | Opens a file for scrolling and searching. | `less notes.txt` |
| `head filename` | Prints the first ten lines by default. | `head notes.txt` |
| `tail filename` | Prints the last ten lines by default. | `tail notes.txt` |
| `grep pattern filename` | Prints lines matching a pattern. | `grep Runtime slurm-scale-*.out` |

<br>

## Moving around in `less`

| Key | What it does |
|---|---|
| Spacebar | Moves down one screen. |
| `b` | Moves back up one screen. |
| `/Traceback`, then Enter | Searches forward for “Traceback.” |
| `n` | Goes to the next search match. |
| `q` | Quits and returns to the terminal. |

<br>

## Check storage usage

| Command | What it does | Example |
|---|---|---|
| `du -sh .` | Summarizes disk usage for the current directory, including its contents, in readable units. | `du -sh .` |
| `du -sh *` | Summarizes disk usage for each matching file or directory here. | `du -sh *` |

`du` shows usage, not your storage quota. Shared systems have storage limits; your instructor will explain any quota commands needed for the course.

<br>

## Run and monitor jobs

Run these commands on the training system. Use the account, QOS, constraint, and reservation details supplied by your instructor. Run each exercise's batch script from its exercise directory so it can find `workload.py`.

| Command | What it does | Example |
|---|---|---|
| `sbatch job_script.slurm` | Submits a batch script and prints a job ID. | `sbatch batch.slurm` |
| `squeue -u "$USER"` | Shows your jobs currently listed in the queue. `$USER` expands to your username. | `squeue -u "$USER"` |
| `salloc [options]` | Requests an interactive allocation. Replace `[options]` with instructor-provided resource and account settings. | See the [interactive allocation guidance](../module-03/exercises/batch-and-interactive-jobs/README.md#3-try-an-interactive-allocation). |
| `srun command` | Launches a job step using Slurm resources. | Inside your allocation: `srun python workload.py` |
| `exit` | Leaves the current shell; use it to finish the allocation shell when instructed. | `exit` |

`python workload.py` runs Python on the current host. `srun python workload.py` asks Slurm to launch it using allocated resources. Follow the instructor's guidance about where to run commands.

A job leaving the queue does not establish success. Find the output file using the job ID and inspect it. The course scripts use filenames such as `slurm-01_demo-12345.out`, where `12345` is the job ID.

> Slurm launched the job. The Python application crashed.

A Python traceback helps you identify an application error. See [Diagnose and fix](../module-03/exercises/diagnose-and-fix/README.md) for the guided example.
