---
title: "Tools and practices for FAIR research software development"
teaching: 60
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions

- What tools are available to help us develop research software in a FAIR way?
- How do the tools fit together to enable FAIR research?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives
After completing this episode, participants should be able to:

- Identify some key tools for FAIR research software
- Explain how can these tools help us work in a FAIR way
- Install and run these key tools on learner's machines

::::::::::::::::::::::::::::::::::::::::::::::::

In this course we will introduce you to a group of tools and practices that are commonly used in research to help you 
develop software in a FAIR way. 
You should already have these tools installed on your machine following the [setup instructions](./index.html#astronaut-data-and-analysis-code). 
Here we will give an overview of the tools, how they help you achieve the aims of FAIR research software and how 
they work together. 
In later episodes we will describe some of these tools in more detail.

### Development environments

Virtual and integrated development environments (IDEs), such as VS Code or PyCharm, help with running, testing, and debugging code.
Virtual environments further enable us to share our working environments with others, making it easier to access, reuse and extend our code.
IDEs often provide integrations with other tools, e.g. version control and command line terminals, enabling you to do many tasks from a single environment,
saving time in switching between different tools.

### Command line terminals

Command line terminals (e.g. Bash, GitBash) enable us to run and test our code without graphical user interfaces (GUI) afforded to us by IDEs -
this is sometimes needed for accessing and running our code remotely on servers and high-performance systems without a GUI provision, where time,
memory and processing power are expensive or in high demand.

Version control systems are typically provided as command line tools, making them often only accessible from command line terminals to enter commands and access
remote version control servers to backing up and sharing our work.

Finally, command line tools use standard protocols for passing parameters, inputs and outputs.
This makes it easier to integrate ours with other command line tools, allowing us to chain them and build up complex 
and reproducible workflows and analysis pipelines using several programs in different steps.
If we write our software in a way which provides such an interoperable command line interface - we will be able to 
integrate it with other command line tools to automate and speed up our work.

### Standard input/output formats and communication protocols

Using standard data exchange, input and output formats and communication protocols helps create interoperable software that can more readily integrate
with other tools into more complex pipelines - increasing its interoperability and reusability.

### Version control tools

Version control means knowing what changes were made to your code, when and by whom - promoting code ownership, responsibility and credit.
When combined with software sharing and collaborative platforms such as GitHub or GitLab, it facilitates code publication, sharing and findability,
teamwork and discussions about software and design decisions, provides backup facilities for your code and speeds up
collaboration on shared code by allowing edits by more than one person at a time.

### Code style and structure conventions

Following code style conventions for your programming language and standard code structure patterns that are agreed upon 
by the community and other programmers are important practices to ensure that others find it easy to read your code, 
reuse or extend it in their own examples and applications.

### Code testing

Testing ensures that your code is correct and does what it is set out to do.
When you write code you often feel very confident that it is perfect, but when writing bigger codes or code that is meant to do complex operations
it is very hard to consider all possible edge cases or notice every single typing mistake.
Testing also gives other people confidence in your code as they can see an example of how it is meant to run and be assured that it does work
correctly on their machine - helping with code understanding and reusability.

### Software- and project- level documentation

Documentation comes in many forms - from **software-level documentation** including docstrings describing 
functions and classes and in-line comments that explain lines of your code, to **project-level documentation** and 
**metadata** (including README, LICENCE, CITATION, CONTRIBUTING, etc. files)
that help to discover it, explain the legal terms of reusing it, describe its functionality and how to install, run and contribute to it,
to whole websites full of documentation with function definitions, usage examples, tutorials and guides.
You many not need as much documentation as a large commercial software product, but making your code reusable relies on other people being able to understand
what your code does and how to use it.

### Software repositories and registries

Having somewhere to share your code is fundamental to making it findable and accessible.
Your institution might have a code repository, your research field may have a practice of sharing code via a specific website, archive or journal,
or your version control system might include an online component that makes sharing different versions of your code easy.
You should check the rules or guidelines of your institution, grant or domain on publishing code, as well as any licenses of the code your software depends on or reuses.

Some examples of commonly used software repositories and registries include:

- general-purpose software repositories, such as [GitHub][github] and [GitLab][gitlab]
- programming language-specific software repositories, such as [PyPi][pypi] (for Python) and [CRAN][cran] (for R)
- software registries, such as [BioTools][biotools] (for biosciences) and [Awesome Research Software Registries][awesome-rs-registries] (providing a list of research software registries by country, organisation, domain and programming language) where research software can be registered to help promote its discovery

### Persistent identifiers

Unique persistent identifiers, such as Digital Object Identifiers (DOIs) provided by [Zenodo][zenodo], [FigShare][figshare] and similar digital archiving services, and commits/tags/releases used by GitHub and similar code sharing platforms,
help with findability and accessibility of your software, and can help you get credit for your work by providing citable references.

### Tools and practices summary 

The table below provides a summary of how different tools and practices help with the FAIR software principles.

| Tools and practices                                                                               | Findable | Accessible | Interoperable | Reusable |
|---------------------------------------------------------------------------------------------------| -------- | ---------- | ------------- | -------- |
| Virtual development environments                                                                  |          | x          |               | x        |
| Integrated development environments/IDEs                                                          |          |            |               | x        |
| Command line terminals - automated and reproducible pipelines                                     |          |            | x             | x        |
| Standard formats - e.g. for data exchange (CSV, YAML)                                             |          | x          | x             | x        |
| Communication protocols - Command Line Interface (CLI) or Application Programming Interface (API) |          | x          | x             | x        |
| Version control tools                                                                             | x        |            |               |          |
| Code testing and correctness                                                                      |          | x          |               | x        |
| Code style conventions                                                                            |          | x          | x             | x        |
| Software-level documentation (comments and docstrings, explaining functionality)                  |          | x          | x             | x        |
| Project-level documentation (READMEs, explaining functionality/installation/running)              |          | x          | x             | x        |
| License - code sharing and reuse                                                                  |          | x          |               | x        |
| Citation - code reuse and credit                                                                  | x        |            |               | x        |
| Software repositories and registries - code sharing                                               | x        | x          |               |          |
| Unique persistent identifiers - finding and citing software                                       | x        | x          |               |          |



## Checking your setup

Let's check your setup now to make sure you are ready for the rest of this course.

::::::  challenge

## Checking your setup

Open a command line terminal and look at the prompt. 
Compare what you see in the terminal with your neighbour, does it look the same or different?
What information is it telling you and why might this be useful? 
What other information might you want?

Run the following commands in a terminal to check you have installed the tools listed in the Setup page. 
Compare the output with your neighbour and see if you can see any differences.

Checking the command line terminal:

1. `date`
2. `echo $SHELL`
3. `pwd`
4. `whoami`

Checking Python:

5. `python --version`
6. `python3 --version`
7. `which python`
8. `which python3`

Checking Git and GitHub:

9. `git --help`
10. `git config --list`
11. `ssh -T git@github.com`

Checking VS Code:

12. `code`
13. `code --list-extensions`

::: hint

The prompt is the `$` character and any text that comes before it, that is shown on every new line before you type in 
commands.
Type each of the commands one at a time and press enter. 
They should give you a result by printing some text in the terminal.

:::

::: solution

The expected out put of each command is:

1. Today's date
2. `bash` or `zsh` - this tells you what shell language you are using. In this course we show examples in Bash.
3. Your "present working directory" or the folder where your shell is running
4. Your username
5. In this course we are using Python 3. If `python --version` gives you Python 2.x you may have two versions of Python installed on your computer and need to be careful which one you are using.
6. Use this command to be certain you are using Python version 3, not 2, if you have both installed.
7. The file path to where the Python version you are calling is installed.
8. If you have more than one version these should be different paths, if both 5. and 6. gave the same result then 7. and 8. should match as well.
9. The help message explaining how to use the `git` command.
10. You should have `user.name`, `user.email` and `core.editor` set in your Git configuration. Check that the editor listed is one you know how to use.
11. This checks if you have set up your connection to GitHub correctly. If is says `permission denied` you may need to look at the instructions for setting up SSH keys again on the Setup page.
12. This should open VSCode in your current working directory. macOS users may need to first open VS Code and [add it to the PATH](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line).
13. You should have the extensions GitLens, Git Graph, Python, JSON and Excel Viewer installed to use in this course.

:::

::::::


You may have noticed that our researcher has received the software project they are meant to be working as 
a `.zip` archive via email. 
In the next episode, we will learn a better practice for sharing and tracking changes to a software project using 
version control software Git and project sharing and collaboration platform GitHub.


## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- [CodeRefinery: Reproducible research - preparing code to be usable by you and others in the future][coderefinery-tools]
- [Python IDEs and Code Editors (Guide) - Real Python][real-python-ides]
- [The Zenodo data repository][zenodo-org]
- [The Fair Cookbook - Depositing to generic repositories - Zenodo use case][fair-cookbook-zenodo]

Also check the [full reference set](learners/reference.md#litref) for the course.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Automating your analysis with shell scripts allows you to save and reproduce your methods.
- Version control helps you back up your work, see how data and code change over time and identify which analysis used which data and code.
- Programming languages each have advantages and disadvantages in different situations. Use the correct tools for your own work.
- Integrated development environments (IDEs) automate many coding tasks, provide easy access to documentation, and can identify common errors.
- Testing helps you check that your code is behaving as expected and will continue to do so in the future or when used by someone else.

::::::::::::::::::::::::::::::::::::::::::::::::::
