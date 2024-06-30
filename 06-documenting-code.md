---
title: Documenting code
teaching: 60
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions 

- How should we document our code?
- Why are documentation and repository metadata important and how they support FAIR software?
- What are the minimum elements of documentation needed to support FAIR software?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives
After completing this episode, participants should be able to:

- Use a`README` file to provide an overview and a `CITATION.cff` file to add citation instructions to a code repository 
- Describe the main types of software documentation (tutorials, how to guides, reference and explanation).
- Apply a documentation framework to write effective documentation of any type. 
- Describe the different formats available for delivering software documentation (Markdown files, wikis, static webpages).
- Implement MkDocs to generate and manage comprehensive project documentation

::::::::::::::::::::::::::::::::::::::::::::::::


## Motivation
The purpose of software documentation is to communicate important information 
about our code to the people who need it – users and developers.   

###  Better Research
Software documentation is often perceived as a thankless task with few tangible benefits and is often neglected in 
research projects. 
However, like software testing, documenting our code can help us become more productive researchers. 
Here are some advantages of documenting our code: 

- Good documentation captures important methodological details ready for when we come to publish our research 
- Good documentation  can help us return to a project seamlessly after time away. 
- Documentation can  facilitate collaborations by helping to onboard new project members
- Good documentation can save us time by answering FAQs about our code for us.


### FAIR Software
Software documentation supports FAIR software by improving the re-usability of our code. 

+ How-to guides and Tutorials ensure that users can install our software independently and make use of its basic features

+ Reference guides and background information  can help developers understand our code sufficiently to modify / extend / repurpose it.

## Software-level Documentation
In previous episodes we encountered several different forms of in-code documentation 
including  in-line comments and docstrings.  

These are an excellent way to improve the readability of our code, but by themselves 
are insufficient to ensure that our code is easy to use, understand and modify - 
this requires additional software-level documentation.

### Types of Documentation
There are many different types of software-level documentation.

#### Technical Documentation
Software-level technical documentation encompasses:

+ Tutorials - lessons that guide learners through a series of exercises to build proficiency as using the code  
+ How-To Guides - step by step instructions on how to accomplish specific goals using the code.
+ Reference - a lookup manual to help users find relevant information about the software e.g. functions and their parameters.
+ Explanation - conceptual discussion of the code to help users understand implementation decisions 

#### Repository Metadata Files
In addition to software-level technical documentation, it is also common to see repository metadata files included 
in a code repository.
Many of these files can be described as "social documentation" i.e. they indicate how users should “behave” in relation 
to our software project. 
Some common examples of repository metadata files and their role are tabulated below:

|     File            |   Description                                                                                                               |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------|
| CONTRIBUTING.md     |   Explains to developers how to contribute code to the project including processes and   standards that should be followed. |
| CODE_OF_CONDUCT.md  |   Defines   expected standards of conduct when engaging  in a software project.                                             |
| LICENSE             |   Defines   the  (legal) terms of use of a piece of   code.                                                                 |
| CITATION            |   Provides instructions on how and when to cite the code      |

## Just Enough Documentation
However, for many small projects the following three pieces of documentation will be sufficient:

+	README - A document that provides an overview of the project, including installation, usage instructions, and dependencies.
  A README may include one or more of the technical documentation types - tutorial / how-to / explanation / reference.
+	LICENSE - A file that outlines the legal terms for using, modifying, and distributing the project.
+	CITATION - A file that provides instructions on how to properly cite the project in academic or professional work.

Let’s look at each of these in turn.

#### README
A README file acts as a “landing page” for your code repository on GitHub and should provide sufficient information for users to and developers to get started using your code.   

::::::::::::::::::::::::::::::::::::: discussion 

## READMEs and The FAIR Principles

Think about the question below. Your instructors may ask you to share your answer in a shared notes document and/or discuss them with other participants.

Here are some of the major sections you might find in a typical README. Which are **essential** to support the FAIR principles? Which are optional?

