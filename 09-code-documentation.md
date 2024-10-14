---
title: Code documentation
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

- Use a `README` file to provide an overview and a `CITATION.cff` file to add citation instructions to a code repository 
- Describe the main types of software documentation (tutorials, how to guides, reference and explanation).
- Apply a documentation framework to write effective documentation of any type. 
- Describe the different formats available for delivering software documentation (Markdown files, wikis, static webpages).
- Implement MkDocs to generate and manage comprehensive project documentation

::::::::::::::::::::::::::::::::::::::::::::::::


We have seen how writing inline comments and docstrings within our code can help with improving its readability. 
The purpose of software documentation is to communicate other important information 
about our software (its purpose, dependencies, how to install and run it, etc.) to the people who need it – 
both users and developers.   

::: callout

### Activate your virtual environment
If it is not already active, make sure to activate your virtual environment from the root of
the software project directory:

```bash
(venv_spacewalks) $ source venv_spacewalks/bin/activate # Mac or Linux
(venv_spacewalks) $ source venv_spacewalks/Scripts/activate # Windows
(venv_spacewalks) $
```
:::

:::::: instructor

At this point, the code in your local software project's directory should be as in:
https://github.com/carpentries-incubator/astronaut-data-analysis-not-so-fair/tree/09-code-documentation.

::::::

## Why document our software?

Software documentation is often perceived as a thankless and time-consuming task with few tangible benefits and 
is often neglected in research projects. 
However, like software testing, documenting our software can help us and others
conduct **better research** and produce **FAIR software**:

- Good documentation captures important methodological details ready for when we come to publish our research 
- Good documentation can help us return to a project seamlessly after time away 
- Documentation can facilitate collaborations by helping us onboard new project members quickly and more easily
- Good documentation can save us time by answering frequently asked questions (FAQs) about our code for us
- Software documentation supports the FAIR research software principles by improving the re-usability of our code. 
  - Good documentation can make our software more understandable and reusable by others, and can bring us some citations
    and credit
  - How-to guides and tutorials ensure that users can install our software independently and make use of its basic features
  - Reference guides and background information can help developers understand our code sufficiently to 
  modify/extend/repurpose it.

## Software-level documentation

In previous episodes we encountered several different forms of in-code documentation aspects, 
including in-line comments and docstrings. 
These are an excellent way to improve the readability of our code, but by themselves 
are insufficient to ensure that our code is easy to use, understand and modify - 
this requires additional software-level documentation.

There are many different types of software-level documentation.

### Technical documentation

Software-level technical documentation encompasses:

- Tutorials - lessons that guide learners through a series of exercises to build proficiency as using the code  
- How-To Guides - step by step instructions on how to accomplish specific goals using the code.
- Reference - a lookup manual to help users find relevant information about the software e.g. functions and their parameters.
- Explanation - conceptual discussion of the code to help users understand implementation decisions 


## Project-level documentation 

Project-level documentation includes various information and metadata about software 
that help to discover it, explain the legal terms of reusing it, describe its functionality on a high level 
and how to install, run and contribute to it.

### Repository metadata files

A common way to to provide project-level documentation is to include various metadata files in the software 
repository together with code.
Many of these files can be described as "social documentation", i.e. they indicate how users should “behave” in relation 
to our software project. 
Some common examples of repository metadata files and their role are explained below:

| File            | Description                                                                                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| README          | Provides an overview of the project, including installation, usage instructions, dependencies and links to other metadata files and technical documentation (tutorial/how-to/explanation/reference) |
| CONTRIBUTING    | Explains to developers how to contribute code to the project including processes and standards that should be followed                                                                              |
| CODE_OF_CONDUCT | Defines expected standards of conduct when engaging  in a software project                                                                                                                          |
| LICENSE         | Defines the (legal) terms of using, modifying and distributing the code                                                                                                                             |
| CITATION        | Provides instructions on how to cite the code                                                                                                                                                       |
| AUTHORS         | Provides information on who authored the code (can also be included in CITATION)                                                                                                                    |


