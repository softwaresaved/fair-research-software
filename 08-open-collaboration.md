---
title: Open project collaboration & management
teaching: 60
exercises: 30
---

::::::::::::::::::::::::::::::::::::: objectives
After completing this episode, participants should be able to:

- Explain why adding licensing information to a repository is important.
- Understand that some licenses are intended for code and others for data. 
- Understand your rights and obligations under the GPL, MIT, BSD, Apache 2 and Creative Commons licenses.
- Recall that open source software can be sold and used in commercial products but that license declaration will need to be included and any other terms of the license adhered to.
- Apply an appropriate open source license to a code repository that is shared on Github.
- Understand how to archive code to Zenodo and write a citation file that can be included with code shared on Github.
- Understand how to track issues with Github.
- Understand how to use Git branches for working on code in parallel and how to merge code back using pull requests.
- Apply issue tracking, branching and pull requests together to fix bugs while allowing other developers to work on the same code.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: questions 

- What licensing information should I include with my code and data?
- How do I share my code on Github?
- How do I ensure my code is citable?
- How do I track bugs in Github repositories and ensure that multiple developers can work on the same files simultaneously?

::::::::::::::::::::::::::::::::::::::::::::::::


# Licensing

## What is licensing and why is it important?

### Copyright Licenses

The authors of any creative work such as written text, photographs,
films, music and computer code are protected by Copyright law.  This
allows them to set the terms under which their work can be copied or
reproduced. This often takes the form of the creator of the work selling
copies of it and receiving a fee from each person who obtains a copy.
Those receiving the copies are typically forbidden from making additional
copies without the permission of the creator. For example if an author
writes a book they will receive some money for each copy of that book
that's sold and anybody who makes and sells a copy of that book would
need their permission to do so.

Copyright licenses don't necessarily require any money to be charged for
copies and the creator might choose to let anybody copy their work,
providing they don't change it and keep their name on it.

Copyright is automatically implied, any creative work which doesn't
specify a license should be assumed to be copyrighted. If it were ever to
come to a court case then the author might have a problem proving this
and enforcing their copyright. Technically the work is copyrighted the
moment it is created, even without any kind of copyright statement,
registration or license agreement.

### Copyright and Open Source

An Open Source license is a form of copyright license that gives anybody
who receives a copy of a work the right to make additional copies and distribute
them to anybody else. It also allows anybody who receives a copy to
make changes to the original work and to redistribute those. When applied
to software this usually requires that anybody supplying the executable binary of a program 
must also supply the source code if requested.

### Copyright Statements

A common way to declare your copyright of a program and the license you
are distributing it under is to include a file called LICENSE in your
code repository, to display it in comments in a code file or to display
it on screen when the program is run. At the very least each source file
should state what license the code is under and tell the reader to refer
to the LICENSE file. This means that if the code ever gets (accidentally)
redistributed without the license file then the reader will still know
about the license that was used. 

### Free Software

In the early history of computing there were often informal agreements
where programmers would share source code with each other, but this was
rarely backed up with any formal copyright license. As the field grew
this was first formalised in the 1980s by Richard Stallman who formed the
Free Software Foundation and defined "Free Software" as software which
which respects users freedoms by granting them four freedoms:

1. The freedom to run the program as you wish, for any purpose.
2. The freedom to study how the program works, and change it so it does your computing as you wish. 
Access to the source code is a precondition for this.
3. The freedom to redistribute copies so you can help your neighbor.
4. The freedom to distribute copies of your modified versions to others. By doing this you can give the whole 
community a chance to benefit from your changes. Access to the source code is a precondition for this.

The term "Free" in English often causes some confusion here as it can
mean both "free as in freedom" and "free as in beer" (no charge). The
term "Libre" software is sometimes used instead of "Free" to help clarify
this.

### Open Source Definition

In the 1990s the "Open Source" movement wanted to make a more business
friendly term and thought using the term "Free" might lead to confusion
when people wanted to charge for software. Despite "Free Software" often
being given away for no charge (or just a small charge/suggested donation
to cover media or distribution costs), nothing in the four freedoms and
the software licenses that were designed around it prohibits charging for
software. 

In 1998 the Open Source Definition was created and says that
software which is open source must be distributed under the a license
which allows the following:

1. Free Redistribution must be allowed
2. Source Code must be included
3. Derived Works must be allowed
4. Integrity of The Author’s Source Code - There can only be restrictions on the distribution of modifications if 
patches can be distributed instead. Must explicitly permit distribution of software built from modified source code. 
The license may require derived works to carry a different name or version number from the original software.
5. No Discrimination Against Persons or Groups
6. No Discrimination Against Fields of Endeavor
7. Distribution of License - License applies to anyone the software is distributed to
8. License Must Not Be Specific to a Product - the program can be extracted from other software it is distributed with
9. License Must Not Restrict Other Software, e.g. can't insist it is only distributed alongside other open source 
software.
10. License Must Be Technology-Neutral

