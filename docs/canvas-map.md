# Canvas mapping and migration checklist



| Canvas item | Repository destination |
|---|---|
| Module 1: NERSC Overview | [module-01/README.md](../module-01/README.md) |
| Module 1: Login practice | [module-01/exercises/log-in/README.md](../module-01/exercises/log-in/README.md) |
| Module 2: Let's Practice Terminal Commands | [module-02/exercises/organize-a-project/README.md](../module-02/exercises/organize-a-project/README.md) |
| Module 3: Interactive Jobs / Batch Jobs | [module-03/exercises/batch-and-interactive-jobs/README.md](../module-03/exercises/batch-and-interactive-jobs/README.md) |
| Module 3: Checking the Slurm Output File | [module-03/exercises/diagnose-and-fix/README.md](../module-03/exercises/diagnose-and-fix/README.md) |
| Module 3: Basic Parallelization → proposed Module 4 activity | [module-04/exercises/cpu-scaling/README.md](../module-04/exercises/cpu-scaling/README.md) |

## Before publishing Canvas changes

- Replace links and copied commands referring to `messy_project/`, `example/`, `slurm_scripts/`, or `solution/` with the new paths.
- Point terminal practice at `module-02/exercises/organize-a-project/messy_project` within the learner’s own course copy.
- Use stable main-branch links after the restructuring PR is merged; branch links are for review.
- Verify links in Student View and walk through every activity on the training system.

## Module 1 login practice quiz

Create a text-entry quiz question linked to the [login exercise](../module-01/exercises/log-in/README.md):

> Paste the hostname returned in your SSH session and the hostname returned in your JupyterLab terminal. Label each response.

Grade for completion: students should report both labeled hostnames after successfully logging in through each method. Do not require a fixed hostname or matching hostnames. No screenshot or file upload is needed.

## Follow-up content work

- Keep the single [Course Reference](course-reference.md) organized by module for use after Canvas access ends.
- Replace the Module 4 sleep demo with a real serial/parallel computation and timing activity, including a 16-CPU case.
- Review the capstone's current Canvas placement and prerequisites; no notebook has been added.
