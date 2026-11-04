# Organize a project

Your collaborator has shared a messy project directory. Organize it so you can find and work with its files.

<br>

## 1. The inherited messy project

Start from the repository root (`HPC-Fundamentals`). You already have your own copy of the course files from the workspace setup. Move into the inherited project and take a look around:

```bash
cd module-02/exercises/organize-a-project/messy_project
pwd
ls
ls -l
ls results_old
ls temp
find . -maxdepth 3 -type d
```

Here is what each command does:

| Command | What it does |
|---|---|
| `cd module-02/exercises/organize-a-project/messy_project` | Moves into the messy project directory from the repository root. `cd` means “change directory.” |
| `pwd` | Prints the full path to your current directory so you can check where you are. |
| `ls` | Lists the names of files and directories in your current directory. |
| `ls -l` | Shows a detailed listing, including permissions, owner, size in bytes, and modification time. |
| `ls results_old` | Lists what is inside `results_old` without moving into it. |
| `ls temp` | Lists what is inside `temp` without moving into it. |
| `find . -maxdepth 3 -type d` | Finds directories starting here (`.`), looking up to three levels down. `-type d` limits the results to directories. |

<br>

This directory represents a common situation: someone has shared a project directory with you, but it is not organized for your new work yet.

As you look around, ask yourself: which files belong together? Which look like data, scripts, notes, or results from an old run?

<br>

## 2. Organize the project enough to work with it

This is not about designing the perfect file structure. The goal is to practice terminal basics and get the directory into a usable state.

Your organization may look different from someone else’s. That is okay.

Inspect the inherited data, scripts, notes, logs, and temporary files. Use `mkdir`, `mv`, `cp`, and `rmdir` to organize them into useful folders. `rm` deletes files, and `rm -r` deletes whole directory trees.

<br>

You are finished when you can explain your organization, locate a data file and a job output, and describe which commands you used. Complete the corresponding Canvas activity, then continue to Module 3 from the repository root.

The point for today is simple: organized files are easier to understand, easier to debug, and easier to clean up when you are working on a shared system.

<br>

## 3. A quick note about storage and quotas

On a shared HPC system, storage is not unlimited. Storage limits are often called **quotas**. We will cover storage systems and quota policies in more detail in New User Training. For today, just notice that you can check how much space files use.

```bash
du -sh .
du -sh *
```

<br>

<br>

## Navigation

- **Next:** [Batch and interactive jobs](../../../module-03/exercises/batch-and-interactive-jobs/README.md)
- **Module:** [Module 2: Text Terminal Basics](../../README.md)
- **Course:** [Course Home](../../../README.md)