### Free and Open Source Software

Because of these two terms many people use the term "Free and Open Source
Software" (FOSS), while other's simple say "Open Source Software" and some
will say "Free Software". In reality these all have very similar meanings
that will respect the four freedoms and the open source definition. For
the rest of this chapter we will refer to "Open Source", but could have
equally said "Free and Open Source Software" or "Free Software". 

## Types of licenses

A number licenses have been written that conform to the Four Freedoms
and/or the Open Source definition. Each of these set out the rights of
anybody receiving software that is distributed under that license. We
will look at a few of the most popular ones. 

### Public Domain  

Before we look at any licenses in detail, one other thing to consider is
Public Domain. This is a concept in some countries (but not all) where a
work is not protected by copyright. These works have no license from
their creators and typically anybody can do anything they like with them.
Copyrights are usually time limited to between 50 and 100 years and in
many jurisdictions when Copyrights expire the works enter the public
domain. It is for this reason that the works of Charles Dickens are no
longer subject to Copyright and anybody can make a copy of them. In some
jurisdictions works can be placed straight into the public domain simply
with a declaration within the work. In the USA works produced by the
federal government are automatically public domain. But in other
countries works need to be registered as public domain. For this reason
it isn't recommended to simply make work public domain if you want to
release it for use across the world.

If you really want to release code under something very similar to public domain then the 
[unlicense](https://unlicense.org/) could be for you. 
It states that anybody is free to use the software in any way they like. In jurisdictions with public domain, 
it "dedicates" the software into the public domain.


### Permissive Licenses

Some of the simplest open source licenses are known as the "permissive
licenses". Broadly speaking these require anybody redistributing the code
to include the license text and a copyright statement crediting the
authors. But they do not require any modifications to release their
source code alongside the executable program. This allows software
released under these licenses to be made into part of a closed source
program and all the creator of the closed source program needs to do is
distribute the license text and perhaps some crediting statement to the
original author, but they don't need to redistribute the source code with
their closed source program.

#### MIT License 

The MIT License is very simple and a very popular choice of license, it is only three paragraphs long. It
states that:

 * Anybody receiving the software can copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the software to anybody they like.
 * That they must include the license text and copyright statement when they redistribute it.
 * That there's no warranty included and you can't hold the authors liable for any problems or damages that might arise.

#### BSD 

The BSD license is very similar to the MIT license, but it has several
variants. The oldest is the 4 clause version which requires:

 * Source code redistributions must include the copyright statement and license text.
 * Binary redistributions must include the copyright notice and license text in their documentation.
 * Any advertising for the software incorporating this software must include a statement saying that it includes 
software written by the author.
 * That the author doesn't endorse any derived products.
 * That the author doesn't provide a warranty. (this is written in a separate section and isn't one of the 4 clauses)

The acknowledgement/advertising clause caused some controversy and some people
thought that it didn't meet the open source definition or comply with the
four freedoms. It also became impractical and lead to very long statements where there were multiple authors of large 
pieces of software.

To address this a new version of the license known as the
3 clause BSD license was created. This removed the acknowledgement
clause. An even simpler 2 clause version removes the endorsement clause.

#### Apache 2.0

Another popular permissive license is the Apache 2.0 license. It is very
similar to the MIT and BSD licenses, but also includes some clauses about
patent licensing. These require any contributor to a program which is
licensed under Apache 2.0 to allow their patents to be used free of
charge by any user of the software. This was done to head off some
concerns about software patent legislation at the time the license was
developed.

### Copyleft Licenses

The other common form of open source licenses are the "Copyleft"
licenses. These require that any modifications to the program are also
released under a compatible copyleft license. This can cause
complications when combining code that's under copyleft with other
licenses as now the entire codebase must be released under the copyleft
license. If there are any incompatible terms in the other license then
this can prevent the two codebases from being combined. 

The main advantage of copyleft licenses is that anybody else who
incorporates the code into another product must also keep that product
open and this makes it harder for it to be subsumed into a commercial
product that doesn't contribute improvements to the code back to the
community which created it.

#### GPL version 2

The mostly commonly known copyleft license is the GNU Public License or
GPL. There are several versions of the GPL available, the oldest GPL
version 1.0, but this version was quickly replaced with version 2.0 and
was rarely used. Version 2 is much more common and is used by a lot of
popular software including the Linux Kernel. Compared with the permissive
license the GPL is quite a long license agreement and many of its clauses
can be quite difficult for non-lawyers to fully understand.

