---
title: "Tools and practices for research software development"
teaching: 60
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions

- What tools are available to help us develop research software in a FAIR way?
- How do the tools fit together to enable FAIR research?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Identify some key tools for FAIR research software
- Explain how can these tools help us work in a FAIR way
- Install and run these key tools on learner's machines

::::::::::::::::::::::::::::::::::::::::::::::::

In this course we will introduce you to a group of tools and practices that are commonly used in research to help you 
develop software in a FAIR way. 
You should already have these tools installed on your machine following the setup instructions. 
Here we will give an overview of the tools, how they help you achieve the aims of FAIR research software and how 
they work together. 
In later episodes we will describe some of these tools in more detail.

The table below summarises some tools and practices that can help with each of the FAIR software principles.

| Tools and practices                                                                              | Findable | Accessible | Interoperable | Reusable |
|--------------------------------------------------------------------------------------------------|----------|------------|---------------|----------|
| Integrated development environments (e.g. VS Code) - development environments (run, test, debug) |          |            |               | x        |
| Command line (e.g. Bash)- reproducible workflows/pipelines                                       |          |            | x             | x        |
| Version control tools                                                                            | x        |            |               |          |
| Testing                                                                                          |          |            |               | x        |
| Coding conventions and documentation                                                             | x        |            | x             | x        |
| License                                                                                          |          | x          |               | x        |
| Citation                                                                                         | x        |            |               | x        |
| Software repositories (e.g. GitHub)                                                              | x        | x          |               |          |


## Writing your code

### Development environment

One of the first choices we make when writing code is what tool to use to do the writing.
You can use a simple text editor such as Notepad, a terminal based editor with syntax highlighting such as Vim or Emacs, 
or one of many Integrated Development Environments (IDEs) which give you the tools to write, run and debug your code 
and inspect the output all in one place. 
Note that you should not use word processing software such as Microsoft Word or Apple Pages to write code - 
these tools are designed to create nicely formatted text for humans to read, so they may add or change formatting, 
or insert invisible characters that the programming language cannot interpret. 
Try opening a Word document in Notepad to see an example.

This is mostly a personal choice as an experienced user of any of these tools can write good, FAIR software efficiently, 
but IDEs are popular because they are designed specifically for writing and running code.
There are some language specific IDEs such as PyCharm, and some that can work with many languages like 
VS Code (Visual Studio Code). 
IDEs also have add-ons that provide extra functionality, such as checking you are code as you type 
(similar to a spell-checker in Word), highlighting when you are not following best practice, or even automatically 
generating bits of code for you.

::::::::::::::::::::::::::: instructor
At this point you could open the Python file or another file in VS Code to show all the squiggly lines suggesting 
improvements.
::::::::::::::::::::::::::::::::

In this course we will use VS Code IDE, as it is free, available on Windows, Mac and Linux operating systems, 
and can be used with many programming languages. 
It is a single tool in which we can:

- view our file system
- open many kinds of files
- edit, compile, run and debug code
- open a terminal to run command line tools (including version control tool Git) or view code outputs

Use VS Code to open the Python script and the data file from our project.

### Command line tool/shell

In VS Code and similar IDEs you can often run the code by clicking a button or pressing some keyboard shortcut.
If you gave your code to a colleague or collaborator they might use the same IDE or something different, 
so you cannot guarantee that they will have the same buttons and shortcuts as you.

In the previous episode we mentioned that interoperable software should use standard protocols so that it can 
integrate with other tools.
One of these standard protocols/tools is the command line tool or shell.
This is one of the oldest ways of interacting with computers so many programs will have command line interfaces.
Command line tools, such as Bash and Zsh, have their own language syntax that allow you to write scripts and/or 
group and chain commands together to build up complex workflows using several programs in different steps. 
They also use less resources than a graphical user interface tool like an IDE, so are commonly used on 
high-performance computers and other shared systems where time, memory and processing power are expensive or in 
high demand.

In this course we will use the Bash shell, which is one of the most common and comes already installed on Mac and Linux operating systems.
You can create a command line interface to your program which will allow it to be run on any system that has a Bash shell, and allow users to change things like input and output files or choose different settings or parameters without editing your code.
With a command line interface, your code can be built into automated workflows so that the whole process from data gathering to analysis to saving publication-quality results can be written in one Bash script and saved and reused.

### Version control

