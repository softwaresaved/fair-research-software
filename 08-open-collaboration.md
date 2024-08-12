---
title: Open project collaboration & management
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

# Sharing your code to encourage collaboration

In addition to adding a license and other metadata to our code (covered in previous episode) 
there are several other important steps to consider before sharing the code publicly.

### Making the code public

By default repositories created on Github are private and only their creator can see them. 
If we're going to be adding an open source license to our repository we probably want to make sure people can actually 
access it too! 

Go to the Github webpage of your repository (`https://github.com/<yourusername>/<yourrepsoitoryname>`) and click on 
the Settings link near the top right corner. 
Then scroll down to the bottom of the page and the "Danger Zone" settings. Click on "Change Visibility" and you 
should see a message saying "Change to public",
if it says "Change to private" then the repository is already public. You'll then be asked to confirm that you want 
to make the repository public and agree 
to the warning that the code will now be publicly visible. As a security measure you'll then have to put in your 
Github password.

### Transferring to an organisation

Currently our repository is under the Github "namespace" of our individual user. This is ok for individual projects 
where we are the sole or at least main author,
but for bigger and more complex projects it is common to use a Github organisation named after our project. 
If we are a member of an organisation and have the appropriate
permissions then we can transfer a repository from our personal namespace to the organisation's. 
This can be done with another option in the "Danger Zone" settings, the
"Transfer ownership" button. Pressing this will then prompt us as to which organisation we want to transfer 
the repository to. 

### Archiving to Zenodo and obtaining a DOI