#### GPL version 3

The GPL version 3 was introduced to try and prevent patenting of software
under the license and to require that people distributing GPL code on
embedded systems must also give users the ability to rebuild that
software and use it in their device. It is an even longer document than
GPL version 2 and has proved controversial with some and despite coming out in 2007
hasn't been adopted by many projects which used GPL version 2.

#### LGPL

In order to allow library software to be combined with ("linked" in
technical terms) other software that is not GPLed, a special version of the
GPL called the LGPL (L for "Lesser" or "Library") was created. This is
used by many popular libraries including the GNU C library that is linked
to every C program compiled on a Linux system.  


#### AGPL

One problem for the GPL is that a lot of modern software doesn't run on
user's own computers, but on remote web servers that they connect to
through their web browser. When a user run's one of these web
applications they aren't receiving a copy of the software's executable
binaries, but are interacting with them over a computer network such as
the internet. This doesn't meet the GPL's definition of distributing the
binaries, so even if the web application is under the GPL, the person
running the server has no obligation to supply users with the source
code. The Affero GPL or AGPL requires that people running web
applications licensed under the AGPL make the source code available to
the users of those web applications. 

### Choosing a License

When choosing a license for your code there's a number of things you might want to consider:

* Do you want to ensure that anybody modifying and redistributing your code will release the source code of their 
changes?
* Or would you prefer to ensure the least number of restrictions and that your code will be used as 
widely as possible? Even if that means it might end up in commercial products that don't release their source code.
* Are you reusing code which is already under an open source license? What obligations do you have under those licenses? 
* Is there a preferred license in your research community?

Don't be tempted to write you're own license (or modify an existing one)
unless you are a copyright lawyer. The common open source licenses have
been carefully written by copyright lawyers, many of them have undergone
multiple iterations in response to cases that have arisen and the
implications of many different legal jurisidcitons has been considered.
The common licenses are also well known, meaning that potential users and
contributors have a better understanding of what their rights and
responsibilities are leaving less room for misunderstanding.

#### Tools to help you choose

