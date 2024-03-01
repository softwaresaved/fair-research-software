---
title: "Course introduction"
teaching: 30
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions 

- What is open, reproducible and FAIR research?
- Why are these practices important?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand the concept of open and reproducible research
- Understand why these principles are of value in the research community 

::::::::::::::::::::::::::::::::::::::::::::::::

## Jargon busting
Before we start with the course, below we cover the terminology and explain terms, phrases, and 
concepts associated with software development in reproducible research that we will use in this course.

* **Reproducibility** - the ability to be reproduced or copied; the extent to which consistent results are obtained 
when an experiment is repeated (definition from [Oxford Languages](https://languages.oup.com/google-dictionary-en/))
* **Computational reproducibility** - obtaining consistent results using the same input data, computational methods (code),
and conditions of analysis; work that can be independently recreated from the same data and the same code 
([definition](https://the-turing-way.netlify.app/reproducible-research/overview/overview-definitions) 
by the Turing Way's "Guide to Reproducible Research")
* **Reproducible research** - the idea that scientific results should be documented in such a way that their deduction
is fully transparent ([definition](https://en.wikipedia.org/wiki/Reproducibility) from Wikipedia)
* **Open research** - research that is openly accessible by others; concerned with making research more transparent, 
more collaborative, more wide-reaching, and more efficient 
([definition](https://en.wikipedia.org/wiki/Open_research) from Wikipedia)
* **FAIR** - an acronym that stands for Findable, Accessible, Interoperable, and Reusable
* **Sustainable software development** - software development practice that takes into account longevity and 
maintainability of code (e.g. beyond the lifetime of the project), environmental impact, societal responsibility and ethics in 
our software practices. 

::: callout
In this course, we use the term "reproducibility" as synonym for "computational reproducibility".
:::

## What is reproducible research?

[The Turing Way's "Guide to Reproducible Research"](https://the-turing-way.netlify.app/index.html#citing-the-turing-way)
provides an [excellent overview of definitions of "reproducibility" and "replicability"](https://the-turing-way.netlify.app/reproducible-research/overview/overview-definitions) found in literature, and their 
different aspects and levels. According to one definition, *reproducible* means that a measurement can be obtained 
with a stated precision by a different team using a different experimental setup in a different location on multiple 
trials (different team, different experimental setup). By the same 
definition, *replicable* means that a measurement can be obtained with stated precision by a different team 
using the same measurement procedure, the same measuring system, under the same operating conditions, 
in the same or a different location on multiple trials (different team, same experimental setup).

We can also further differentiate between:

* Computational reproducibility: when detailed information is provided about code, software, hardware and 
implementation details.
* Empirical reproducibility: when detailed information is provided about non-computational empirical scientific 
experiments and observations. In practice, this is enabled by making the data and details of how it was 
collected freely available.
* Statistical reproducibility: when detailed information is provided, for example, about the choice of 
statistical tests, model parameters, and threshold values. This mostly relates to pre-registration of study design to prevent p-value hacking and other manipulations.

In this course, we are concerned with computational reproducibility.

## Why do reproducible research?

Scientific transparency and rigor are key factors in research. Scientific methodology and 
results need to be published openly and replicated and confirmed by several independent parties.
However, research papers often lack the full details required for independent replication. 
Many attempts at replicating the results of well-known scientific studies have failed in a variety of disciplines [reference].
This is called [**the reproducibility crisis**](https://en.wikipedia.org/wiki/Replication_crisis) - an ongoing 
methodological crisis in which the results of many scientific studies are difficult or impossible to reproduce.

Reproducible research is a practice that ensures that researchers can repeat the same analysis multiple times with the 
same results. It offers many benefits to those who practice it:

* Reproducible research helps researchers remember how and why they performed specific tasks and analyses; 
this enables easier explanation of work to collaborators and reviewers. 
* Reproducible research enables researchers to quickly modify analyses and figures - this is often 
required at all stages of research and automating this process saves loads of time. 
* Reproducible research enables reusability of previously conducted tasks so that new projects 
that require the same or similar tasks become much easier and efficient by reusing or reconfiguring previous work. 
* Reproducible research has greater impact on professional lives of researchers through the 
ability to reuse and cite all research outputs - including code and data.
* Reproducible research is a strong indicator of rigor, trustworthiness, and 
transparency in scientific research. This can increase the quality and speed of peer review, because reviewers can 
directly access the analytical process described in a manuscript. It increases the probability that errors are caught 
early on - by collaborators or during the peer-review process, helping alleviate the reproducibility crisis.  

However, reproducible research often requires that researchers implement new practices and learn new tools.
This course aims to teach some of these practices and tools pertaining to the use of software to conduct 
reproducible research.

## Software in research
Software is fundamental to modern research - some of it would even be impossible without software [ssi survey reference]. 
From short, thrown-together temporary scripts to
solve a specific problem and help with day-to-day research tasks, 
through an abundance of complex spreadsheets analysing collected
data, to the hundreds of software engineers and millions of lines of code behind international
efforts such as the Large Hadron Collider and the Square Kilometre Array, there are few areas of
research where software does not have a fundamental role.

In the survey conducted by the Software Sustainability Institute in 2014 [ref], 
92% of researchers indicated they used research software [reference]. 
We define "research software" as software or code that is used to generate, process or analyse results of a research 
for publication. 
Even formulas in spreadsheets are considered code - they are a form of computer programming in that allow you to 
create, calculate, and change data sets in a number of different ways. 
So, software is not reserved for [computational science](https://en.wikipedia.org/wiki/Computational_science) 
(aka scientific computing) and “traditional” uses of computing capabilities and infrastructures (e.g.
simulations and computational methods) any more.
Nor its use is restricted to "hard" sciences - the use of research software is ubiquitous and 
fairly even across all disciplines [ssi survey ref].

Research software is also widely developed - researchers do not just use “off the shelf” software and
the majority of researchers develop their own. 
In order to be able to produce quality software that outputs correct and verifiable results and 
that can be reused over time - researchers require training.
This course teaches good practises and reproducible working methods that are agnostic of a 
programming language (although we will use Python code as examples) and aims to provide 
researchers with the tools and knowledge to feel confident when writing good quality and sustainable 
software to support their research. Typically, we think of such software as being **FAIR**.

## FAIR software

FAIR stands for Findable, Accessible, Interoperable, and Reusable and comprises a set of principles designed to 
increase the visibility and usefulness of your research to others. 
The FAIR data principles [ref] are widely known and applied today. 
Similar FAIR principles [ref] have now been defined for software too. In general, they mean: 

* **Findable** - software and its associated metadata must be easy to discover by humans and machines alike.
* **Accessible** - in order to reuse software, software and its metadata must be retrievable.
* **Interoperable** - when interacting with other software it must be done by exchanging data and/or metadata through 
standardised protocols and application programming interfaces (APIs).
* **Reusable** - software should be usable (can be executed) and reusable 
(can be understood, modified, built upon, or incorporated into other software).

Each of the above principles can be achieved by a number of practices listed below. 
This is not exact science, and by all means the list below is not exhaustive, 
but any of the practices that you employ to your research software methodology will bring you 
closer to the gold standard of a fully reproducible research.
(Also check out the following ["10 easy things to make your research software FAIR"](https://librarycarpentry.org/Top-10-FAIR/files/poster_10things_FAIRsoftware.pdf
).)

* Findable
  * Create a description of your software
  * Place your software in a software repository (and ideally register it in a software registry)
  * Use a unique and persistent identifier for your software (also useful for citations)
* Accessible
  * Make sure people can download your software
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

## Software and data used in this course
TODO

## Acknowledgements and references
The content of this episode borrows from or references the following work, which we also recommend for further reading:

[1] [A Beginner's Guide to Conducting Reproducible Research](https://esajournals.onlinelibrary.wiley.com/doi/10.1002/bes2.1801), 
Jesse M. Alston, Jessica A. Rick, https://doi.org/10.1002/bes2.1801
[2] The Turing Way "Guide for reproducible research", https://the-turing-way.netlify.app/reproducible-research/overview/overview-definitions

TODO...

[2] SSI survey