Zenodo is a data archive run by CERN. Anybody can upload datasets up to 50GB to it and receive a 
Digital Object Identifier (DOI). 
Zenodo's definition of a dataset is quite broad and can include code. 
This gives us a way to obtain a DOI for our code. We can archive our Github repository to Zenodo by doing the following:

 1. Go to the [Zenodo Login page](https://zenodo.org/login) and choose to login with Github.
 2. Authorise Zenodo to connect to Github. 
 3. Go to the [Github page](https://zenodo.org/account/settings/github/) in your Zenodo account. 
This can be found in the pull down menu with your user name in the top right corner of the screen.
 4. You'll now have a list of all of your Github repositories. Next to each will be an "On" button. 
If you have created a new repository you might need to press the "Sync" button to update the list of repositories 
Zenodo knows about.
 5. Press the "On" button for the repository you want to archive. If this was successful you'll be told to refresh the page.
 6. The repository should now appear in the list of Enabled repositories at the top of the screen.
But it doesn't yet have a DOI. To get one we have to make a release on Github. Click on the repository and 
then press the green button to create a release. 
This will take you to Github's release page where you'll be asked to give a title and description of the release. 
You will also have to create a tag, this is a way of having a friendly name for the version of some code in 
Git instead of using a long hash code. 
Often we'll create a sequential version number for each release of the software and have the tag name match this, 
for example v1.0 or just 1.0.
 7. If we now refresh the Zenodo page for this repository we will see that it has been assigned a DOI.

The DOI doesn't just link to Github, Zenodo will have taken a copy of our repository at the point 
where we tagged the release. 
This means that even if we delete it from Github or even if Github were ever to go away or remove it, 
they'll still be a copy on Zenodo. 
Zenodo will allow people to download the entire repository as a single Zip file. 

Zenodo will have actually created two DOIs for you. One represents the latest version of the software and 
will always represent the latest if you make more releases. 
The other is specfic to the release you made and will always point to that version. 
We can see both of these by clicking on the DOI link in the Zenodo page for the repository.
One of the things which is displayed on this page is a badge image that you can copy the link for and add to the 
README file in your Git repository so that people can find
the Zenodo version of the repository. 
If you click on the DOI image in the Details section of the Zenodo page then you will be shown instructions for 
obtaining a link to the DOI badge in various formats including Markdown.
Here is the badge for this repository and the corresponding Markdown: 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11869450.svg)](https://doi.org/10.5281/zenodo.11869450)

```text
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11869450.svg)](https://doi.org/10.5281/zenodo.11869450)
```

:::  challenge

### Archive your repository to Zenodo

 * Create an account on Zenodo that is linked to your Github account.
 * Use Zenodo to create a release for your repository and obtain a DOI for it.
 * Get the link to the DOI badge for your repository and add a link to this image to your README file in 
Markdown format. Check that this is the DOI for the latest version and not the DOI for a specific version, 
if not you'll be updating this every time you make a release.

:::::::::::::::::::::::::::::::::::::::::::::::


::: callout

## Problems with Github and Zenodo integration

The integration between Github and Zenodo does not interact well with some browser privacy features and extensions. 
Firefox can be particularly problematic with this and 
might open new tabs to login to Github and then give an error saying: `Your browser did something unexpected. 
Please try again. If the error continues, try disabling all browser extensions.`
If this happens try disabling the extra privacy features/extensions or using another browser such as Chrome.

:::

### Adding a DOI and ORCID to the citation file

Now that we have our DOI it is good practice to include this information
in our citation file. In the previous part of this lesson we created a `CITATION.cff` file with information about how to cite our code.
There are a few fields we can add which are related to the DOI, one of these is the `version` file which covers the version number of the software.
We can add a DOI to the file in the `identifiers` section with a type of `doi` and `value` with the URL.
Optionally we can also add a `date-released` field indicating the date we released this software.
Here is an updated version of our CITATION.cff from the previous episode with a version number, DOI and release date added.

```yaml
# This CITATION.cff file was generated with cffinit.
# Visit https://bit.ly/cffinit to generate yours today!
cff-version: 1.2.0
title: My Software
message: >-
  If you use this software, please cite it using the
  metadata from this file.
type: software
authors:
  - given-names: Anne
    family-names: Researcher
version: 1.0.1
identifiers:
  - type: doi
    value: 10.5281/zenodo.1234
date-released: 2024-06-01
```

:::  challenge

### Add a DOI to your citation file

Add the DOI you were allocated in the previous exercise to your CITATION.cff file and commit/push the updated version to your Github repository. 
You can remove the `commit` field from the CITATION.cff file as the DOI is a better way to point to given version of the code.

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


# Working with collaborators

The strength of online collaboration tools such as Github doesn't just lie in the ability to share code. They also allow us to track problems with that code, 
for multiple developers to work on it independently and bring their changes together and to review those changes before they are accepted.

## Tracking issues with code

A key feature of Github (as opposed to Git itself) is the issue tracker. This provides us with a place to keep track of any problems or bugs in the code and to discuss them
with other developers. Sometimes advanced users will also use issue trackers of public projects to report problems they are having (and sometimes this is misused by users
seeking help using documented features of the program). 

The code from the testing chapter earlier has a bug with an extra bracket in eva_data_analysis.py (and if you've fixed that a missing import of summarise_categorical in the test).
Let's go ahead and create a new issue in our Github repository to describe this problem. We can find the issue tracker on the "Issues" tab in the top left of the Github 
page for the repository. Click on this and then click on the green "New Issue" button on the right hand side of the screen. We can then enter a title and description of our issue.

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

 - Go to the Github webpage for your code
 - Click on the Issues tab
 - Click on the "New issue" button
 - Enter a title and description for the issue
 - Click the "Submit Issue" button to create the issue.


:::::::::::::::::::::::::::::::::::::::::::::::

### Discussing an issue

Once the issue is created, further discussion can take place with additional comments. These can include code snippets and file attachments such as screenshots or logfiles.
We can also reference other issues by writing a # symbol and the number of the other issue. This is sometimes used to identify related issues or if an issue is a duplicate.

### Closing an issue

Once an issue is solved then it can be closed. This can be done either by pressing the "Close" button in the Github web interface or by making a commit which includes the word
"fixes", "fixed", "close", "closed" or "closes" followed by a # symbol and the issue number.

## Working in parallel with Git branches

Branching is a feature of Git that allows two or more parallel streams of
work. Commits can be made to one branch without interfering with
another. Branches are commonly used as a way for one developer to work on
a new feature or a bug fix while other developers work on other features.
When those new features or bug fixes are complete, the branch will be merged back with the main (sometimes called master) branch.

### Creating a new branch

New git branches are created with the `git branch` command. This should be followed by the name of 
the branch to create. It is common practice when the bug we are fixing has a corresponding issue to name the branch after the issue number and name. 
For example, we might call the branch `01-extra-brakcet-bug` instead of something less descriptive like `bugfix`. 

For example, the command:

```bash
git branch 01-extra-brakcet-bug
```

will create a new branch called `01-extra-brakcet-bug`. We can view the names of all the branches, by default there should be one branch called `main` or perhaps `master` and our new `01-extra-brakcet-bug` branch.
by running `git branch` with no parameters. This will put `*` next to the currently active branch.

```bash
git branch
```


```output
  01-extra-brakcet-bug
* main
```

We can see that creating a new branch has not activated that branch. To switch branches we can either
use the `git switch` or `git checkout` command followed by the branch name. For example:

```bash
git switch 01-extra-brakcet-bug
```

To create a branch and change to it in a single command we can use `git switch` with the `-c` option (or `git checkout` with the `-b` option, `git switch` is only found in more recent versions of Git).

```bash
git switch -c 02-another-bug
```

### Committing to a branch

Once we have switched to a branch any further commits that are made will go to that branch. When we run a `git commit` command we'll see the name of the
branch we're committing to in the output of `git commit`. Let's edit our code and fix the lack of default values bug that we entered into the issue tracker earlier on.

Change your code from

```python
<call to pandas without checks identified in testing section>
```

to:

```python
<call to pandas with checks identified in testing section>
```

and now commit it.

```bash
git commit -m "fixed bug" eva_data_analysis.py
```

In the output of `git commit -m` the first part of the output line will show the name of the branch we just made the commit to.

```output
[01-extra-brakcet-bug 330a2b1] fixes missing values bug, closes #01 
```

If we now switch back to the `main` branch our new commit will no longer be there in the source file or the output of `git log`.

```bash
git switch main
```

And if we go back to the `01-extra-brakcet-bug` branch it will re-appear.

```bash
git switch 01-extra-brakcet-bug
```

If we want to push our changes to a remote such as GitHub we have to tell the `git push` command which branch to push to. If the branch doesn't exist on the remote (as it currently won't)
then it will be created. 

```bash
git push origin 01-extra-brakcet-bug
```

If we now refresh the Github webpage for this repository we should see the bugfix branch has appeared in the list of branches.

If we needed to pull changes from a branch on a remote (for example if we've made changes on another computer or via Github's web based editor), then we can specify a branch on a `git pull` 
command.

```bash
git pull origin 01-extra-brakcet-bug
```

## Merging branches

When we have completed working on a branch (for example fixing a bug) then we can merge our branch back into the main one (or any other branch). This is done with the `git merge` command.

This must be run on the *TARGET* branch of the merge, so we'll have to use a `git switch` command to set this. 

```bash
git switch main
```

Now we're back on the main branch we can go ahead and merge the changes from the bugfix branch:

```bash
git merge 01-extra-bracket-bug
```

## Pull requests

On larger projects we might need to have a code review process before changes are merged, especially before they are merged onto the main branch that might be what is being released
as the public version of the software. Github has a process for this that it calls a "Pull Request", other Git services such as GitLab have different names for this, GitLab calls them "Merge Requests".
Pull requests are where one developer requests that another merge code from a branch (or "pull" it from another copy of the repository). The person receiving the request then has the
chance to review the code, write comments suggesting changes or even change the code themselves before merging it. It is also very common for automated checks of code to be run on a pull
request to ensure the code is of good quality and is passing automated tests.

As a simple example of a pull request, we can now create a pull request for the changes we made on our `01-extra-bracket-bug` branch and pushed to Github earlier on. The Github webpage for our repository
will now be saying something like "bugfix had recent pushes n minutes ago - Compare & Pull request". Click on this button and create a new pull request. 

Give the pull request a title and write a brief description of it, then click the green "Create pull request" button. Github will then check if we can merge this pull request without
any problems. We'll look at what to do when this isn't possible later on. 

There should be a green "Merge pull request" button, but if we click on the down arrow inside this button there are three options on how to handle this request:

1. Create a merge commit
2. Squash and merge
3. Rebase and merge

The default is option 1, which will keep all of the commits made on our branch intact. This can be useful for seeing the whole history of our work, but if we've done a lot of minor
edits or attempts at fixing a problem to fix one bug it can be excessive to have all of this history saved. This is where the second option comes in, this will place all of our changes from the branch into just 
a single commit, this might be much more obvious to other developers who will now see our bugfix as a single commit in the history. The third option merges the branch histories together
in a different way that doesn't make merges as obvious, this can make the history easier to read but effectively rewrites the commit history and will change the commit hash IDs. Some
projects that you contribute to might have their own rules about what kind of merge they will prefer. For the purposes of this exercise we'll stick with the default merge commit. 

Go ahead and click on "Merge pull request", then "Confirm merge". The changes will now be merged together. Github gives us the option to delete the branch we were working on, since
it's history is preserved in the main branch there isn't any reason to keep it.

### Using forks instead of branches

A fork is similar to a branch, but instead of it being part of the same repository it is a entirely new copy of the repository. Forks are commonly used by Github users who wish to work
on a project that they're not a member of. Typically forking will copy the repository to our own namespace (e.g. github.com/username/reponame instead of github.com/projectname/reponame)

To create a fork on github use the "Fork" button to the right of the repository name. After we create our fork we can make some changes and these could even be on the main branch 
inside our forked repository. Github will track that a fork has been made displays a "Contribute" button to create a pull request back to the original repository. Using this we can
request that the changes on our fork are incorporated by the upstream project.


:::  challenge

### Pull request exercise

Q: Work in pairs for this exercise. Share the Github link of your repository with your partner. 
If you have set your repository to private, you'll need to add them as a collaborator. Go to the settings page on your Github repository's webpage, click on Collaborators from 
the left hand menu and then click the green "Add People" button and enter the Github username or email address of your partner. 
They will get an email and an alert within Github to accept your invitation to work on this repository, without doing this they won't be able to access it.

 - Now make a fork of your partners repository. 
 - Edit the CITATION.cff file and add your name to it.
 - Commit these changes to your fork
 - Create a pull request back to the original repository
 - Your partner will now receive your pull request and can review 


:::::::::::::::::::::::::::::::::::::::::::::::

## Acknowledgements

The content of this episode was inspired / heavily borrowed from the following resources:

- Software carpentry git lesson licensing and citation sections - https://swcarpentry.github.io/git-novice/11-licensing.html and https://swcarpentry.github.io/git-novice/12-citation.html
- Carpentries Github Skill up - https://carpentries-incubator.github.io/github-skill-up-instructors/ and https://carpentries.github.io/github-skill-up-maintainers/
- RSG Soton Git lesson - https://southampton-rsg.github.io/swc-git-novice/06-collab/index.html

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- Licencing and citation episodes from the [Software Carpentry's Git Novice lesson][swc-git-lesson]
- [Open source definition][osd-definition], by the [Open Source Initiative][osd]
- [What is free software?][free-software]

Also check the [full reference set](learners/reference.md#litref) for the course.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Open source applies Copyright licenses permitting others to reuse and adapt your code or data.
- Permissive licenses allow code to be used in other products providing the copyright statement is displayed.
- Copyleft licenses require the source code of any modifications to be released under a copyleft license.
- Creative commons licenses are suitable for non-code files such as documentation and images.
- Open source software can be sold, but you must supply the source code and the people you sell it to can give it away to somebody else.
- Add license file to your repository and add a license to each file in case it gets detached.
- Zenodo can be used to archive a Github repository and obtain a DOI for it.
- We can include a CITATION file to tell people how to cite our code.
- Github can track bugs or issues with a program.
- Git branches can be used to allow multiple developers to work on the same part of a program in parallel.
- The `git branch` command shows the list of branches and can create new branches.
- The `git switch` command changes which branch we are working on.
- The `git merge` command merges another branch into the current one.
- Pull requests allow developers to work on their own branch/fork and then request other developers review their changes before they are merged.

::::::::::::::::::::::::::::::::::::::::::::::::::