::: callout
### Just enough documentation

For many small projects the following three pieces of project-level documentation may be sufficient: README, LICENSE and 
CITATION.
:::

Let’s look at each of these files in turn.

### README file
A README file acts as a “landing page” for your code repository on GitHub and should provide sufficient information for users to and developers to get started using your code.   

::::::::::::::::::::::::::::::::::::: challenge 

### README and the FAIR principles

Think about the question below. Your instructors may ask you to share your answer in a shared notes document and/or 
discuss them with other participants.

Here are some of the major sections you might find in a typical README. 
Which are **essential** to support the FAIR principles? Which are optional?

+ Purpose of the code
+ Audience (who the code is intended for)
+ Installation instructions
+ Contribution guide
+ How to get help
+ License
+ Software citation
+ Usage example
+ Dependencies and their versions
+ FAQs
+ Code of Conduct

:::::::::::::::::::::::: solution 

To support the FAIR principles (Findability, Accessibility, Interoperability, and Reusability), 
certain sections in a README file are more important than others. 
Below is a breakdown of the sections that are *essential* or *optional* in a README to align with these principles. 

#### Essential

- **Purpose of the code** - clearly explains what the code does; essential for findability and reusability.
- **Installation instructions** - provides step-by-step instructions on how to install the software, ensuring accessibility.
- **Usage Example** - provides examples of how to use the code, helping users understand its functionality and enhancing reusability.
- **License**- specifies the terms under which the code can be used, which is crucial for legal clarity and reusability.
- **Dependencies and their versions** - lists the external libraries and tools required to run the code, including their versions; essential for  reproducibility and interoperability.
- **Software citation** - provides citation information for academic use, ensuring proper attribution and reusability.

#### Optional

- **Audience (who the code is intended for)** - helps users identify if the code is relevant to them, improving findability and usability.
- **How to get help** - informs users where they can get help, ensuring better accessibility.
- **Contribution guide** - encourages and guides contributions from the community, enhancing the code's development and reusability.
- **FAQs** - provide answers to common questions, aiding in troubleshooting and improving accessibility.
- **Code of Conduct** - sets expectations for behaviour in the community, fostering a welcoming environment and enhancing accessibility.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

Let's create a simple README for our repository - from VS Code or command line terminal create file `README.md` (in 
Markdown format) or `README.txt` (in plain text format).

We can start by adding a one-liner that explains the purpose of our code and who it is for.

``` code
# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.
```

Now let's add a list of Spacewalks' key features:

``` code
## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time
```

Now let's tell users about any pre-requisites required to run the software:

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

### Spacewalks README

Extend the README for Spacewalks by adding:

1. Installation instructions
2. A simple usage example

:::  solution

Installation instructions:

NB: In the solution below the back ticks of each code block have been escaped to avoid rendering issues (if you are 
copying and pasting the text, make sure you unescape them).

```text
## Installation instructions

+ Clone the Spacewalks repository to your local machine using Git.
If you don't have Git installed, you can download it from the official Git website.

\`\`\`
git clone https://github.com/your-repository-url/spacewalks.git
cd spacewalks
\`\`\`

+ Install the necessary dependencies:
\`\`\`
python3 -m pip install pandas==2.2.2 matplotlib==3.8.4 numpy==2.0.0 pytest==7.4.2
\`\`\`

+ To ensure everything is working correctly, run the tests using pytest.

\`\`\`
python3 -m pytest
\`\`\`
```

Usage instructions:

```text
## Usage Example

To run an analysis using the eva_data_analysis.py script from the command line terminal,
launch the script using Python as follows:

\`\`\`
# Usage Examples
python3 eva_data_analysis.py eva-data.json eva-data.csv
\`\`\`

The first argument is path to the JSON data file.
The second argument is the path the CSV output file.
```
::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::


### LICENSE file

