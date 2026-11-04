# HPC Fundamentals: First Job on a Shared System

You will follow a research project from organizing a collaborator’s files to running, debugging, and choosing resources for jobs on a shared system.

<br>

## Learning outcomes

By the end of this course, you should be able to:

- Use basic terminal commands to navigate and organize files.
- Copy an inherited project into your own workspace.
- Recognize that shared systems have storage limits and quotas.
- Submit a simple batch job using Slurm.
- Use an interactive allocation to test a command.
- Read Slurm output files and distinguish application errors from scheduler messages.
- Recognize that resource requests should match what your code can use.

<br>

## Resources

- [Command Reference](docs/command-reference.md)
- [NERSC Documentation](https://docs.nersc.gov/)
- [Absolute Beginner's Guide](https://docs.nersc.gov/beginner-guide/)
- [Instructor guide](instructor/README.md)
- *[Canvas mapping and migration checklist](docs/canvas-map.md)*

<br>

## Course modules

| Canvas module | Materials |
|---|---|
| Module 1: NERSC Overview | [Overview](module-01-nersc-overview/README.md) |
| Module 2: Text Terminal Basics | [Terminal practice](module-02-text-terminal-basics/README.md) |
| Module 3: Running Jobs | [Batch, interactive, and debugging exercises](module-03-running-jobs/README.md) |
| Module 4: Using Resources Effectively | [Existing CPU scaling demonstration](module-04-using-resources-effectively/README.md) |

<b>

## Before the workshop

You should already be able to log in to the NERSC system before this session starts. Confirm that your account, multi-factor authentication (MFA), and SSH setup work. We will not spend much time troubleshooting access during the workshop. If you need help getting ready, start with the [Absolute Beginner's Guide](https://docs.nersc.gov/beginner-guide/).

<br>

## Log in and create a workspace

Open your terminal and log in using the SSH command supplied by your instructor. Run the following commands on the training system after logging in.

You will make your own workspace so you can organize files, edit scripts, and save job output as you work. Your instructor will confirm the training project directory and the location of the shared course files. The example below uses the original workshop's `ntrain1` directory; substitute the path your instructor provides if it differs.

### 1. Create your workspace

```bash
cd "$CFS/ntrain1"
pwd
```

Choose a unique directory name, such as your NERSC username. In the next commands, replace `your_username` with that name:

```bash
mkdir your_username
cd your_username
pwd
```

Check the path printed by `pwd`: you should be inside your own directory within the training project.

### 2. Copy the course files

Your instructor will tell you where the shared training files are located. Using the original workshop location as an example:

```bash
cp -R /global/cfs/cdirs/ntrain1/RO_HPC_Fundamentals HPC-Fundamentals
cd HPC-Fundamentals
ls
```

Make sure you are copying the version with the module folders shown below. The shared training copy will need to be updated for this repository layout.

If your instructor asks you to get the files from GitHub instead, run these commands **from your personal workspace**, in place of the copy commands above:

```bash
git clone https://github.com/lipigupta/HPC-Fundamentals.git
cd HPC-Fundamentals
ls
```

The GitHub commands retrieve the default branch. Until the module restructuring is merged, your instructor will need to provide the course branch or a prepared training copy containing these folders.

### 3. Check your starting point

You should see:

```text
README.md
docs/
environment/
instructor/
module-01-nersc-overview/
module-02-text-terminal-basics/
module-03-running-jobs/
module-04-using-resources-effectively/
```

This directory is the **repository root**. When an exercise says to start from the repository root, it means this `HPC-Fundamentals` directory. Use `pwd` to check where you are and `ls` to see what is available.

You now have your own copy of the course materials. Follow the module links above to begin. In Module 2, you will inspect the inherited messy project and organize its files. The Python examples are ready for the later job exercises; see the [environment notes](environment/README.md) for dependencies.

<br>

## Big idea

This course is not about memorizing every command. The goal is to practice a common HPC workflow:

> Access the system, understand your files, run your code, read the output, fix errors, and try again.

<br>

s<br>

## Sources and Disclosure
This course is based on: Software Carpentries [Intro to HPC](https://github.com/carpentries-incubator/hpc-intro/) and HPC Carpentries [HPC Intro to Shell](https://github.com/hpc-carpentry/hpc-shell/)

This course and the contents of this repository are under CC-BY 4.0 license.

AI was used to help in the creation of this course, to structure the lesson, create the scripts and exercises, refine the learning objectives, and prepare the README files.
