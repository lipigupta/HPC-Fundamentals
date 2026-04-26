# Instructor Guide: HPC Fundamentals Scaffold

This guide is for the instructor. The learner-facing guide is `README.md`.

## Core narrative

Learners are new interns/students who have inherited a messy project directory from a collaborator. They need to copy it into their own workspace, organize it enough to work safely, then prepare and run a Python workload through Slurm.

The course is intentionally workflow-first:

1. Access the system.
2. Prepare a workspace.
3. Inspect and organize inherited files.
4. Notice storage usage and quotas at a high level.
5. Submit a batch job.
6. Use an interactive allocation.
7. Diagnose a failed job by reading Slurm output.
8. Fix the application error.
9. See a small resource-scaling example.

## Suggested timing for a 3-hour session

| Segment | Time |
|---|---:|
| Welcome, goals, SSH check | 10 min |
| Copy scaffold and create workspace | 10 min |
| Terminal basics through messy project | 35 min |
| Quota/storage preview | 5 min |
| Batch job setup and submission | 20 min |
| Interactive allocation and `python` vs `srun` | 25 min |
| Read failed Slurm output | 25 min |
| Fix and resubmit | 20 min |
| CPU scaling teaser | 20 min |
| Wrap-up and bridge to New User Training | 10 min |

## Messy directory answer key

This is one possible solution. Do not present it as the only correct solution.

```text
messy_project/
├── data/
│   ├── data_final.txt
│   └── data_raw.txt
├── scripts/
│   └── script.sh
├── results/
│   ├── slurm-10101.out
│   └── slurm-10102.out
├── logs/
│   └── slurm-99887.out
├── notes/
│   ├── notes.txt
│   └── meeting_notes.txt
├── archive/
│   ├── backup_data_copy.txt
│   └── README_old.md
└── temp/
    └── scratch/
        └── old_runs/
```

Command sequence:

```bash
cd ~/hpc_fundamentals/messy_project
mkdir data scripts results logs notes archive
mv data_final_FINAL.txt data/data_final.txt
mv data1.txt data/data_raw.txt
mv script.sh scripts/
mv slurm-10101.out results/
mv slurm-10102.out results/
mv results_old/slurm-99887.out logs/
mv notes.txt notes/
mv random_notes/meeting_notes.txt notes/
mv README_old.md archive/
mv backup/data_copy.txt archive/backup_data_copy.txt
rmdir backup
rmdir random_notes
```

Keep this segment focused. The goal is terminal practice and workflow readiness, not a long discussion of file organization philosophy.

## Quota/storage preview

Keep this brief because New User Training covers storage in detail.

Suggested script:

> Because this is a shared system, storage is not unlimited. Limits on storage are called quotas. We will not go deep into quota policies today because that is covered in New User Training. For now, I just want you to know that file organization and cleanup matter on HPC systems.

Commands:

```bash
du -sh .
du -sh *
```

Add site-specific quota command if desired.

## Broken job teaching point

The intentional error is in `python_black_box/run_broken.py`:

```python
print(result)
```

It should be:

```python
print(results)
```

This is intentionally small. The point is not Python debugging. The point is reading output carefully.

Instructor point:

> The scheduler is reporting that the application exited with an error. The scheduler did not cause the Python NameError.

## `python` vs `srun python`

Simple explanation:

```text
python run.py        # runs Python directly where you are
srun python run.py   # asks Slurm to launch Python using allocated resources
```

Inside a simple single-task allocation, they may look similar. For parallel jobs or multi-resource jobs, `srun` is the mechanism Slurm uses to launch work across allocated resources.

## CPU scaling demo

`python_black_box/scale_demo.py` reads `SLURM_CPUS_PER_TASK` and uses that many Python worker processes.

Expected approximate runtimes:

| CPUs | Expected runtime |
|---:|---:|
| 1 | ~32 sec |
| 8 | ~4 sec |
| 32 | ~1 sec |

Teaching point:

> More resources help only when the application can use them.

## NERSC-specific adjustments to make before teaching

Review all Slurm scripts and add the correct site-specific directives. Possible examples include:

```bash
#SBATCH --account=<your_project>
#SBATCH --qos=<training_or_debug_qos>
#SBATCH --constraint=cpu
```

If using a reservation, add the reservation directive provided by NERSC.