+ Purpose of the code
+ Audience (who the code is intended for)
+ Installation Instructions
+ Contribution Guide
+ How to Get Help
+ License
+ Software Citation
+ Usage Example
+ Dependencies and their versions
+ FAQs
+ Code of Conduct

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: spoiler 

## Discussion Spoilers

To support the FAIR principles (Findability, Accessibility, Interoperability, and Reusability), certain sections in a README file are more important than others. Below is a breakdown of the sections are ESSENTIAL / OPTIONAL in a README to align with these principles. 

### Essential

1. **Purpose of the code**
   - **Explanation:** Clearly explains what the code does. This is essential for findability and reusability.

2. **Installation Instructions**
   - **Explanation:** Provides step-by-step instructions on how to install the software, ensuring accessibility.

3. **Usage Example**
   - **Explanation:** Provides examples of how to use the code, helping users understand its functionality and enhancing reusability.
   
4. **License**
   - **Explanation:** Specifies the terms under which the code can be used, which is crucial for legal clarity and reusability.

5. **Dependencies and their versions**
   - **Explanation:** Lists the external libraries and tools required to run the code, including their versions. This is essential for  reproducibility and interoperability.

6. **Software Citation**
   - **Explanation:** Provides citation information for academic use, ensuring proper attribution and reusability.

### Optional

7. **Audience (who the code is intended for)**
   - **Explanation:** Helps users identify if the code is relevant to them, improving findability and usability.
   

8. **How to Get Help**
   - **Explanation:** Informs users where they can get help, ensuring better accessibility.


9. **Contribution Guide**
   - **Explanation:** Encourages and guides contributions from the community, enhancing the code's development and reusability.

10. **FAQs**
   - **Explanation:** Provides answers to common questions, aiding in troubleshooting and improving accessibility.


11. **Code of Conduct**
   - **Explanation:** Sets expectations for behaviour in the community, fostering a welcoming environment and enhancing accessibility.

:::::::::::::::::::::::::::::::::


Let's create a simple README for our repository.

``` bash
$ cd ~/Desktop/spacewalks
$ touch README.md
```

Let's start by adding a one-liner that explains the purpose of our code and who it is for.

``` code
# Spacewalks

## Overview
Spacewalks is a python-based analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.
```

Now let's add a list of Spacewalk's key features:

``` code
## Features
Key features of Spacewalks:
- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time
```

Now let's tell users about any Pre-requisites required to run the software:

``` code
## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12 
installed. You will also need the following libraries (minimum versions in brackets)

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation 
```

:::  challenge

## Spacewalks README

Extend the README for Spacewalks by adding
a. Installation instructions
b. A simple usage example

:::  solution

Installation instructions:

  ```text
# Installation instructions

+ Clone the Spacewalks repository to your local machine using Git.
If you don't have Git installed, you can download it from the official Git website.

\`\`\`bash
git clone https://github.com/your-repository-url/spacewalks.git
cd spacewalks
\`\`\`

+ Install the necessary dependencies:
\`\`\`bash
pip install pandas==2.2.2 matplotlib==3.8.4 numpy==2.0.0 pytest==7.4.2
\`\`\`

+ To ensure everything is working correctly, run the tests using pytest.

\`\`\`bash
python -m pytest
\`\`\`
```

Usage instructions:

```text
# Usage Example

To run an analysis using the Spacewalks.py script from the command line terminal,
launch the script using Python as follows:

\`\`\`python
# Usage Examples
python spacewalks.py eva-data.json eva-data.csv
\`\`\`

The first argument is path to the Json data file.
The second argument is the path the CSV output file.
```
::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::


#### LICENSE
A license file outlines the legal terms for using, modifying, and distributing the project.
We'll talk about choosing a license in detail in later episode.

#### CITATION File
We can add a citation file to our repository to provide instructions on how and when to cite our code.

Citation files use a special format called CFF - the Citation File Format (CFF) and are
a way to include metadata about software or datasets in plain text files, making it easy
for both humans and machines to use this information.

**Why Use CFF?**

+ For developers, using a CFF file can help to automate the process of publishing
new releases on Zenodo via GitHub.

