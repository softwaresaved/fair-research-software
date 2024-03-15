---
title: "FAIR research software"
teaching: 45
exercises: 15
---

:::::::::::::::::::::::::::::::::::::: questions 

- What are FAIR research principles?
- How do FAIR principles apply to software (and data)?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Explain the FAIR research principles in the context of research software and data
- Explain why these principles are of value in the research community 

::::::::::::::::::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::: discussion

## Motivation (10 minutes)
Think about the questions below. Your trainers may ask you to share your answers in a shared notes document and/or
discuss them with other participants.

- What motivated you to attend this course? Did you come by your own choice or were you advised to attend?
- What do you hope to learn or change in your current research software practice? Describe how your knowledge, 
work or attitude may be different afterwards.
::::::::::::::::::::::::::::::::::::::::::::::::


## FAIR software

FAIR stands for Findable, Accessible, Interoperable, and Reusable and comprises a set of principles designed to
increase the visibility and usefulness of your research to others.
The FAIR data principles, first published [in 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792175/), are widely known and applied today.
Similar [FAIR principles for software](https://www.nature.com/articles/s41597-022-01710-x) have now been defined too. In general, they mean:

* **Findable** - software and its associated metadata must be easy to discover by humans and machines.
* **Accessible** - in order to reuse software, the software and its metadata must be retrievable by standard protocols.
* **Interoperable** - when interacting with other software it must be done by exchanging data and/or metadata through
  standardised protocols and application programming interfaces (APIs).
* **Reusable** - software should be usable (can be executed) and reusable
  (can be understood, modified, built upon, or incorporated into other software).

Each of the above principles can be achieved by a number of practices listed below.
This is not exact science, and by all means the list below is not exhaustive,
but any of the practices that you employ to your research software methodology will bring you
closer to the gold standard of a fully reproducible research.

* Findable
  * Create a description of your software
  * Place your software in a software repository (and ideally register it in a software registry)
  * Use a unique and persistent identifier for your software (also useful for citations)
* Accessible
  * Make sure people can freely, legally and easily get a copy your software
* Interoperable
  * Explain the functionality of your software
  * Use standard formats for inputs and outputs
  * Communicate with other software via standard protocols and APIs
* Reusable
  * Document your software (including its functionality, and how to install and run it)
  * Follow best practices for software development (including coding conventions, code readability and verifying its correctness)
  * Give a licence to your software clearly stating how it can be reused
  * State how to cite your software

We are going to explore the above practices on an example software project we will be working on as part of this
course.

::::::::::::::::::::::::::::::::::::: challenge

Think of a piece of software you use in your research - any computational tool used for data gathering, modelling & simulation, processing & visualising results or others. 
If you have a bit of code or software you wrote yourself, in any language, feel free to use that.

Do you think it is Findable, Accessible, Interoperable and Reusable? 
Give it a score from 1 to 5 in each category (1 - very bad, 2 - bad, 3 - passable, 4 - good, 5 - perfect).

::::::::::::::::::::::::::::::::::::::::::::::::

## Software and data used in this course

We are going to follow a fairly typical experience of a new PhD or postdoc joining a research group. 
They are given some data and an analysis script written by another group member who works on similar things, and they want to run this, check they understand it and then adapt it to their own project.
You should have downlaoded a CSV data file and a Python code file in the setup for this lesson.

The CSV file contains data about Extra-vehicular Activity (EVAs or spacewalks) undertaken by astronauts and cosmonauts from 1965 to 2013.

![CSV file showing the column headers (EVA #, Country, Crew, Vehicle, Date, Duration, Purpose) and first few rows](episodes/fig/Astronaut-csv-screenshot.png)

The code is a short Python script which does some common research tasks:
* Read in the data from the CSV file
* Change the data from one format to another and save to a file the new format
* Perform some calculations to generate summary statistics about the data
* Make a plot to visualise the data

![A first few lines of a Python script](episodes/fig/astronaut-analysis-bad-code-screenshot.png)

Let's think about how FAIR this piece of software is.

::::::::::::::::::::::::::::::::::::: discussion

Compare this data and code to the software you chose earler.
Do you think it is Findable, Accessible, Interoperable and Reusable? 
Give it a score from 1 (very bad) to 5 (perfect) in each category and then we will discuss it together.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: hint

Here are some questions to help you assess the FAIRness of the code:

1. **Findable**
  * If these files were emailed to you, or sent on a chat platform, or handed to you on a memory stick, how easy would it be to find them again in 6 months, or 3 years?
  * If you asked your collaborator to give you the files again later on, how would you describe them? Do they have a clear name? 
  * If more data was added to the data set later, could you explain exactly which data you used in the original analysis?
2. **Accessible**
  * If the person who gave you the files left your institution, how could you get access to the files again?
  * Do you need to log into anything to use this? Does it require purchase or subscription to a service, platform or tool?
3. **Interoperable**
  * Is it clear what kind of input data it can read and what kind of output data is produced? Will you be able to create the input files and read the output files with the tools your community generally uses? 
  * If you wanted to use this tool as part of a larger data processing pipeline, does it allow you to link it with other tools in standard ways such as an API or command-line interface?
4. **Reusable**
  * Can you run the code? What programs or libraries do you need to install to make it work (and which versions)? Are these commonly used tools in your field?
  * Do you have explicit permission to use your collaborators code in your own research and do they expect credit of some form (paper authorship, citation or acknowledgement)? Are you allowed to edit, publish or share the files with others?
  * Is the language used familiar to you and people in your research field? Can you read the variable names in the code and the column names in the data file and understand what they mean?
  * Is the code written in a way that allows you to easily modify or extend it? Can you easily see what parameters to change to make it calculate a different statistic, or run on a different input file?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: solution

I would give the following scores:
F - 1/5
  - Positive: None
  - Negative: No descriptive name, identifier or version number. No way to find again except through one person and they might not remember what file you mean.
A - 2/5
  - Positive: No accounts or paid services needed. Python is free, the data is free and under a shareable license
  - Negative: No way to get the code without that one person.  Not clear where the data comes or what license it has unless you check the URL in the comment.
I - 3/5
  - Positive: CSV and JSON files are common and well documented formats. They are machine- and human-readable. They could be generated by or fed into other programs in a pipeline.
  - Negative: JSON might not be well used in some fields. No API or CLI.
R - 2/5
  - Positive: Can ask collaborator for explicit permissions for using and modifying and how to credit them, if they did not specify before. Python is a common language.
  - Negative: Python and library versions not specified. Bad variable names, hardcoded inputs, no clear structure or documentation.

::::::::::::::::::::::::::::::::::::::::::::::::

## Acknowledgements

The content of this episode was inspired / heavily borrowed from the following resources:

- ...
- ...

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- [The FAIR Guiding Principles for scientific data management and stewardship](https://www.nature.com/articles/sdata201618)
- [The FAIR Cookbook](https://faircookbook.elixir-europe.org/content/home.html)
- [The Turing Way Guide for Reproducible Research: Open Research](https://the-turing-way.netlify.app/reproducible-research/open)
- ["10 easy things to make your research software FAIR"](https://librarycarpentry.org/Top-10-FAIR/files/poster_10things_FAIRsoftware.pdf)
- ["Five recommendations for FAIR software"](https://fair-software.eu/))



:::::::::::::::::::::::::::::::::::::::: keypoints

- Open research means the outputs of publicly funded research are publicly accessible with no or minimal restrictions.
- Reproducible research means the data and software is available to recreate the analysis.
- FAIR data and software is:
  - Findable
  - Accessible
  - Interoperable
  - Reusable
- These principles support research and researchers by saving time, reducing barriers to discovery, and increasing impact of the research output.


::::::::::::::::::::::::::::::::::::::::::::::::::