The website [choosealicense.com](https://choosealicense.com) has some great
resources to help you choose a license that's appropriate for your needs.

:::  challenge

### License selection exercise

Q: You have created a library of functions that are commonly used by
researchers in your field. You would like to share this code with your
research community and ensure that the code remains as open as possible
to benefit the community. But you would also like to see it being
integrated into as many different research codes and even commercial
products as possible. What would be a good choice of license? (hint: You
can use the [choosealicense.com](https://choosealicense.com) website to help you)

:::  solution

A: The LGPL license could be a good choice for library code. It can be
linked to software that isn't GPL licensed but any modifications to the
library itself must be released under a GPL compatible license.

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::


### Creative Commons Licenses

All of the licenses we've discussed so far are really only intended for
source code. They are not suitable for documentation, datasets, drawings,
logos, music, maps etc. To solve this problem there are the Creative
Commons licenses, which are expressly built for anything other than
source code. Creative commons has now gone through four versions with the
latest being version 4.0, generally you should use version 4.0 as this is
more suited for use around the world 

There are several different types of Creative Commons licenses:

#### CC0

Creative Commons Zero or CC0 is the simplest license and is effectively a
public domain license, but is suitable for use world wide.

####  Attribution (BY)

All the Creative Commons licenses apart from CC0 require you to give
credit to the original creator. This is very similar to what is required
by all of the permissive code licenses.

#### Share-a-like (SA)

Share-a-Like Creative Commons licenses requires any derivative works to
be released under a compatible creative commons license. This is very
similar to the way that Copyleft licenses work.

#### Non-Commercial (NC)

Non-commercial creative commons licenses only allow for non-commercial
use of the work.


#### No Derivatives (ND)

No derivatives creative commons licenses require that users of the work
can't redistribute modified versions of it.

#### Combinations of Creative Commons Licenses

Under these rules the following combinations are possible:

* CC-BY - Creative Commons Attribution
* CC-BY-SA - Creative Commons Attribution Share Alike
* CC-BY-NC - Creative Commons Non Commercial
* CC-BY-NC-SA - Creative Commons Non Commercial Share Alike
* CC BY-ND - Creative Commons No Derivatives
* CC BY-ND-NC - Creative Commons No Derivatives Non Commercial

:::  challenge

### License selection exercise 2

Choose a license for your code and data from the pervious exercises.
Discuss with your neighbour or the group your choice of license and
reason for choosing it.

:::::::::::::::::::::::::::::::::::::::::::::::


:::  challenge

### Adding a license to your code

Add a LICENSE file containing the full text of the license you've chosen to the Git repository of your code from 
previous chapters of this lesson.
Add a copyright statement, the name of the license you are using and a
mention of the LICENSE file to at least one source file  
Push your changes to your Github repository. Check the "About" section of your repository's Github webpage and see 
if there is now a license listed.

:::::::::::::::::::::::::::::::::::::::::::::::



## Relicensing

### License Compatibility

Generally, you can relicense someone else's code under more permissive
licenses to less permissive ones without their permission. For example,
you could relicense code from the MIT license to the GPL. This is because
nothing in the GPL contradicts anything in the MIT license, but you'll
still have to display the MIT license for the original code and the GPL
for your modifications. 

This doesn't work the other way though, you can't take code released
under GPL and relicense it as MIT since MIT is a more liberal license
that doesn't match the terms of the GPL.

Creative commons zero or public domain code can usually be relicensed to
any open source license (or a commercial license for that matter). 

Sometimes there are contradictory statements in licenses which prevent
relicensing. For example Apache 2 has some provisions about software
patents, you won't be able to relicense Apache 2 code under MIT since it
doesn't have an equivalent patent clause.

The GNU project has a
[useful guide][gnu-license-guide] to license compatibility on their website.

### Getting agreement to relicense

Sometimes the developers of a program will wish to change the license it
is distributed under. In order to do this they'll need the agreement of
all the copyright holders of the program and typically this will mean
everyone who contributed code to it. This is fine if you only have a
handful of contributors to your project, but gets harder when the project
starts to grow bigger.

Some projects work around this by having contributors agree to a
"contributor license agreement". This will set out the terms under which
the code is contributed to the project. It might include a copyright
assignment or just granting certain rights to the project. This usually
allows the company (or non-profit foundation as many open source projects
are based on non-profit foundations) running the project to relicense the
code in future and to take legal action against people who violate the
license.

### Going commercial

It is possible to sell software that is licensed under an open source
license commercially, you will need to supply the source code along with
the binaries. However, under any license meeting the Open Source
Definition or the Four Freedoms the person receiving the software can
make copies and give (or sell) them to anybody else. 

It is also possible to release software under two licenses, one open
source and one commercial. This has been done by a few open source
projects who wish to sell the software to some customers (sometimes with
extra custom modifications) and give it to others. 


:::  challenge

### Relicensing exercise

Q: Find the webpage of a major open source project that is relevant to
your research or the `Spacewalks` codebase we have been working with. See if you can find a contributor license agreement. Add a
link to this in the chat/etherpad/hackmd. 

Hint: try looking at Matplotlib - https://matplotlib.org which Spacewalks uses for plotting

:::  solution

A: Here are a few examples:

   Python - https://www.python.org/psf/contrib/

   Scipy - https://github.com/scipy/scipy/blob/main/CONTRIBUTING.rst

   Matplotlib - https://matplotlib.org/stable/project/license.html

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

# Sharing your code to encourage collaboration

## Getting Code Ready to Share

In addition to adding a license to our code there are several other important steps to consider before sharing it publicly.

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

### Archiving to Zenodo and Obtaining a DOI

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

## Tracking Issues with Code

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

## Working in Parallel with Git Branches

Branching is a feature of Git that allows two or more parallel streams of
work. Commits can be made to one branch without interfering with
another. Branches are commonly used as a way for one developer to work on
a new feature or a bug fix while other developers work on other features.
When those new features or bug fixes are complete, the branch will be merged back with the main (sometimes called master) branch.

### Creating a new Branch

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

## Merging Branches

When we have completed working on a branch (for example fixing a bug) then we can merge our branch back into the main one (or any other branch). This is done with the `git merge` command.

This must be run on the *TARGET* branch of the merge, so we'll have to use a `git switch` command to set this. 

```bash
git switch main
```

Now we're back on the main branch we can go ahead and merge the changes from the bugfix branch:

```bash
git merge 01-extra-bracket-bug
```

## Pull Requests

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

### Using Forks Instead of Branches

A fork is similar to a branch, but instead of it being part of the same repository it is a entirely new copy of the repository. Forks are commonly used by Github users who wish to work
on a project that they're not a member of. Typically forking will copy the repository to our own namespace (e.g. github.com/username/reponame instead of github.com/projectname/reponame)

To create a fork on github use the "Fork" button to the right of the repository name. After we create our fork we can make some changes and these could even be on the main branch 
inside our forked repository. Github will track that a fork has been made displays a "Contribute" button to create a pull request back to the original repository. Using this we can
request that the changes on our fork are incorporated by the upstream project.


:::  challenge

### Pull Request Exercise

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