+ For users, having a CFF file makes it easy to cite the software or dataset.  with formatted citation information available for copy-paste and direct import into reference managers like Zotero from GitHub.

**Creating a CFF File**

A CFF file is written in YAML format.
At a minimum a CFF file must contain the title of the software/data, the type of asset (software/data)
and at least one author:

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
```

Additional, optional metadata includes an Abstract, repository URL and more.

**Steps to Make Your Software Citable**

We can create (and update) a CFF file for our software using an online Web App called
[`cffinit`][cffinit-webapp].

Let's create a dummy citation file for a project called "Spacetravel" with Author "Max Hypothesis", follow these steps:

  1. First, head to `cffinit` online at [`cffinit`][cffinit-webapp].
2. Then, let's work through the metadata input form to complete the minimum information needed to generate a CFF. We'll also add the following abstract:

  "Spacetravel - a simple python script to calculate time spent in Space by individual NASA astronauts"

3. At the end of the process, download the CFF file and inspect it. It should look like this:

```yaml
# This CITATION.cff file was generated with cffinit.
# Visit https://bit.ly/cffinit to generate yours today!

cff-version: 1.2.0
title: Spacetravel
message: >-
  If you use this software, please cite it using the
  metadata from this file.
type: software
authors:
  - given-names: Hypthesis
    name-particle: Max
abstract: >-
    A simple python script to calculate time spent in Space by individual NASA astronauts
```

**Updating and citing**

CFF files can also be updated using `cffinit`.

To cite our software (or dataset), once a CFF file has been pushed to our remote repository,
GitHub's "Cite this repository"  button can be used to generate a citation in various  formats (APA, BibTeX).

**Tools**
Command line tools are also available for creating, validating, and converting CFF files. 
Further information is available from the [Turing Way's guide to software citation][turing-way-citation].

:::  challenge

## `Spacewalks` Software Citation

Write a software citation file for the Spacewalks code and add it to the root
folder of our project.

+ Add the URL of the code repository as a "Related Resources"
+ Add a one-line description of the code under the "Abstract" section
+ Add at least two key words under the "Keywords" section
+ Use the commit hash of your most recent commit to indicate the code
  version your citation file refers to.

:::  solution

Use [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/#/version-specific),
a web application to create your citation file using a series of online forms.

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
    name-particle: Sara
  - given-names: Aleksandra
    family-names: Nenadic
  - given-names: 'Kamilla'
    family-names: Kopec-Harding
  - given-names: YOUR
    family-names: NAME-HERE
repository-code: >-
  https://github.com/YOUR-REPOSITORY-URL/spacewalks.git
abstract: >-
  A python script to analyse NASA extravehicular activity
  data
keywords:
  - NASA
  - Extravehicular Activity
commit: 9736ffcf257b55fd60abedabc8bb28e4e012f012
```
:::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::::::::::::::


## Tools

Once our project reaches a certain size or level of complexity we may want to add
additional documentation such as a standalone tutorial or “Background” explaining our methodological choices.

Once we move beyond using a README as our primary source of documentation, we need to
consider how we will distribute our documentation to our users.

Options include:

+ A `docs/` folder of Markdown files.
+ Adding a Wiki to our repository.
+ Creating a set of web pages for our documentation using a static site generator for our documentation such
  as Sphinx or MkDocs

Creating a static site is a popular solution as it has the key benefit being able to
automatically generate a reference manual from any docstrings we have added to our code.


### MkDocs

Let's setup MkDocs.

```bash
python -m pip install mkdocs
python -m pip install "mkdocstrings[python]"
python -m pip install mkdocs-material
```

Let's check that MkDocs has been setup correctly:
```bash
python -m pip list
```

Let's create a `mkdocs.yml` file to configure `mkdocs` package installation.

```bash
# In ~/Desktop/spacewalks
touch mkdocs.yml
```

```yaml
site_name: Spacewalks Documentation

theme:
  name: "material"
font: false
nav:
  - Spacewalks Documentation: index.md
  - Tutorials: tutorials.md
  - How-To Guides: how-to-guides.md
  - Reference: reference.md
  - Background: explanation.md
```

