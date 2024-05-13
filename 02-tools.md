---
title: "Tools and practices for research software development"
teaching: 60
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions 

- What tools are available to help us work in a FAIR way?
- How do the tools fit together to enable FAIR research?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Identify some key tools for FAIR research
- Install and run key tools on their own workstation
- Explain why these help us work in a FAIR way

::::::::::::::::::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::: challenge

- List the tools, platforms and standards you currently use in your research.
- Note down whether you they could be easily used or understood by:
  - Someone else in your research group
  - Another researcher in your field but from a different group
  - An untrained member of the public

::::::::::::::::::::::::::::::::::::::::::::::::






::::::::::::::::::::::::::::::::::::: challenge

Looking at the list you made earlier, give each item a mark for how:
  - Findable
  - Accessible
  - Interoperable
  - Reusable
you think they are in themselves. Do they help you work in a FAIR way?

::::::::::::::::::::::::::::::::::::::::::::::::



::::::::::::::::::::::::::::::::::::: challenge

Open a terminal and look at the prompt. Compare with oyur neighbour, does it look different?
What information is it telling you and why might this be useful?

Hint: The prompt is the `$` character and any text that comes before it, that is shown on every new line before you type in commands.

Solution:

::::::::::::::::::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::: challenge

Run the following commands to check you have installed the tools listed in the Setup page. Compare the output with your neightbour and see if you can see any differences.

1. `echo $SHELL`
2. `pwd`
3. `whoami`
4. `python --version`
5. `which python`
6. `git --help`
7. `code`

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
