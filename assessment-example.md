# Name of the Lesson: HPC Fundamentals

## Module-Level Obejective: Read Slurm output files and distinguish application errors from scheduler messages.

## Assessment Questions: 

Scenario: You submitted two different python scripts to run via batch scripts to the scheduler. One ran successfully (job ID: 10101) and the other did not (job ID: 10102). 

**1) Which of the following files should you check first to troubleshoot?**

a) submit.sh - the submission script

b) myapp.py - the application script

c) slurm-10101.out - the slurm log for the successful job

d) slurm-10102.out - the slurm log for the unsuccessful job

>Answer: d - it will likely explicitly tell you the error.

You use the bash command 'tail slurm-10102.out' to print the end of the log file. It shows:
```
srun: error: nid00456: task 0: Exited with exit code 1
srun: Terminating StepId=10102.0
```

**2) True or False: this is definitive proof that the error originated from the scheduler, slurm, and not the application.**

>Answer: false - an error from the application can trigger an "error" in slurm which will terminate the job, but the error originated in the application. 

You use the bash command `cat slurm-10102.out` to see the entire log contents. It shows: 

```
Job started on Tue Apr 23 11:02:44
Running on host: nid00456
Working directory: /global/homes/u/user/project

Loading modules...
Starting training job...
Loading synthetic training data...

Epoch 1: loss=0.8452
Epoch 2: loss=0.7011
Epoch 3: loss=0.5894
Epoch 4: loss=0.5123
Epoch 5: loss=0.4778

Training complete.

Traceback (most recent call last):
  File "myapp.py", line 26, in <module>
    print(result)
NameError: name 'result' is not defined

srun: error: nid00456: task 0: Exited with exit code 1
srun: Terminating StepId=10102.0
```

**3) Which line/s show the error and how to fix it?**

>Answer: line 55 begins the Traceback which is how Python displays error messages, and explicitly shows where in the application the error lies (which is usually a clue as to how to fix the issue.)

## Rubric

| Criterion                                                                   | Proficient                                                                                                                                                                                                       | Intermediate                                                                                                                                                      | Novice                                                                                                                                               | Not completed                                                                                                                        |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Identify the main way(s) to begin the troubleshooting process               | Instructs the flowchart user in 3 or more ways to assess the success of their job.                                                                                                                               | Instructs the flowchart user in only 2 ways to assess the success of their job.                                                                                   | Instructs the flowchart user in only 1 way to assess the success of their job.                                                                       | Instructs the flowchart user to assess the success of their job incorrectly, or fails to begin the troubleshooting process entirely. |
| Provide examples of common sources of error the flowchart user should check | Raises 2 common causes of job failures.                                                                                                                                                                          | Raises 1 common cause of job failures.                                                                                                                            | Raises no common causes of job failures.                                                                                                             | Raises incorrect causes of job failures ("the system is bad/faulty" ect.)                                                            |
| Provides examples of best practices to solve the error.                     | Includes detailed instructions for addressing common causes of failure for each identified cause, including specific commands or links to the NERSC documentation or other reputable source to aid in debugging. | Includes some instructions for addressing common causes of failure for each identified cause, with a general link to the NERSC documentation to aid in debugging. | Includes very general instructions for addressing common causes of failure for each identified cause, with ambiguous or generic ideas for debugging. | Does not provide any instructions for debugging or how to address common causes for job failure.                                     |





















