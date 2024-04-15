---
title: Version control
teaching: 60
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions

- What is a version control system?
- How can a version control system help make my work reproducible?
- What does a standard version control workflow look like?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Create self-contained commits in Git to incrementally save work
- Inspect logs to review the history of work
- Push new work from a local machine to a remote server

::::::::::::::::::::::::::::::::::::::::::::::::

In this episode, we will begin to cover the basics of version control and explore
how this tool assists us in producing reproducible and sustainable scientific projects.
We will create a new project, make some changes to it and track them with
version control, and then push those changes to a remote server for safe-keeping.

### What is a version control system?

Version control is the practice of tracking and managing changes to files.
Version control systems are software tools that assist in the management of these
file changes over time. They keep track of every modification to the files in a
special database that allows users to "travel through time" and compare earlier
versions of the files with the current state.

### Motivation for using a version control system

The main motivation as scientists to use version control in our projects is for
reproducibility purposes. As hinted to above, by tracking and storing every change
we make, we can more effectively restore the state of the project at any point
in time. This is incredibly useful if we want to reproduce results from a
specific version of the code, or track down changes that broke some functionality.

The other benefit we gain is that version control provides us with provenance of
the project. As we make each change, we also leave a message about what the
change was and why it was made. This improves the transparency of the project and
makes it auditable, which is good scientific practice.

Later on in this workshop, we will also see how using a version control system
allows many people to collaborate on the same project without a lot of manual
effortto combine different items of work.

### Create a new repository

Create a new directory in the `Desktop` folder for our work, and then change the current working directory to the newly created one:

```bash
$ cd ~/Desktop
$ mkdir spacewalks
$ cd spacewalks
```

We tell Git to make `spacewalks` a repository -- a place where Git can store versions of our files:

```bash
git init
```

We can check everything is setup correctly by asking Git to tell us the status of our project:

```bash
$ git status
```

```output
On branch main
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

The exact wording of this output may be slightly different if you are using a different version of Git.

### Add initial files into our repository

During the [setup](./index.html#astronaut-data-and-analysis-code) for this course, you have been provided with a `.zip` archive with two files:

- `bad code.py`
- `Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv`

We need to move these files into our git folder.
You can either drag and drop the files from a file explorer window into the left pane of the VSCode IDE, or you can use the [`mv` command](https://linuxcommandlibrary.com/man/mv) in the terminal.

```bash
mv /path/where/you/saved/the/file/bad\ code.py ~/Desktop/spacewalks/
mv /path/where/you/saved/the/file/Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv ~/Desktop/spacewalks/
```

Let's see what that has done to our repository by running `git status` again:

```bash
git status
```

```output
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv
	bad code.py

nothing added to commit but untracked files present (use "git add" to track)
```

This is telling us that Git has noticed the new files.
The "untracked files" message means that there's a file in the directory that Git isn't keeping track of.
We can tell Git to track a file using `git add`:

```bash
$ git add bad\ code.py
$ git add Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv
```

and then check the right thing happened:

```bash
$ git status
```

```output
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv
	new file:   bad code.py
```

Git now knows that it's supposed to keep track of `bad code.py` and `Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv`, but it hasn't recorded these changes as a commit yet.
To get it to do that, we need to run one more command:

```bash
$ git commit -m "Add and example script and dataset to work on"
```

```output
[main (root-commit) a5fa618] Add and example script and dataset to work on
 2 files changed, 438 insertions(+)
 create mode 100644 Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv
 create mode 100644 bad code.py
