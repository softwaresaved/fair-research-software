---
title: Setup
---

## Setup

To go through the course material on your own or at a workshop, 
you will need the following software installed and working correctly on your system:

- Command line tool (such as **Bash**, **Zsh** or **Git Bash**)  
- Git version control system
- GitHub account
- Python 3 
- Visual Studio Code integrated development environment (IDE)

The installation instructions for all the above tools are below.

### Command Line Tool
You will need a command line tool (also referred to as a shell, a terminal or a console) 
in order to run Python scripts, various commands that interact with your filesystem and use Git.

- On Windows, it is **strongly** recommended to install **Git Bash** (which is included in
  [Git For Windows package](https://gitforwindows.org/) - see the [Git installation section](../index.html#git-version-control-tool) below). 
The use of Windows command line tool `cmd` is not suitable for the course. We also advise against using
  [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/) for this course as we do not
  provide instructions for troubleshooting any potential issues between WSL and Visual Studio Code (VS Code).
- On macOS and Linux, you will already have a command line tool available on your system. 
You can use a command line tool such as [**Bash**](https://www.gnu.org/software/bash/),
  or any other [command line tool that has similar syntax to Bash](https://en.wikipedia.org/wiki/Comparison_of_command_shells),
  since none of the content of this course is specific to Bash. Note that starting with macOS Catalina,
  Macs will use [Zsh (Z shell)](https://www.zsh.org/) as the default command line tool instead of Bash.

To test your command line tool, start it up and type:

```bash
$ date
```

If your command line program is working - it should return the current date and time similar to:

```output
Wed 21 Apr 2021 11:38:19 BST
```

### Git Version Control Tool
Git is a program that is run from your command line tool to provide version control for your work. 
Git is also used to interact with online code and project sharing platform GitHub.

- On Windows, it is recommended to use **Git Bash**, which comes included as part of the [Git For Windows package](https://gitforwindows.org/) 
and will install the Bash command line tool as well as Git.
- On macOS, Git is included as part of Apple's [Xcode tools](https://en.wikipedia.org/wiki/Xcode)
  and should be available from the command line as long as you have Xcode. If you do not have Xcode installed, you can download it from
  [Apple's App Store](https://apps.apple.com/us/app/xcode/id497799835?mt=12) or you can
  [install Git using alternative methods](https://git-scm.com/download/mac).
- On Linux, Git can be installed using your favourite package manager.

To test your Git installation, start your command line tool and type:

```bash
$ git help
```

If your Git installation is working you should see something like:

```output
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```

#### Git Configuration

When you use Git on a machine for the first time, you also need to configure a few additional things:

* your name,
* your email address (the one you used to open [your GitHub account](../index.html#github-account) with, which will be used to identify your commits),
* preferred text editor for Git to use (e.g. **Nano** or another text editor of your choice),
* whether you want to use these settings globally (i.e. for every Git project on your machine).

This can be done from a command line tool as follows:

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "name@example.com"
$ git config --global core.editor "nano -w"
```

### GitHub Account

GitHub is a free, online host for Git repositories that you will use during the course to store your work in so
you will need to open a free [GitHub](https://github.com/) account unless you do not already have one.

#### GitHub Configuration

In order to access GitHub using Git from your machine securely,
you need to set up a way of authenticating yourself with GitHub through Git.
The recommended way to do that for this course is to set up
[**SSH authentication**](https://www.ssh.com/academy/ssh/public-key-authentication) which requires a pair of keys -
one public that you upload to your GitHub account, and one private that remains on your machine.

GitHub provides full documentation and guides on how to:

- [generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), and
- [add an SSH key to a GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

A short summary of the commands you need to perform is shown below.

To generate an SSH key pair, you will need to run the `ssh-keygen` command from your command line tool 
and provide **your identity for the key pair** (e.g. the email address you used to register with GitHub)
via the `-C` parameter as shown below.

You will then be prompted to answer a few questions -
e.g. where to save the keys on your machine and a passphrase to use to protect your private key.
Pressing 'Enter' on these prompts will get `ssh-keygen` to use the default key location (within
`.ssh` folder in your home directory) and set the passphrase to empty.

```bash
$ ssh-keygen -t ed25519 -C "your-github-email@example.com"
```

```output
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/<YOUR_USERNAME>/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/<YOUR_USERNAME>/.ssh/id_ed25519
Your public key has been saved in /Users/<YOUR_USERNAME>/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:qjhN/iO42nnYmlpink2UTzaJpP8084yx6L2iQkVKdHk your-github-email@example.com
The key's randomart image is:
+--[ED25519 256]--+
|.. ..            |
| ..o A           |
|. o..            |
| .o.o .          |
| ..+ =  B        |
| .o = ..         |
|o..X *.          |
|++B=@.X          |
|+*XOoOo+         |
+----[SHA256]-----+
```

Next, you need to copy your public key (**not your private key - this is important!**) over to
your GitHub account. The `ssh-keygen` command above will let you know where your public key is saved 
(the file should have the extension ".pub"), and you can get its contents from a command line tool as follows:

```bash
$ cat /Users/<YOUR_USERNAME>/.ssh/id_ed25519.pub
```
```output
ssh-ed25519 AABAC3NzaC1lZDI1NTE5AAAAICWGVRsl/pZsxx85QHLwSgJWyfMB1L8RCkEvYNkP4mZC your-github-email@example.com
```

Copy the line of output that starts with "ssh-ed25519" and ends with your email address
(it may start with a different algorithm name based on which one you used to generate the key pair
and it may have gone over multiple lines if your command line window is not wide enough).

Finally, go to your [GitHub Settings -> SSH and GPG keys -> Add New](https://github.com/settings/ssh/new) page 
to add a new SSH public key. 
Give your key a memorable name (e.g. the name of the computer you are working on that contains the
private key counterpart), paste the public key
from your clipboard into the box labelled "Key" (making sure it does not contain any line breaks), 
then click the "Add SSH key" button.


### Python 3 Distribution

You will need Python 3 for this course (note that while Python 2 may work as well, it is not supported by this course). 
You may already have Python 3 installed on your system, in which case you do not have to do anything - 
you can check this using the commands below.

```bash
$ python3 --version # on macOS/Linux
$ python --version # on Windows — Windows installation comes with a python.exe file rather than a python3.exe file 
```

You should see something like the output below.

```output
Python 3.11.7
```

To download the latest Python distribution for your operating system,
please head to [Python.org](https://www.python.org/downloads/).
Then use the appropriate command above for your platform to test your installation.


If you are using Windows and invoking `python` command causes your Git Bash terminal to hang with no error message 
or output, you may need to create an alias for the python executable `python.exe` like so:

```bash
$ alias python="winpty python.exe"
```
This alias will be valid for the duration of the shell session. For a more permanent solution, from the shell do:

```bash
$ echo "alias python='winpty python.exe'" >> ~/.bashrc
```

## Visual Studio Code (VS Code)
We will use Microsoft [Visual Studio Code (VS Code)](https://code.visualstudio.com/) as an 
Integrated Development Environment (IDE) to type and execute Python code and run command line and Git commands 
(through its integrations with the tools we have installed separately so far).

Please make sure to [download VS Code](https://code.visualstudio.com/Download) for your platform.

### VS Code Configuration

After installing VS Code - we need to make sure that it knows about all the tools (command line, Git and Python) 
we have installed previously, so that we can use them all from within VS Code interface and not have to switch 
between them all the time.

#### Command Line Tool Integration

On macOS and Linux systems, VS Code will typically recognise a command line tool you have on your system 
and you will not need to do anything.

To check command line tool integration - select "Terminal -> New Terminal" from the top level menu. 
This should open a terminal window within VS Code and tell you which command line tool the terminal is using. 
If you want to change it - you may do that from the drop-down menu to the right of the window, 
and you can change the default command line tool from the same menu by using the option "Select Default Profile" (so 
it will use that one next time you open a terminal window).

![*VS Code terminal window*](episodes/fig/vscode-terminal.png){alt='Terminal window in VS Code with "Select Default Profile" option highlighted'}

#### Python Integration

#### Git Integration