Version control means knowing what changes were made to your code and when. Many people who have worked on large documents such as essays start doing this by saving files called `essay_draft`, `essay_version1.doc`, `essay_version2.doc`, and so on. This can work on a small scale but most people find it quickly gets confusing which version a certain change was made, or which version is the one that you got feedback from a supervisor on. Using a version control system helps you keep track of changes, including when you might be working on shared code being edited by more than one person at a time.

It also lets you assign version numbers or tags to particular versions so you can then use those to refer back to them later. For example you can run your code and output some results and add a comment to your output that those results were produced by version 2.4 of your code, so if you try to run the same thing later and find it is different, you can check if it is a change in the code due to using a newer version, or a change in the data, or something else.

We will be using the Git version control system, which can be used through the command line, in a browser or in a desktop application.

### Testing

Testing ensures that your code is correct and does what it is set out to do. When you write code you often feel very confident that it is perfect, but when writing bigger codes or code that is meant to do complex operations it is very hard to consider all possible edge cases or notice every single typing mistake. Testing also gives other people confidence in your code as they can see an example of how it is meant to run and be assured that it does work correctly on their machine.

We will show different ways to test your code for different purposes. You need to think about what it is that is important to you and any future users or collaborators to decide what kind of testing is most useful for you.

### Documentation

Documentation comes in many forms - from the names of variables and functions in your code, additional comments that explain some lines, up to a whole website full of documentation in function definitions and usage, tutorials and guides. You many not need as much documentation as a large commercial software product, but making your code Reusable relies on other people being able to understand what your code does and how to use it.

### Licences and citation

A licence states what people can legally do with your code, and what restrictions you have placed on it. Whenever you want to use someone else's code you should check what license they have and make sure your use is legal. You may be restricted by your institution, your grant funding, or by other tools you use that require certain licenses for you to be compatible with them.

Having a citation guidance is not a legal requirement but if you want to get academic credit for your work you can make other people's life much easier by telling them how you would like to be credited, and making sure when you use ohers code in your research that you give them credit as they want.

Both licensing law and citation proceedures can vary depending on your country and institution, so remember to check with a local team where you are. Your local research IT or library team would be a good place to start.

### Code repositories and registries

Having somewhere to share your code is fundamental to making it Findable. Your institution might have a code repository, your research field may have a practice of sharing code in a specific website or journal, or your version control system might include an online component that makes sharing different versions of your code easy. Again, remember to check the rules of your institution and grant on publising code, and any licenses for code you depend on or reuse.

We will discuss later how to share your code on GitHub and make it easy for others to find and use.

## Summary

### Findable

- Describe your software - README
- Software repository/registry - GitHub, registries
- Unique persistent identifier - GitHub commits/tags/releases, Zenodo

### Accessible

- Software repository/registry
- License
- Language and dependencies

### Interoperable

- Explain functionality - readme, inline comments and documentation
- Standard formats
- Communication protocols - CLI/API

### Reusable

- Document functionality/installation/running
- Follow best practices where appropriate
- License
- Citation

## Checking your setup

::::::::::::::::::::::::::::::::::::: challenge

Run the following commands in a Bash shell to check you have installed the tools listed in the Setup page. Compare the output with your neightbour and see if you can see any differences.

1. `echo $SHELL`
2. `pwd`
3. `whoami`
4. `python --version`
5. `which python`
6. `git --help`
7. `code`

Solution:

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: exercise

Open a terminal and look at the prompt. Compare what you see in the terminal with your neighbour, does it look the same or different?
What information is it telling you and why might this be useful? What other information might you want?

Hint: The prompt is the `$` character and any text that comes before it, that is shown on every new line before you type in commands.

Solution:

::::::::::::::::::::::::::::::::::::::::::::::::

You may have noticed that our researcher has received the software project they are meant to be working as a `.zip` archive via email. 
In the next episode, we will learn a better practice for sharing and tracking changes to a software project using version control software Git and 
project sharing and collaboration platform GitHub.


## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- ...
- ...

Also check the [full reference set](learners/reference.md#litref) for the course.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Automating your analysis with shell scripts allows you to save and reproduce your methods.
- Version control helps you back up your work, see how data and code change over time and identify which analysis used which data and code.
- Programming languages each have advantages and disadvantages in different situations. Use the correct tools for your own work.
- Integrated development environments (IDEs) automate many coding tasks, provide easy access to documentation, and can identify common errors.
- Testing helps you check that your code is behaving as expected and will continue to do so in the future or when used by someone else.

::::::::::::::::::::::::::::::::::::::::::::::::::