```

When we run `git commit`, Git takes everything we have told it to save by using `git add` and stores a copy permanently in a special `.git` directory.
This permanent copy is called a commit (or revision).

We use the flag `-m` (for message) to record a short, descriptive, and specific comment that will help us remember later on what we did and why.
If we only run `git commit` without the `-m` option, Git will launch a text editor so that we can write a longer message.

Good commit messages start with a brief (<50 characters) statement about the changes made in the commit.
Generally, the message should complete the sentence "If applied, this commit will".
If you want to go into more detail, add a blank line between the summary line and your additional notes.
Use this additional space to explain why you made changes and/or what their impact will be.

If we run `git status` now, we see:

```bash
$ git status
```

```output
On branch main
nothing to commit, working tree clean
```

This tells us that everything is up to date.

:::::::::::::::::::::::::::::::::::::::::  callout

## Where are my changes?

If we run `ls` at this point, we will still see only two files, the script and the dataset.
That's because Git saves information about files' history in the special `.git` directory mentioned earlier so that our filesystem doesn't become cluttered (and so that we can't accidentally edit or delete an old version).

::::::::::::::::::::::::::::::::::::::::::::::::::

### Make a change

Did you notice how when we were typing the Python script into the terminal, we had to add a slash before the space like this: `bad\ script.py`?
Using a backslash in this way is called 'escaping' and it lets the terminal know to treat the space as part of the filename, and not a separate argument.
However, it is pretty annoying and considered bad practice to have spaces in your filenames like this, especially if you'll be manipulating them from the terminal.
So let's go ahead and remove the space from the filename altogether and replace it with a hyphen instead.
You can use the `mv` command again like so:

```bash
$ mv bad\ code.py bad-code.py
```

If you run `git status` again, you'll see Git has noticed the change in the filename.

```bash
$ git status
```

```output
On branch main
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    bad code.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	bad-code.py

no changes added to commit (use "git add" and/or "git commit -a")
```

:::::::::::::::::::::::::::::::::::::: challenge

### Add and commit the changed file

Using the Git commands demonstrated so far, save the change you just made to the Python script.

Remember, commit messages should be descriptive and complete the sentence "If applied, this commit will...".
You can also use `git status` to check the status of your project at any time.

:::::::::::::: solution

### Solution

To save the changes to the renamed Python file, use the following Git commands:

```bash
$ git add bad\ code.py bad-code.py
$ git status
```

```output
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    bad code.py -> bad-code.py
```

```bash
$ git commit -m "Replace space in Python filename with hyphen"
```

```output
[main ef3508f] Replace space in Python filename with hyphen
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename bad code.py => bad-code.py (100%)
```

### Advanced solution

We initially renamed the Python file using the `mv` command, and we than had to add *both* `bad-code.py` and `bad\ code.py`.
Alternatively, we could have used Git's own `mv` command like so:

```bash
$ git mv bad\ code.py bad-code.py
$ git status
```

```output
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    bad code.py -> bad-code.py
```

`git mv` is the equivalent of running `mv ...` followed immediately by `git add ...` of the old and new filenames, so the changes have been staged automatically.
All that needs to be done is to commit them.

```bash
$ git commit -m "Replace space in Python filename with hyphen"
```

```output
[main 20e7004] Replace space in Python filename with hyphen
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename bad code.py => bad-code.py (100%)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Commit messages

We have already met the concept of commit messages when we made and stored changes
to our code files. Commit messages are short descriptions of, and the motivation
for, what a commit will achieve. It's therefore important to take some time to
ensure these commit messages are helpful and descriptive, as when work is reviewed
(by your future self or a collaborator) they provide the context of what change
was made and why. This can make tracking down specific changes in commits much
easier, without having to inspect the code or files themselves.

