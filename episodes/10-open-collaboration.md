---
title: Open code & collaboration
teaching: 60
exercises: 30
---

::::::::::::::::::::::::::::::::::::: objectives
After completing this episode, participants should be able to:

- Understand how to archive code to Zenodo and create a digital object identifier (DOI) for a software project (and include that info in CITATION.cff).
- Understand how to track issues with code in GitHub.
- Understand how to use Git branches for working on code in parallel and how to merge code back using pull requests.
- Apply issue tracking, branching and pull requests together to fix bugs while allowing other developers to work on the same code.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: questions 

- How do I ensure my code is citable?
- How do we track issues with code in GitHub?
- How can we ensure that multiple developers can work on the same files simultaneously?

::::::::::::::::::::::::::::::::::::::::::::::::

Sharing code openly promotes collaboration, transparency, and innovation by allowing others to review, use, and 
improve the code. 
It fosters knowledge exchange, accelerates scientific progress, and enhances the reproducibility of research. 
Additionally, open sharing encourages community contributions and can lead to better-maintained, 
more reliable software.

Adding a [license](../learners/licensing.md) and other metadata to our code (covered in the previous episode) are the first steps towards 
sharing the code publicly.
There are several other important steps to consider which we will cover here.

::: callout

### Activate your virtual environment
If it is not already active, make sure to activate your virtual environment from the root of
the software project directory:

```bash
$ source venv_spacewalks/bin/activate # Mac or Linux
$ source venv_spacewalks/Scripts/activate # Windows
(venv_spacewalks) $
```
:::

::: instructor
At this point, the code in your local software project's directory should be as in:
https://github.com/carpentries-incubator/astronaut-data-analysis-not-so-fair/tree/10-open-collaboration
:::

## Sharing code to encourage collaboration

### Making the code public

By default repositories created on GitHub are private and only their creator can see them. 
Since we added an open source license to our repository we probably want to make sure people can actually 
access it. 

To make your repository public, if it is not already, go to your repository on GitHub and click on 
the `Settings` link near the top right corner. 
Then scroll down to the bottom of the page and the "Danger Zone" settings. Click on "Change Visibility" and you 
should see a message saying "Change to public".
If it says "Change to private" then the repository is already public. 
You will then be asked to confirm that you indeed want to make the repository public and agree 
to the warning that the code will now be publicly visible. 
As a security measure, you will then have to put in your GitHub password.

### Transferring to an organisation

Currently our repository is under the GitHub "namespace" of our individual user. 
This is OK for individual projects where we are the sole or at least the main code author,
but for bigger and more complex projects it is common to use a GitHub organisation named after our project. 
If we are a member of an organisation and have the appropriate
permissions then we can transfer a repository from our personal namespace to the organisation's. 
This can be done with another option in the "Danger Zone" settings, the
"Transfer ownership" button. 
Pressing this will then prompt us as to which organisation we want to transfer the repository to. 

### Archiving code to Zenodo and obtaining a DOI

[Zenodo][zenodo] is a data archive run by CERN. 
Anybody can upload datasets up to 50GB to it and receive a Digital Object Identifier (DOI). 
Zenodo's definition of a dataset is quite broad and can include code - which gives us a way to obtain a DOI for our 
software. 