Note font-false is for GDPR compliance

Let's add support for `mkdocstrings` - this will allow us to automatically our docstrings
into our documentation using a simple tag.

```yaml
site_name: Spacewalks Documentation

theme:
  name: "material"

nav:
  - Spacewalks Documentation: index.md
  - Tutorials: tutorials.md
  - How-To Guides: how-to-guides.md
  - Reference: reference.md
  - Background: explanation.md

plugins:
  - mkdocstrings

```

Let's populate our reference file with the docstrings we created.

```markdown
This file documents the key functions in the Spacewalks tool.
It is provided as a reference manual.
```

Let's build our documentation.

```bash
mkdocs build
```

Once the build step is completed, our documentation site is save to 
a `site` folder in the root of our project folder.

These files will be distributed with our code. We can either direct users
to read these files locally on their own device using their browser, 
or we can choose to host our documentation as a website that our
uses can navigate to.

::::::::::::::::::::::::::::::::::::: callout

## Hosting Documentation

In the previous section, we saw how mkdocs documentation can be distributed with our
repository and viewed "offline"  using a browser.

We can also make our documentation available as a live website by deploying our
documentation to a hosting service.

### GitHub Pages
As our repository is hosted in GitHub, we can use GitHub Pages - a service that
allows GitHub users to host websites directly from their GitHub repositories.

There are two types of GitHub Pages: project pages and user/organization Pages.
While similar, they have different deployment workflows, and we will only discuss
project pages here. For information about deploying to user/organisational pages, see
[MkDocs Deployment pages][mkdocs-deploy].

Project Pages deploy site files to a branch within the project repository (default is gh-pages).
To deploy our documentation:

1. First let us commit our documentation to the main branch of our git repository and push the changes to GitHub

```bash
$ git add .
$ git commit -m "Add project-level documentation"
$ git push origin main
```

> **Warning!**
> Before we proceed to the next step, we MUST ensure that there are no uncommitted changes or untracked files in
> our repository.
>
> If there are, the commands used in the upcoming steps will include them in our documentation!

2. Once we are on the main branch and all our changes are up to date, run the following command to deploy our documentation to GitHub.

```bash
mkdocs gh-deploy
```
This command will build our documentation with MkDocs, then commit and push the files to the gh-pages branch using the ghp-import tool.

For more options, use:
```bash
mkdocs gh-deploy --help
```
Notice that the deploy command did not allow us to preview the site before it was pushed to GitHub; so, it is a good idea to check
changes locally with the build  commands before deploying.

### Other Options
You can find out about other deployment options including free documentation hosting service ReadTheDocs on the [MkDocs deployment pages][mkdocs-deploy].

:::::::::::::::::::::::::::::::::::::


## Documentation Guides

Once we start to consider other forms of documentation beyond the README,
we can also increase the re-usability of our code by ensuring that the content and style of
our documentation matches its purpose.

Documentation guides such as [Write the Docs][write-the-docs], [The Good Docs Project][the-good-docs-project] and the [Diataxis framework][diataxis-framework]
provide a range of resources including documentation templates to help to help us do this.

:::  challenge

### A Spacewalks How-to Guide

a. Review the Diataxis guidance page on writing a How-to guide. Identify
three features of an effective how-to guide.

b. Following the Diataxis guidelines, add a How-to Guide to the `docs` folder
that show users how to change the destination filename for the output dataset generated
by Spacewalks.

:::  solution

An effective How-to guide should:

+ be goal oriented and focus on action.
+ avoid teaching or explanation
+ use appropriate language e.g. conditional imperatives
+ have an informative title

```text
# How to change the file path of Spacewalk's output dataset

This guide shows you how to set the file path for Spacewalk's output
data set to a location of your choice.

By default, the cleaned data set generated by Spacewalk is saved to the current
working directory with file name `eva-data.csv`.

If you would like to modify the name or location of the output dataset, set the
second command line argument to your chosen file path.

\`\`\`python
python spacewalks.py eva-data.json data/clean/eva-data-clean.csv
\`\`\`

The specified destination folder must exist before running spacewalks.

```
:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::