Generally, commit messages should complete the sentence "If applied, this commit
will...". Most often a short, 50 character (ish) title will suffice, but a longer-form
description of the changes can also be provided by leaving a blank space between
the summary line and the rest of the message. There are many different conventions
that can be used for commit messages that range from very structured (such as
[conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)) to the
fun (such as [gitmoji](https://gitmoji.dev/)). The important thing is that it
is clear to the reader what a commit is doing and why. If a project is using a
specific commit message convention, this will often be described in their
[contributing guidelines](https://en.wikipedia.org/wiki/Contributing_guidelines).

:::::::::::::::::::::::::::::::::::::: challenge

### Good commit messages

Read the two commit messages below. In pairs or small groups, discuss which
messages help you understand more about what the commit author did. What about
the commit messages do you find helpful or not?

1. ```output
   [main 7cf85f6] Change variable
     1 file changed, 1 insertion(+), 1 deletion(-)
   ```
2. ```output
   [main 8baf69d] Change variable name from columns to column_headers
    1 file changed, 1 insertion(+), 1 deletion(-)
   ```

:::::::::::::: solution

### Solution

Commit message (2) is the better commit message since it is more descriptive about
what the author did. This message could be improved further by adding a blank line
then further describing the change discussing, for example, why the variable name
was changed.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Self-contained commits

If we want our commit messages to be descriptive and help us understand the
changes in the project over time, then we also have to make commits that are
very self-contained. That is to say that each commit we make should only change
one, logical thing. By "logical" here, we mean that one aspect of updating the
files has been achieved to completion - such as adding docstrings or refactoring
a function - we don't mean that changes are committed line-by-line. See the
["Things to avoid when creating commits" section][git-commit-avoid]
of [Openstack's "Git Commit Good Practice" documentation][git-commit-good-practice] for examples of logical,
self-contained commits, and commits that don't follow this practice.

The reasons that self-contained commits are important are that: it helps with
reviewing changes if each commit tackles one step; if code breaks, tracking down
the specific change that caused the break is simpler; if you need to undo changes,
you can remove them in small increments, rather than losing a lot of unrelated
work along with the change you do want to remove.

:::::::::::::::::::::::::::::::::::::: challenge

### Understanding commit contents

Below are the `diff`s of two commits. A `diff` shows the differences in a file
(or files!) compared to the previous commit in the history so you can what has
changed. The lines that begin with `+`s represent additions, and the lines that
begin with `-`s represent deletions. Compare these two commit `diff`s. Can you
understand what the commit author was trying to achieve in each commit? How many
changes have they tried to make in each commit? Discuss in pairs or small groups.

<!-- FIXME: Figure out if ```diff would show diff colours here.
Alternatively, add screenshots from GitHub UI -->
1. ```bash
    diff --git a/bad-code.py b/bad-code.py
    index e804094..ba6a0f9 100644
    --- a/bad-code.py
    +++ b/bad-code.py
    @@ -1,3 +1,7 @@
    +import json
    +import datetime as dt
    +import matplotlib.pyplot as myplot
    +
    #https://data.nasa.gov/Raw-Data/Extra-vehicular-Activity-EVA-US-and-Russia/9kcy-zwvn/about_data

    csvfile = open('Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv', 'r')
    @@ -13,7 +17,6 @@
            #print(thing)
            l[fieldnames[thing]] = line[thing]

    -    import json
        json.dump(l, jsonfile)
        jsonfile.write('\n')

    @@ -25,8 +28,6 @@
        data.append(json.loads(line))
    data.pop(0)

    -import datetime as dt
    -
    time = []
    date =[]

    @@ -49,7 +50,5 @@
    for i in time:
        t.append(t[-1]+i)

    -import matplotlib.pyplot as myplot
    -
    myplot.plot(date,t[1:])
    myplot.show()
   ```
2. ```bash
    diff --git a/bad-code.py b/bad-code.py
    index e804094..333ef14 100644
    --- a/bad-code.py
    +++ b/bad-code.py
    @@ -1,23 +1,25 @@
    +import json
    +import datetime as dt
    +import matplotlib.pyplot as myplot
    +
    #https://data.nasa.gov/Raw-Data/Extra-vehicular-Activity-EVA-US-and-Russia/9kcy-zwvn/about_data
    
    csvfile = open('Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv', 'r')
    -jsonfile= open('file.json', 'a')
    -fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")
    +jsonfile= open('file.json', 'w')
    +fieldnames = ("EVA #", "Country", "Crew", "Vehicle", "Date", "Duration", "Purpose")
    
    for count in range(370):
        line = csvfile.readline().split(',')
    
    -    #dict
    -    l = dict()
    -    for thing in range(len(line[:7])):
    -        #print(thing)
    -        l[fieldnames[thing]] = line[thing]
    -
    -    import json
    -    json.dump(l, jsonfile)
    +    # Create an empty dictionary to store cleaned data in
    +    data = dict()
    +    for i in range(7):
    +        data[fieldnames[i]] = line[i]
    +    json.dump(data, jsonfile)
        jsonfile.write('\n')
    
    jsonfile.close()
    +csvfile.close()
    
    data=[]
    
    @@ -25,8 +27,6 @@
        data.append(json.loads(line))
    data.pop(0)
    
    -import datetime as dt
    -
    time = []
    date =[]
    
    @@ -49,7 +49,5 @@
    for i in time:
        t.append(t[-1]+i)
    
    -import matplotlib.pyplot as myplot
    -
    myplot.plot(date,t[1:])
    myplot.show()
   ```

:::::::::::::: solution

### Solution

The git `diff` presented in option (1) is cleaner. The author has only tackled
one thing: placing the import statements at the top of the file. This kind of
commit is much easier to review in isolation, and will be easier to track down
if [`git bisect`](https://git-scm.com/docs/git-bisect) is required.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Git logs

If we want to know what we've done recently, we can ask Git to show us the project's history using `git log`:

```bash
$ git log
```

```output
commit 20e700455d340711537651ac4b798c18feba08b3
Author: Sarah Gibson <REDACTED>
Date:   Mon Mar 11 16:30:13 2024 +0000

    Replace space in Python filename with hyphen

commit a5fa618f9cc9699146ac738bb439b50da6b9917d
Author: Sarah Gibson <REDACTED>
Date:   Thu Feb 8 14:12:44 2024 +0000

    Add and example script and dataset to work on
```

This output demonstrates why it is important to write meaningful and descriptive
commit messages. Without the messages, we will only have the commit hashes (the
strings of random numbers and letters after "commit") to identify each commit,
which would be impossible for us.

We may need to inspect our recent commits to establish where a bug was introduced
or because we've decided that our recent work isn't suitable and we wish to discard
it and start again. Once we have identified the last commit we want to keep, we 
can revert the state of our project back to that commit with a few different
methods:

- [`git revert`](https://git-scm.com/docs/git-revert): This command reverts a
  commit by creating a new commit that reverses the action of the supplied commit
  or list of commits. Because this comand creates new commits, your git history
  is more complete and tells the story of exactly what work you did, i.e.,
  deciding to discard some work.
- [`git reset`](https://git-scm.com/docs/git-reset): This command will recover
  the state of the project at the specified commit. What is done with the commits
  you had made is defined by some optional flags:
  - `--soft`: Any changes you had made would be preserved and left as "Changes to be committed"
  - `--mixed`: Any changes you had made would be preserved but not marked for commit (this is the default action)
  - `--hard`: All changes you had made are discarded
  Using this command produces a "cleaner" history, but does not tell the full
  story and your work.

### Pushing to a Git server

One of the benefits of using a distributed version control system, such as Git,
is its distributed nature. So far we have have been working with a project on our
local machines and, even though we have been incrementally saving our work in a
way that is recoverable (version control), if anything happened to our laptops,
the whole project would be lost. However, we can use the distribution aspect of
Git to push our projects and histories to a server (someone else's computer) so
that they are accessible and retrievable if the worst were to happen to our
machines. Distributing our projects in this way also opens us up to collaboration
since colleagues would be able to access our projects, make their own copies on
their machines, and conduct their own work.

We will now go through how to push a local project to [GitHub](https://github.com),
though other Git hosting services are available, such as [GitLab](https://gitlab.com)
and [Bitbucket](https://bitbucket.org).

1. In your browser, navigate to <https://github.com> and sign into your account
2. In the top right hand corner of the screen, there is a menu labelled "+" with
   a dropdown. Click the dropdown and select "New repository" from the options.

   ![*Creating a new GitHub repository*](fig/ep03_fig01-create_new_repo.jpg){ alt-text="Selecting the 'New repository' option from GitHub's dropdown menu" .image-with-shadow }

3. You will be presented with some options to fill in or select while creating
   your repository. In the "Repository Name" field, type "spacewalks". This is
   the name of your project and matches the name of your local folder.

   ![*Naming the GitHub repository*](fig/ep03_fig02-repository_name.png){ alt-text="Setting the name of the repository on GitHub" .image-with-shadow }

   Ensure the visibility of the repository is "Public" and leave all other options
   blank. Since this repository will be connected to a local repository, it needs
   to be empty which is why we don't initialise with a README or add a license or
   `.gitignore` file. Click "Create repository" at the bottom of the page.

   ![*Complete GitHub repository creation*](fig/ep03_fig03-create_repository.jpg){ alt-text="Completing the creation of the GitHub repository" .image-with-shadow }

4. Now you have created your repository, you need to send the files and the history
   you have stored on your local computer to GitHub's servers. GitHub provides
   some instructions on how to do that for different scenarios. You want to use
   the instructions under the heading "...or push an existing repository from the
   command line". These instructions will look like this:

   ```bash
   git remote add origin https://github.com/<YOUR_GITHUB_HANDLE>/spacewalks.git
   git branch -M main
   git push -u origin main
   ```

   You can copy these commands using the button that looks like two overlapping
   squares to the right-hand side of the commands. Paste them into your terminal
   and run them.

   ![*Copy the commands to sync the local and remote repositories*](fig/ep03_fig04-copy_commands.jpg){ alt-text="Copying the commands to sync the local and remote repositories" .image-with-shadow }

5. If you refresh your browser window, you should now see the two files `bad-code.py`
   and `Extra-vehicular_Activity__EVA__-_US_and_Russia_20240126.csv` visible in
   the GitHub repository, matching what you have locally on your machine.

Let's explain a bit more about what those commands did...

```bash
git remote add origin https://github.com/<YOUR_GITHUB_HANDLE>/spacewalks.git
```

This command tells Git to create a `remote` called "origin" and link it to the
URL of your GitHub repository. A `remote` is a version control concept where two
(or more) repositories are connected to each other in such a way that they can
be kept in sync by exchanging commits. "origin" is a name used to refer to the
remote repository. It could be called anything, but "origin" is a convention that
is often used by default in Git and GitHub since it indicates which repository
is considered the "source of truth", particularly useful when many people are
collaborating on the same repository.

```bash
git branch -M main
```

`git branch` is a command used to manage branches. We'll discuss branches later
on in the workshop. This command ensures the branch we are working on is called
"main". This will be the default branch of the project for everyone working on it.

```bash
git push -u origin main
```

The `git push` command is used to update remote references with any changes you
have made locally. This command tells Git to update the "main" branch on the
"origin" remote. The `-u` flag (short for `--set-upstream`) will set a tracking
reference, so that in the future only `git push` can be run without the need to
specify the remote and reference name.

:::::::::::::::::::::::::::::::::::::: challenge

### Terminology

In pairs or small groups, discuss the difference between the terms `remote`
and `origin`. What is the definition of each term?

:::::::::::::: solution

### Solution

- `remote`: a version control concept where two (or more) repositories are linked
  together in such a way that they can be kept in sync by exchanging commits
- `origin`: a common Git/GitHub naming convention for the remote repository to
  designate the source of truth for collaborators

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Summary

During this episode, we have covered the basics of using version control to
track changes to our projects. We have seen how to: create new projects,
incrementally save progress, construct informative commit messages and content,
inspect the history of our projects and retrieve the state, and push our projects
to distributed servers.

These skills are critical to reproducible and sustainable science since using
version control makes our work self-documenting - the commit messages provide
the narrative of what changed and why - and we can recover the exact state of
our projects at a specific time, so we can more reliably run the "same" code
again. We can also back up our projects by pushing them to distributed, remote
servers and reduce the risk of data loss over the course of a project's lifetime.

Version control is a vast topic and we have only covered the absolute basics
here as a brief introduction. For a deeper and more complete dive into the
subject matter, please see the "Further reading" section below.

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- [Software Carpentry's Git Novice lesson][swc-git-lesson]
- [The Turing Way's "Guide to Version Control"][ttw-guide-version-control]
- ["How Git Works" course on Pluralsight][how-git-works]
- [How to Write a Good Commit Message][good-commit-message]
- [Git Commit Good Practice][git-commit-good-practice]

Also check the [full reference set](learners/reference.md#litref) for the course.

:::::::::::::::::::::::::::::::::::::::: keypoints

- A version control system is software that tracks and manages changes to a project over time
- Using version control aids reproducibility since the exact state of the software that produced an output can be recovered
- A commit represents the smallest unit of change to a project
- Commit messages describe what each commit contains and should be descriptive
- Logs can be used to overview the history of a project

::::::::::::::::::::::::::::::::::::::::::::::::::