Let us now look into how we can archive a GitHub repository to Zenodo. 
Note that, instead of using the real Zenodo website, we will practice with [Zenodo Sandbox](https://sandbox.zenodo.org/).

::: callout

### Zenodo Sandbox
[Zenodo Sandbox](https://sandbox.zenodo.org/) is a testing environment for Zenodo, a repository for research outputs, 
allowing users to safely experiment with its features without affecting the live system.
It is a clone of Zenodo, created for testing purposes, that works exactly the same way as Zenodo you can use it 
for learning, training, experimenting, and preparing uploads without impacting the primary Zenodo repository until
you are ready to publish and release your code (ot other research outputs) officially.
It will also not create real DOIs for a number of test repositories we use for this course and saturate the DOI space
(remember that a DOI, once created, is meant to exist forever).
:::

We can archive our GitHub repository to Zenodo (Sandbox) by doing the following:

 1. Go to the [Zenodo Sandbox login page](https://sandbox.zenodo.org/login) and choose to login with GitHub.
 2. Authorise Zenodo Sandbox to connect to GitHub. 
 3. Go to the [GitHub page](https://sandbox.zenodo.org/account/settings/github/) in your Zenodo Sandbox account. 
This can be found in the pull down menu with your user name in the top right corner of the screen.
 4. You will now have a list of all of your GitHub repositories. Next to each will be an "On" button. 
If you have created a new repository you might need to press the "Sync" button to update the list of repositories 
Zenodo Sandbox knows about.
 5. Press the "On" button for the repository you want to archive. If this was successful you will be told to refresh the page.
 6. The repository should now appear in the list of "Enabled" repositories at the top of the screen, but
it does not yet have a DOI. To get one we have to make a "release" on GitHub. Click on the repository and 
then press the green button to create a release. 
This will take you to GitHub's release page where you will be asked to give a title and description of the release. 
You will also have to create a "tag" for your release - a way of having a friendly name for the version of some code in 
Git instead of using a long hash code. 
Often we will create a sequential version number for each release of the software and have the tag name match this, 
for example v1.0 or just 1.0.
 7. If we now refresh the Zenodo Sandbox page for this repository we will see that it has been assigned a DOI.

The DOI does not just link to GitHub, Zenodo will have taken a copy (a snapshot) of our repository at the point 
where we tagged the release. 
This means that even if we delete it from GitHub or even if GitHub were ever to go away or remove it, 
there will still be a copy on Zenodo. 
Zenodo will allow people to download the entire repository (more accurately, its state at the time it was tagged for release) as a single `zip` file. 

Zenodo will have actually created two DOIs for you. One represents the latest version of the software and 
will always represent the latest if you make more releases. 
The other is specific to the release you made and will always point to that version. 
We can see both of these by clicking on the DOI link in the Zenodo page for the repository.

One of the things which is displayed on this page is a badge image that you can copy the link for and add to the 
README file in your GitHub repository so that people can find the Zenodo version of the repository. 
If you click on the DOI image in the Details section of the Zenodo page then you will be shown instructions for 
obtaining a link to the DOI badge in various formats including Markdown.
Here is the badge for this repository and the corresponding Markdown: 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11869450.svg)](https://doi.org/10.5281/zenodo.11869450)

```text
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11869450.svg)](https://doi.org/10.5281/zenodo.11869450)
```

:::  challenge

### Archive your repository to Zenodo (Sandbox)

Note: for this exercise, as demonstrated earlier, you should use the [Sandbox Zenodo](https://sandbox.zenodo.org/) (a version of 
Zenodo for testing and playing with before minting a real DOI).
For real software releases, you should use Zenodo.

 * Create an account on Zenodo Sandbox that is linked to your GitHub account.
 * Use Zenodo Sandbox to create a release for your repository and obtain a DOI for it.
 * Get the link to the DOI badge for your repository and add a link to this image to your README file in 
Markdown format. Check that this is the DOI for the latest version and not the DOI for a specific version, 
if not you will be updating this every time you make a release.

:::::::::::::::::::::::::::::::::::::::::::::::


::: callout

## Problems with GitHub and Zenodo integration

The integration between GitHub and Zenodo does not interact well with some browser privacy features and extensions. 
Firefox can be particularly problematic with this and 
might open new tabs to login to GitHub and then give an error saying: `Your browser did something unexpected. 
Please try again. If the error continues, try disabling all browser extensions.`
If this happens try disabling the extra privacy features/extensions or using another browser such as Chrome.

:::

### Adding a DOI and ORCID to the citation file

Now that we have our DOI it is good practice to include this information
in our citation file. 
Earlier we created a `CITATION.cff` file with information about how to cite our code.
There are a few fields we can add now which are related to the DOI; one of these is the `version` file which covers 
the version number of the software.
We can add a DOI to the file in the `identifiers` section with a type of `doi` and `value` of the Zenodo URL.
Optionally we can also add a `date-released` field indicating the date we released this software.
Here is an updated version of our `CITATION.cff` from the previous episode with a version number, DOI and release date added.

```yaml
# This CITATION.cff file was generated with cffinit.
# Visit https://bit.ly/cffinit to generate yours today!

cff-version: 1.2.0
title: Spacewalks
message: >-
  If you use this software, please cite it using the
  metadata from this file.
type: software
authors:
  - given-names: Jaffa
    name-particle: Sarah
  - given-names: Aleksandra
    family-names: Nenadic
  - given-names: Kamilla
    family-names: Kopec-Harding
repository-code: >-
  https://github.com/YOUR-REPOSITORY-URL/spacewalks.git
abstract: >-
  A Python script to analyse NASA extravehicular activity
  data
keywords:
  - NASA
  - Extravehicular activity
version: 1.0.1
identifiers:
  - type: doi
    value: 10.5281/zenodo.1234
date-released: 2024-06-01
```

:::  challenge

### Add a DOI to your citation file

Add the DOI you were allocated in the previous exercise to your `CITATION.cff` file and then commit and 
push the updated version to your GitHub repository. 
If you used the `commit` field in your `CITATION.cff` file before to point to a given version of the code - you can 
now remove it as using the DOI field is better for this job.

:::::::::::::::::::::::::::::::::::::::::::::::


::: callout

### Going further with publishing code

We now have our code published online, licensed as open source, archived with Zenodo, accessible via a DOI and with a citation file to encourage people to cite it. 
What else might we want to do in order to improve how findable, accessible or reusable it is?
One further step we could take is to publish the code with a peer reviewed journal. Some traditional journals will accept software submissions, although these are usually
as a supplementary material for a paper. There also journals which specialise in research software such as the [Journal of Open Research Software](https://openresearchsoftware.metajnl.com/),
[The Jornal of Open Source Software](https://joss.theoj.org/) or [SoftwareX](https://www.sciencedirect.com/journal/softwarex). With these venues, the submission will be the software
itself and not a paper, although a short abstract or description of the software is often required.
:::


## Working with collaborators

The strength of online collaboration platforms such as GitHub does not just lie in the ability to share code. 
They also allow us to track problems with that code, 
for multiple developers to work on it independently and bring their changes together and to review those 
changes before they are accepted.

### Tracking issues with code

A key feature of GitHub (as opposed to Git itself) is the issue tracker. 
This provides us with a place to keep track of any problems or bugs in the code and to discuss them
with other developers. 
Sometimes advanced users will also use issue trackers of public projects to report problems they are having 
(and sometimes this is misused by users seeking help using documented features of the program). 

The code from the testing chapter earlier has a bug with an extra bracket in eva_data_analysis.py (and if you have fixed that a missing import of summarise_categorical in the test).
Let's go ahead and create a new issue in our GitHub repository to describe this problem. 
We can find the issue tracker on the "Issues" tab in the top left of the GitHub 
page for the repository. 
Click on this and then click on the green "New Issue" button on the right hand side of the screen. 
We can then enter a title and description of our issue.

A good issue description should include:

 - What the problem is, including any error messages that are displayed.
 - What version of the software it occurred with.
 - Any relevant information about the system running it, for example the operating system being used.
 - Versions of any dependent libraries.
 - How to reproduce it.

After the issue is created it will be assigned a sequential ID number.

:::  challenge

### Write an issue to describe our bug

Create a new issue in your repository's issue tracker by doing the following:

 - Go to the GitHub webpage for your code
 - Click on the Issues tab
 - Click on the "New issue" button
 - Enter a title and description for the issue
 - Click the "Submit Issue" button to create the issue.
:::

### Discussing an issue

Once the issue is created, further discussion can take place with additional comments. 
These can include code snippets and file attachments such as screenshots or logfiles.
We can also reference other issues by writing a # symbol and the number of the other issue. 
This is sometimes used to identify related issues or if an issue is a duplicate.

### Closing an issue

Once an issue is solved then it can be closed. 
This can be done either by pressing the "Close" button in the GitHub web interface or by making a commit which includes the word
"fixes", "fixed", "close", "closed" or "closes" followed by a # symbol and the issue number.

### Working in parallel with Git branches

Branching is a feature of Git that allows two or more parallel streams of work. 
Commits can be made to one branch without interfering with
another. 
Branches are commonly used as a way for one developer to work on a new feature or a bug fix while other developers 
work on other features.
When those new features or bug fixes are complete, the branch will be merged back with the `main` (sometimes called the
`master`) branch.

#### Creating a new branch

New Git branches are created with the `git branch` command. This should be followed by the name of 
the branch to create. 
It is common practice when the bug we are fixing has a corresponding issue to name the branch after the issue number and name. 
For example, we might call the branch `01-extra-bracket-bug` instead of something less descriptive like `bugfix`. 

For example, the command:

```bash
(venv_spacewalks) $ git branch 01-extra-bracket-bug
```

will create a new branch called `01-extra-bracket-bug`. 
We can view the names of all the branches by running `git branch` with no parameters.
By default there should be one branch called `main` (formerly `master`) and our new `01-extra-bracket-bug` branch.
The command will put `*` next to the currently active branch.

```bash
(venv_spacewalks) $ git branch
```

```output
  01-extra-bracket-bug
* main
```

We can see that creating a new branch has not activated that branch. To switch branches we can either
use the `git switch` or `git checkout` command followed by the branch name. For example:

```bash
(venv_spacewalks) $ git switch 01-extra-bracket-bug
```

To create a branch and change to it in a single command we can use `git switch` with the `-c` option 
(or `git checkout` with the `-b` option). 
Note that `git switch` command is only available in more recent versions of Git.

```bash
(venv_spacewalks) $ git switch -c 02-another-bug
```

#### Committing to a branch

Once we have switched to a branch any further commits that are made will go to that branch. 
When we run a `git commit` command we will see the name of the
branch we are committing to in the output of `git commit`. 
Let's edit our code and fix the lack of default values bug that we entered into the issue tracker earlier on.

Change your code from:

```python
<call to pandas without checks identified in testing section>
```

to:

```python
<call to pandas with checks identified in testing section>
```

and now commit it.

```bash
(venv_spacewalks) $ git commit -m "fixed bug" eva_data_analysis.py
```

In the output of `git commit -m` the first part of the output line will show the name of the branch we just made the commit to.

```output
[01-extra-brakcet-bug 330a2b1] fixes missing values bug, closes #01 
```

If we now switch back to the `main` branch our new commit will no longer be there in the source file or the output of `git log`.

```bash
(venv_spacewalks) $ git switch main
```

And if we go back to the `01-extra-bracket-bug` branch it will re-appear.

```bash
(venv_spacewalks) $ git switch 01-extra-bracket-bug
```

If we want to push our changes to a remote such as GitHub we have to tell the `git push` command which branch to push to. If the branch doesn't exist on the remote (as it currently won't)
then it will be created. 

```bash
(venv_spacewalks) $ git push origin 01-extra-bracket-bug
```

If we now refresh the GitHub webpage for this repository we should see the bugfix branch has appeared in the list of branches.

If we needed to pull changes from a branch on a remote 
(for example if we have made changes on another computer or via GitHub's web based editor), 
then we can specify a branch on a `git pull` command.

```bash
git pull origin 01-extra-bracket-bug
```

### Merging branches

When we have completed working on a branch (for example fixing a bug) then we can merge our branch back
into the main one (or any other branch). 
This is done with the `git merge` command.

This must be run on the *TARGET* branch of the merge, so we will have to use a `git switch` command to set this. 

```bash
(venv_spacewalks) $ git switch main
```

Now we are back on the main branch we can go ahead and merge the changes from the bugfix branch:

```bash
(venv_spacewalks) $ git merge 01-extra-bracket-bug
```

### Pull requests

On larger projects we might need to have a code review process before changes are merged, especially before they are 
merged onto the main branch that might be what is being released as the public version of the software. 
GitHub has a process for this that is called a **pull request**. Other Git services such as GitLab have different names 
for this; GitLab calls them **merge requests**.
Pull requests are situations where one developer requests that another merges code from a branch 
(or "pull" it from another copy of the repository). 
The person receiving the request then has the chance to review the code, write comments suggesting changes or 
even change the code themselves before merging it. 
It is also very common for automated checks of code to be run on a pull
request to ensure the code is of good quality and is passing automated tests.

As a simple example of a pull request, we can now create a pull request for the changes we made on our 
`01-extra-bracket-bug` branch and pushed to GitHub earlier on. 
The GitHub webpage for our repository
will now be saying something like "bugfix had recent pushes `n` minutes ago - Compare & Pull request". 
Click on this button and create a new pull request. 

Give the pull request a title and write a brief description of it, then click the green "Create pull request" button. 
GitHub will then check if we can merge this pull request without
any problems. 
We will look at what to do when this is not possible later on. 

There should be a green "Merge pull request" button, but if we click on the down arrow inside this button there are three options on how to handle this request:

1. Create a merge commit
2. Squash and merge
3. Rebase and merge

The default is option 1, which will keep all of the commits made on our branch intact. This can be useful for seeing the whole history of our work, but if we've done a lot of minor
edits or attempts at fixing a problem to fix one bug it can be excessive to have all of this history saved. This is where the second option comes in, this will place all of our changes from the branch into just 
a single commit, this might be much more obvious to other developers who will now see our bugfix as a single commit in the history. The third option merges the branch histories together
in a different way that doesn't make merges as obvious, this can make the history easier to read but effectively rewrites the commit history and will change the commit hash IDs. Some
projects that you contribute to might have their own rules about what kind of merge they will prefer. For the purposes of this exercise we'll stick with the default merge commit. 

Go ahead and click on "Merge pull request", then "Confirm merge". The changes will now be merged together. 
GitHub gives us the option to delete the branch we were working on, since
its history is preserved in the main branch there is no reason to keep it.

#### Using forks instead of branches

A fork is similar to a branch, but instead of it being part of the same repository it is a entirely new copy of the repository. 
Forks are commonly used by Github users who wish to work
on a project that they are not a member of. 
Typically forking will copy the repository to our own namespace (e.g. github.com/username/reponame instead of github.com/projectname/reponame)

To create a fork on github use the "Fork" button to the right of the repository name. 
After we create our fork we can make some changes and these could even be on the main branch 
inside our forked repository. 
GitHub will track that a fork has been made displays a "Contribute" button to create a pull request back to the original repository. Using this we can
request that the changes on our fork are incorporated by the upstream project.


:::  challenge

### Practice pull requests

Q: Work in pairs for this exercise. Share the GitHub link of your repository with your partner. 
If you have set your repository to private, you will need to add them as a collaborator. Go to the settings page on your GitHub repository's webpage, click on Collaborators from 
the left hand menu and then click the green "Add People" button and enter the GitHub username or email address of your partner. 
They will get an email and an alert within GitHub to accept your invitation to work on this repository, without doing this they won't be able to access it.

 - Now make a fork of your partners repository. 
 - Edit the `CITATION.cff` file and add your name to it.
 - Commit these changes to your fork
 - Create a pull request back to the original repository
 - Your partner will now receive your pull request and can review 
:::

 
Do not forget to commit any uncommitted changes you may have and then push your work to GitHub.

```bash
(venv_spacewalks) $ git add <your_changed_files>
(venv_spacewalks) $ git commit -m "Your commit message"
(venv_spacewalks) $ git push origin main
```

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- Licencing and citation episodes from the [Software Carpentry's Git Novice lesson][swc-git-lesson]
- Carpentries GitHub Skill ups for [instructors][git-skillup-instructors] and [maintainers][git-skillup-maintainers]
- [RSG Southampton Git lesson][git-soton] - [collaboration section][git-soton-collaboration]
- [Open source definition][osd-definition], by the [Open Source Initiative][osd]
- [What is free software?][free-software]

Also check the [full reference set](learners/reference.md#litref) for the course.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Zenodo can be used to archive a GitHub repository and obtain a DOI for it.
- We include a CITATION file with our code to tell people how to cite it.
- GitHub can help us track bugs or issues with software.
- Git branches can be used to allow multiple developers to work on the same part of code in parallel.
- The `git branch` command shows the list of branches and can create new branches.
- The `git switch` command changes which branch we are working on.
- The `git merge` command merges another branch into the current one.
- Pull requests allow developers to work on their own branch/fork and then request other developers review 
their changes before they are merged.

::::::::::::::::::::::::::::::::::::::::::::::::::