Copyright allows a creator of work (such as written text, photographs, films, music, software code) to state that 
they own the work they have created. Copyright is automatically implied - even if the creator does not explicitly 
assert it, copyright of the work exists from the moment of creation. A licence is a legal document which sets down 
the terms under which the creator is releasing what they have created for others to use, modify, extend or exploit.

Because any creative work is copyrighted the moment it is created, even without any kind of licence agreement, 
it is important to state the terms under which software can be reused. 
The lack of a licence for your software implies that no one can reuse the software at all - hence it is imperative 
you declare it. A common way to declare your copyright of a piece of software and the license you are 
distributing it under is to include a file called LICENSE in the root directory of your code repository.

There is an optional extra [episode in this course on different open source software licences](../learners/licensing.md) 
that you can choose for your code and that we recommend for further reading. 

:::::: instructor
Make sure to mention the [extra content on different open source software licences](../learners/licensing.md), 
briefly cover it if there is time, then focus on the technicalities of adding a license file to a 
code repository (as there is likely not going to be enough time to spend on different license types).
::::::

:::::: callout
#### Tools to help you choose a licence

A [short intro](../learners/licensing.md) on different open source software licences included as extra content to this course. 

Check out the [open source guide](https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project) 
on applying, changing and editing licenses.

The website [choosealicense.com](https://choosealicense.com) has some great
resources to help you choose a license that is appropriate for your needs, and can even automate adding the LICENSE
file to your GitHub code repository.

:::::::


::::::  challenge

### Select a licence

Choose a license for your code. 
Discuss with your neighbour or the group your choice of license and reason for choosing it.

::::::


:::::: challenge

### Add a license to your code

Add a LICENSE file containing the full text of your chosen license to your code repository.

::: solution

1. Licence can be done in either of the following two ways:
    a. Create a LICENSE file in the root of your software repository on your local machine and copy into it 
    the text of your chosen licence (you can find it online). Push your local changes to your GitHub repository. 
    b. In your repository on GitHub, go to `Add file` option and start typing file name "LICENSE" - GitHub will
    recognise that you want to add a licence and will offer you a choice of difference licences to choose from. Select
    one and commit your changes, then do `git pull` locally to bring those changes to your machine.
2. Add a copyright statement, the name of the license you are using and a mention of the LICENSE file to at least 
one source code file (e.g. `eva_data_analysis.py`)
3. Link to your LICENSE file from README to make this information about your code more prominent.

After completing the above, check the "About" section of your repository's GitHub landing webpage and see
if there is now a license listed.


:::

::::::


### CITATION file

We can add a citation file to our repository to provide instructions on how and when to cite our code.
A citation file can be a plain text (`CITATION.txt`) or a Markdown file (`CITATION.md`), but there are 
certain benefits to use a special file format called the Citation File Format (CFF) which provides 
a way to include richer metadata about software or datasets we want to cite, making it easy
for both humans and machines to use this information.

#### Why use CFF?

For developers, using a CFF file can help to automate the process of publishing
new releases on [Zenodo][zenodo] via GitHub. 
GitHub also "understands" CFF, and will display citation information prominently on the landing page 
of a repository that contains citation info in CFF.

For users, having a CFF file makes it easy to cite the software or dataset 
with formatted citation information available for copy-paste and direct import from GitHub into reference managers like 
Zotero.

#### CFF file format

A CFF file is using the [YAML](https://yaml.org/) key-value pair format.
At a minimum a CFF file must contain the title of the software/data, the type of asset (software or data)
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

Additional and optional metadata includes an abstract, repository URL and more.

#### Creating CFF file and making your software citable

We can create (and later update) a CFF file for our software using an online application called
[`cffinit`][cffinit-webapp] by following these steps:

1. Head to [`cffinit` online tool][cffinit-webapp].
2. Then, work through the metadata input form to complete the minimum information needed to generate a CFF. 

   We can use the following description as an "Abstract":
       "A Python script to analyse NASA extravehicular activity data"
      
    Add the URL of the code repository as a "Related Resources".

    Add at least two key words under the "Keywords" section.

3. At the end of the process, download the CFF file and inspect it. It should look like this:

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
```

CFF files can also be updated using the `cffinit` online tool by pasting the previous version of CFF file and working 
through the form to update various fields.

#### Citing

To cite our software (or dataset), once a CFF file has been pushed to our remote repository,
GitHub's "Cite this repository" button can be used to generate a citation in various formats (APA, BibTeX).

::: callout

###
Further information is available from the [Turing Way's guide to software citation][turing-way-citation].

:::

:::::  challenge

### Spacewalks software citation

Add the citation file for our Spacewalks software to the root folder of our repository on GitHub.
You can either do it directly on GitHub or creating the file locally and the committing and pushing to GitHub from the 
command line.
::::::

## Documentation tools

Once our project reaches a certain size or level of complexity we may want to add
additional documentation such as a standalone tutorial or “background” explaining our methodological choices.

Once we move beyond using a README as our primary source of documentation, we need to
consider how we will distribute our documentation to our users. Options include:

- A `docs/` folder of Markdown files
- Adding a Wiki to our repository
- Creating a set of web pages for our documentation using a static site generator for our documentation such
  as Sphinx or MkDocs.

Creating a static site is a popular solution as it has the key benefit being able to
automatically generate a reference manual from any docstrings we have added to our code.

### MkDocs

Let's setup the static documentation site generator tool MkDocs.

```bash
python3 -m pip install mkdocs
python3 -m pip install "mkdocstrings[python]"
python3 -m pip install mkdocs-material
```

Let's creates a new MkDocs project in the current directory:

```bash
# In ~/Desktop/spacewalks
mkdocs new .    
```
```output
INFO    -  Writing config file: ./mkdocs.yml
INFO    -  Writing initial docs: ./docs/index.md
```

This command creates a new MkDocs project in the current directory with a `docs` folder containing an `index.md` file 
and a `mkdocs.yml` configuration file in the root of our project.

Now, let's fill in the `mkdocs.yml` configuration file for our project.

```yaml
site_name: Spacewalks Documentation
use_directory_urls: false
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

Note `font: false` variable is for GDPR compliance; `use_directory_url: false` variable tells MKDocs tools how to 
handle URLs for documentation that is served as a website (we will cover this in a moment).  

Let's add support for `mkdocstrings` - this will allow us to automatically our docstrings
into our documentation using a simple tag.

```yaml
site_name: Spacewalks Documentation
use_directory_urls: false
theme:
  name: "material"
font: false
nav:
  - Spacewalks Documentation: index.md
  - Tutorials: tutorials.md
  - How-To Guides: how-to-guides.md
  - Reference: reference.md
  - Background: explanation.md

plugins:
  - mkdocstrings

```

Let's populate our `docs/` folder to match our configuration file.

```bash
(venv_spacewalks) $ touch docs/tutorials.md
(venv_spacewalks) $ touch docs/how-to-guides.md
(venv_spacewalks) $ touch docs/reference.md
(venv_spacewalks) $ touch docs/explanation.md
```

Let's populate our reference file `reference.md` with some preamble to include
before the reference manual that will be generated from the docstrings we created.

```markdown
This file documents the key functions in the Spacewalks tool.
It is provided as a reference manual.

::: eva_data_analysis

```

Finally, let's build our documentation.

```bash
(venv_spacewalks) $ mkdocs build
```
```output
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: /Users/AnnResearcher/Desktop/Spacewalks/site
WARNING -  griffe: eva_data_analysis.py:105: No type or annotation for returned value 'int'
WARNING -  griffe: eva_data_analysis.py:84: No type or annotation for returned value 1
WARNING -  griffe: eva_data_analysis.py:33: No type or annotation for returned value 1
INFO    -  Documentation built in 0.31 seconds
```
Once the build step is completed, our documentation site is saved to 
a `site` folder in the root of our project folder.
These files will be distributed with our code. We can either direct users
to read these files locally on their own device using their browser, 
or we can choose to host our documentation as a website that our
uses can navigate to.

Note that we used the setting `use_directory_urls: false` in the `mkdocs.yml` file. This setting
ensures that the documentation site is generated with URLs that are easy to navigate
locally on a user's device.

::: challenge
### Explore your documentation

Explore documentation in `site/` folder built with MkDocs for your project, starting from `index.html` file.

For example, check `site/reference.html` to see how docstrings from your functions are 
provided here as a reference manual.
:::

Finally, let us commit our documentation to the main branch of our git repository and push the changes to GitHub.

```bash
(venv_spacewalks) $ git add mkdocs.yml 
(venv_spacewalks) $ git add docs/
(venv_spacewalks) $ git add site/
(venv_spacewalks) $ git commit -m "Add project-level documentation"
(venv_spacewalks) $ python3 -m pip freeze > requirements.txt
(venv_spacewalks) $ git add requirements.txt 
(venv_spacewalks) $ git commit -m "Added mkdocs plugin"
(venv_spacewalks) $ git push origin main
```

::::::::::::::::::::::::::::::::::::: callout
### Hosting documentation

We saw how MkDocs documentation can be distributed with our
repository and viewed "offline"  using a browser.

We can also make our documentation available as a live website by deploying our
documentation to a hosting service.

:::::: spoiler

### Some options for hosting documentation

### GitHub Pages
As our repository is hosted in GitHub, we can use GitHub Pages - a service that
allows GitHub users to host websites directly from their GitHub repositories.

There are two types of GitHub Pages: project pages and user/organization Pages.
While similar, they have different deployment workflows, and we will only discuss
project pages here. For information about deploying to user/organisational pages, see
[MkDocs Deployment pages][mkdocs-deploy].

Project Pages deploy site files to a branch (by default the `gh-pages` branch, but it can be any other branch) 
within the project repository. To deploy our documentation:

> **Warning!**
> Before we proceed to the next step, we MUST ensure that there are no uncommitted changes or untracked files in
> our repository.
>
> If there are, the commands used in the upcoming steps will include them in our documentation!

1. (If not done already), let us commit our documentation to the main branch of our git repository and push the changes to GitHub.

```bash
(venv_spacewalks) $ git add mkdocs.yml 
(venv_spacewalks) $ git add docs/
(venv_spacewalks) $ git add site/
(venv_spacewalks) $ git commit -m "Add project-level documentation"
(venv_spacewalks) $ git push origin main
```
2. Once we are on the main branch and all our changes are up to date, run the following command from the command line 
termindal to deploy our documentation to GitHub.

```bash
# Important: 
# - This command will push the documentation to the gh-pages branch of your repository
# - It will ALSO include uncommitted changes and untracked files (read the warning above!!) <- VERY IMPORTANT!!
(venv_spacewalks) $ mkdocs gh-deploy
```
```output
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: /Users/AnnResearch/Desktop/Spacewalks/site
WARNING -  griffe: eva_data_analysis.py:105: No type or annotation for returned value 'int'
WARNING -  griffe: eva_data_analysis.py:84: No type or annotation for returned value 1
WARNING -  griffe: eva_data_analysis.py:33: No type or annotation for returned value 1
INFO    -  Documentation built in 0.37 seconds
WARNING -  Version check skipped: No version specified in previous deployment.
INFO    -  Copying '/Users/AnnResearcher/Desktop/Spacewalks/site' to 'gh-pages' branch and pushing to
           GitHub.
Enumerating objects: 63, done.
Counting objects: 100% (63/63), done.
Delta compression using up to 11 threads
Compressing objects: 100% (60/60), done.
Writing objects: 100% (63/63), 578.91 KiB | 7.93 MiB/s, done.
Total 63 (delta 7), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (7/7), done.
remote: 
remote: Create a pull request for 'gh-pages' on GitHub by visiting:
remote:      https://github.com/kkh451/spacewalks/pull/new/gh-pages
remote: 
To https://github.com/kkh451/spacewalks-dev.git
 * [new branch]      gh-pages -> gh-pages
INFO    -  Your documentation should shortly be available at: https://kkh451.github.io/spacewalks/
```
This command will build our documentation with MkDocs, then commit and push the files to the `gh-pages` branch using 
the GitHub `ghp-import` tool which is installed as a dependency of MkDocs.

For more options, use:
```bash
mkdocs gh-deploy --help
```
Notice that the deploy command did not allow us to preview the site before it was pushed to GitHub; so, it is a good 
idea to check changes locally with the build commands before deploying.

### Other options
You can find out about other deployment options including free documentation hosting service ReadTheDocs on the 
[MkDocs deployment pages][mkdocs-deploy].

::::::
:::::::::::::::::::::::::::::::::::::

## Documentation guides

Once we start to consider other forms of documentation beyond the README,
we can also increase reusability of our code by ensuring that the content and style of
our documentation matches its purpose.

Documentation guides such as [Write the Docs][write-the-docs], [The Good Docs Project][the-good-docs-project] and the [Diataxis framework][diataxis-framework]
provide a range of resources including documentation templates to help to help us do this.

:::::: discussion

### Spacewalks how-to guide

a. Review the Diataxis guidance page on writing a How-to guide. Identify
three features of an effective how-to guide.

b. Following the Diataxis guidelines, add a how-to guide to the `docs/how-to-guides.md` file
in your documentation folder to show users how to change the destination filename for the output 
CSV dataset generated by the Spacewalks software.

::: spoiler
### Discussion hints & solution

An effective how-to guide should:

+ be goal oriented and focus on action.
+ avoid teaching or explanation
+ use appropriate language e.g. conditional imperatives
+ have an informative title

An example how-to guide for our project to the file `docs/how-to-guides.md`:

```
# How to change the file path of Spacewalk's output dataset

This guide shows you how to set the file path for Spacewalk's output
data set to a location of your choice.

By default, the cleaned data set in CSV format, generated by the Spacewalk software, is saved to the `results/`
folder within the working directory with file name `eva-data.csv`.

If you would like to modify the name or location of the output dataset, set the
second command line argument to your chosen file path. 
For example, if you want to save the output data set to the subfolder `data/clean/` you can 
invoke the script as:

`(venv_spacewalks) $ python3 eva_data_analysis.py eva-data.json data/clean/eva-data-clean.csv`

The specified destination folder `data/clean/` must exist before running spacewalks analysis script.
```

Remember to rebuild your documentation:

```bash
(venv_spacewalks) $ mkdocs build
```
:::

::::::

The Diataxis framework provides guidance for developing technical documentation
for different purposes. Tutorials differ in purpose and scope to how-to guides, and as a result,
differ in content and style.

::::: discussion
### Spacewalks tutorial
Let's adapt the how-to guide from the previous challenge into a tutorial that explains 
how to change the file path for the output dataset when running the analysis script.

::: spoiler 
### Solution

Here is what an example tutorial may look like. 

#### Introduction

In this tutorial, we will learn how to change the file path for the output dataset generated by the Spacewalk software.
By the end of this tutorial, you will be able to specify a custom file path for the cleaned dataset.

#### Prerequisites

Before you start, ensure you have the following:

- Python installed on your system
- The Spacewalk script (`eva_data_analysis.py`)
- An input dataset (`eva-data.json`)

####  Prepare the destination directory

First, let us decide where we want to save the cleaned dataset and make sure the directory exists.

For this tutorial, we will use `data/clean/` as the destination folder.

Let's create the directory if it does not exist - e.g. from the command line do:

```bash
(venv_spacewalks) $ mkdir -p data/clean
```

#### Run the analysis script with a custom path

Next, execute the Spacewalk script and specify the custom file path for the output dataset:
```bash
(venv_spacewalks) $ python3 eva_data_analysis.py <input-file> <output-file>
```

Replace <input-file> with your input dataset (`data/eva-data.json`) and <output-file> with your desired output path 
(`data/clean/eva-data-clean.csv`).

Here is the complete command:
```bash
(venv_spacewalks) $ python3 eva_data_analysis.py data/eva-data.json data/clean/eva-data-clean.csv
```

Notice how the output to the command line clearly indicates that we are using a custom output file path.

```output
Using custom input and output filenames
Reading JSON file data/eva-data.json
Saving to CSV file data/clean/eva-data-clean.csv
Adding crew size variable (crew_size) to dataset
Saving to CSV file data/clean/eva-data-clean.csv
Plotting cumulative spacewalk duration and saving to results/cumulative_eva_graph.png
```

After running the script, let us check the `data/clean` directory to ensure the
cleaned dataset has been saved correctly.

```bash
(venv_spacewalks) $ ls data/clean
```
You should see `eva-data-clean.csv` file listed in the `data/clean` folder.

#### Exercise: custom output path

+ Create a new directory named `output/data` in your working directory.
+ Run the Spacewalk script to save the cleaned dataset in the newly created `output/data` directory with the filename `cleaned-eva-data.csv`.
+ Verify that the dataset has been saved correctly.

##### Solution

```bash
# Create the directory:
(venv_spacewalks) $ mkdir -p output/data

# Run the script:
(venv_spacewalks) $ python3 eva_data_analysis.py data/eva-data.json output/data/cleaned-eva-data.csv

# Verify the output:
(venv_spacewalks) $ ls output/data

# You should see cleaned-eva-data.csv listed
```

Congratulations! You have successfully changed the file path for Spacewalks output dataset
and completed an exercise to practice the process. You can now customize the output location
and filename according to your needs.

:::
::::::

Now that we have seen examples of both a how-to guide and a tutorial, let's compare the two.

::::::::::::::::::::::::::::::::::::: discussion

### Tutorial vs. how-to guide

How does the content and language of our example tutorial differ from our example how-to guide?

:::::::::::::::::::::::: spoiler
### Discussion hints

#### Content

- The tutorial clearly signposts what will be covered
- The tutorial includes a narrative of each step and the expected output
- The tutorial highlights important behaviour the learner should notice
- The tutorial includes an exercise to practice skills

#### Language

- The tutorial uses the "we" language
- The tutorial uses imperative to provide clear instructions, e.g. "First do x, then do y"

:::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::



Do not forget to commit any uncommitted changes you may have and then push your work to GitHub.

```bash
(venv_spacewalks) $ git add <your_changed_files>
(venv_spacewalks) $ git commit -m "Your commit message"
(venv_spacewalks) $ git push origin main
```

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- ["The Art of Readme"][art-of-readme] article by Kira Oakley - a useful discussion of best practices for writing
  a high-quality README
- [What are best practices for research software documentation?][ssi-blog-docs] (Software Sustainability blog post) by Stephan Druskat et al.
- [Preparing Software for Reuse and Release episode][python-irsd-reuse-and-release] from the Intermediate Research Software Development lesson on The Carpentries Incubator by Aleksandra Nenadic et al.
- [CodeRefinery lesson: How to document your research software][coderefinery-documentation]
- [CITATION.cff file format][cff]
  
Also check the [full reference set](learners/reference.md#litref) for the course.


:::::::::::::::::::::::::::::::::::::::: keypoints

- Documentation allows users to run and understand software without having to work things out for themselves 
directly from the source code.
- Software documentation supports the FAIR principles by improving the reusability of research code.
- A (good) README, CITATION file and LICENSE file are the minimum documentation elements required to support FAIR 
research code.
- Documentation can be provided to users in a variety of formats including a `docs` folder of Markdown files, 
a repository Wiki and static webpages.
- A static documentation site can be created using the tool MkDocs.
- Documentation frameworks such as Diataxis provide content and style guidelines that can helps us write high 
quality documentation.

::::::::::::::::::::::::::::::::::::::::::::::::::