::::::::::::::::::::::::::::::::::::: discussion

## A Spacewalks Tutorial

The Diataxis framework provides guidance for developing technical documentation
for different purposes. Tutorials differ in purpose and scope to How-to Guides and as a result
differs in content and style.

We have adapted the How-to guide from the previous challenge into
the tutorial below. How does the content and language of the tutorial
differ from the how-to guide?



### Tutorial: Changing the File Path for the Spacewalks Output Dataset

#### Introduction
In this tutorial, we will learn how to change the file path for the output dataset generated by Spacewalk.
By the end of this tutorial, you will be able to specify a custom file path for the cleaned dataset.

#### Prerequisites
Before you start, ensure you have the following:

+ Python installed on your system
+ The Spacewalk script (eva_analysis.py)
+ An input dataset (eva-data.json)

####  Prepare the Destination Directory
First, let us decide where we want to save the cleaned dataset.
and make sure the directory exists.

For this tutorial, we will use data/clean as the destination folder.

Let's create the directory if it doesn't exist:

```bash
mkdir -p data/clean
```

#### Run the Spacewalk Script with Custom Path
Next, execute the Spacewalk script and specify the custom file path for the output dataset:
```bash
python eva_analysis.py <input-file> <output-file>
```

Replace <input-file> with your input dataset (eva-data.json) and <output-file> with your desired output path (data/clean/eva-data-clean.csv).

Here is the complete command:
```bash
python eva_analysis.py eva-data.json data/clean/eva-data-clean.csv
```

Notice how the output to the command line clearly indicates that we are using a custom output file path.

```output
TODO
```

After running the script, let us check  the data/clean directory to ensure the
cleaned dataset has been saved correctly.

```bash
ls data/clean
```
You should see eva-data-clean.csv listed in the data/clean folder


#### Exercise: Custom Output Path

+ Create a new directory named output/data in your working directory.
+ Run the Spacewalk script to save the cleaned dataset in the newly created output/data directory with the filename cleaned-eva-data.csv.
+ Verify that the dataset has been saved correctly.

##### Solution

```bash
# Create the directory:
mkdir -p output/data

# Run the script:
python spacewalks.py eva-data.json output/data/cleaned-eva-data.csv

# Verify the output:
ls output/data

# You should see cleaned-eva-data.csv listed
```

### Summary
Congratulations! You have successfully changed the file path for Spacewalks output dataset
and completed an exercise to practice the process. You can now customize the output location
and filename according to your needs.



:::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: spoiler

## Content
- The tutorial clearly signposts what will be covered
- Includes a narrative of each step and the expected output
- Highlights important behaviour the learner should notice
- Includes an exercise to practice skills

## Language
- Uses "we" language
- Uses imperative to provide clear instructions "First do x, then do y"

:::::::::::::::::::::::::::::::::


## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- ["The Art of Readme"][art-of-readme] article by Kira Oakley - a useful discussion of best practices for writing
  a high-quality README
- [What are best practices for research software documentation?][ssi-blog-docs] (Software Sustainability blog post) by Stephan Druskat et al.
- [Preparing Software for Reuse and Release episode][python-irsd-reuse-and-release] from the Intermediate Research Software Development lesson on The Carpentries Incubator by Aleksandra Nenadic et al.
- [How to document your research software][coderefinery-documentation] Coderefinery lesson

Also check the [full reference set](learners/reference.md#litref) for the course.


:::::::::::::::::::::::::::::::::::::::: keypoints

- Documentation allows users to run and understand software without having to work things out for themselves 
directly from the code.
- Software documentation supports the FAIR principles by improving the reusability of research code.
- A (good) README, CITATION file and LICENSE file are the minimum documentation elements required to support FAIR 
research code.
- Documentation can be provided to users in a variety of formats including a `docs` folder of Markdown files, 
a repository Wiki and static webpages.
- A static documentation site can be created using the tool `mkdocs`.
- Documentation frameworks such as Diataxis provide content and style guidelines that can helps us write high 
quality documentation.

::::::::::::::::::::::::::::::::::::::::::::::::::

