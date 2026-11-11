# Log in to NERSC

Practice accessing NERSC through SSH and Jupyter before working with files in Module 2. You will check your username and record the hostname from each session.

You need an active NERSC account and working multi-factor authentication (MFA). If either login fails, ask your instructor for help before continuing.

<br>

## 1. Log in using SSH

Open a terminal on your computer. Follow your instructor's SSH instructions and the [NERSC terminal login guide](https://docs.nersc.gov/beginner-guide/#lock-and-key-log-in-using-a-terminal) to connect and complete MFA. Follow the guide's host fingerprint verification instructions if this is your first connection.

Once connected, run these commands in your remote terminal:

```bash
whoami
hostname
```

- `whoami` prints your username. Check that it matches your NERSC account.
- `hostname` prints the name of the machine running your shell.

Copy the hostname into your notes and label it **SSH**. Then disconnect:

```bash
exit
```

You should now be back in your computer's local terminal.

<br>

## 2. Log in using Jupyter

Open [NERSC Jupyter](https://jupyter.nersc.gov/) in your browser. Follow the [NERSC Jupyter login guide](https://docs.nersc.gov/beginner-guide/#keypad-entry-log-in-using-jupyter) to sign in and complete MFA.

For this access check, start the **Login Node** option for Perlmutter, unless your instructor directs you otherwise. Once JupyterLab opens, open a **Terminal** from the launcher.

Run the same commands in the JupyterLab terminal:

```bash
whoami
hostname
```

Check your username, then copy the hostname into your notes and label it **Jupyter**.

The hostname may differ between SSH and Jupyter, or between sessions. Record the values you actually see; they do not need to match.

<br>

## 3. Submit your access check in Canvas

Complete the Module 1 login practice quiz in Canvas:

> Paste the hostname returned in your SSH session and the hostname returned in your JupyterLab terminal. Label each response.

Use this format, replacing the placeholders with your results:

```text
SSH: <hostname from your SSH session>
Jupyter: <hostname from your JupyterLab terminal>
```

You are finished when you have successfully used both login methods and submitted both hostnames. No screenshot or file upload is needed.

<br>

<br>

## Navigation

- **Next module:** [Module 2: Text Terminal Basics](../../../module-02/README.md)
- **Module 1:** [Module 1: NERSC Overview](../../README.md)
- **Course:** [Course Home](../../../README.md)
