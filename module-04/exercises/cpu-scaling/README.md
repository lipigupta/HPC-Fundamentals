# CPU scaling demonstration

Start from the repository root on the training system:

```bash
cd module-04/exercises/cpu-scaling
```

Review each Slurm script and set the instructor-provided account, QOS, constraint, and reservation directives. Submit from this exercise directory:

```bash
sbatch 04_scale_1_cpu.slurm
sbatch 05_scale_8_cpu.slurm
sbatch 06_scale_32_cpu.slurm
```

After completion, compare runtimes:

```bash
grep Runtime slurm-scale-*.out
```

Record requested CPUs and runtime for each run. Explain how `workload.py` uses `SLURM_CPUS_PER_TASK` to choose its worker count, and why requesting CPUs alone cannot parallelize arbitrary code.

This existing demonstration runs 32 independent one-second sleeps using a process pool. Approximate durations are 32, 4, and 1 seconds plus overhead. It illustrates concurrent execution, not a benchmark of CPU computation. Timing varies.

## Navigation

- **Previous:** [Diagnose and fix](../../../module-03/exercises/diagnose-and-fix/README.md)
- **Module:** [Module 4: Using Resources Effectively](../../README.md)
- **Course:** [Course Home](../../../README.md)
