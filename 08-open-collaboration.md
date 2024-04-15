---
title: Open project collaboration & management
teaching: 60
exercises: 30
---

::::::::::::::::::::::::::::::::::::: objectives

- Explain why adding licensing information to a repository is important.
- Choose an apporpriate open source license.
- Understand that some licenses are intended for code and others for data. 
- Understand your rights and obligations under the GPL, MIT, BSD, Apache 2 and Creative Commons licenses.
- Recall that open source software can be sold and used in commercial products but that license declaration will need to be included and any other terms of the license adhered to.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: questions 

-  What licensing information should I include with my code and data?
-  How do I share my code on Github?
-  How do I ensure my code is citable?

::::::::::::::::::::::::::::::::::::::::::::::::


## What is licensing and why is it important?
Explain Copyright
What does it permit/control
What is open source/free software

Four freedoms/open source definition

1. The freedom to run the program as you wish, for any purpose.
2. The freedom to study how the program works, and change it so it does your computing as you wish. Access to the source code is a precondition for this.
3. The freedom to redistribute copies so you can help your neighbor.
4. The freedom to distribute copies of your modified versions to others. By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

Open source definition

1. Free Redistribution must be allowed
2. Source Code must be included
3. Derived Works must be allowed
4. Integrity of The Author’s Source Code - Restrict distribution of modifications if patches can be distributed instead. Must explicitly permit distribution of software built from modified source code. The license may require derived works to carry a different name or version number from the original software.
5. No Discrimination Against Persons or Groups
6. No Discrimination Against Fields of Endeavor
7. Distribution of License - License applies to anyone the software is distributed to
8. License Must Not Be Specific to a Product - the program can be extracted from other software it is distributed with
9. License Must Not Restrict Other Software, e.g. can't insist it is only distribted alongside other open source software.
10. License Must Be Technology-Neutral


## Types of licenses

### Public Domain
* No restrictions on use
* Some countries anybody can declare anything public domain
* In others you need to explicitly register it
* US Government work automatically public domain, many other countries have a default open source license, e.g. UK's Open Government Licence.
  
### Permissive Licenses

#### MIT License
#### BSD
* 2 clause
* 3 clause
* 4 clause

#### Apache 2.0

### Copyleft Licenses

* GPLv2
* GPLv3
* LGPL
* AGPL

### Tools to help you choose

* Choosealicense.com

::::::::::::::::::::::::::::::::::::: challenge

## License selection exercise

Q: choose a license for a scenario

:::::::::::::::: solution

A: 

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::


### Creative Commons Licenses
Explain code vs data/documentation licenses

* BY
* SA
* NC
* ND
* CC0

* Older CC licenses, less suitable internationally, more variants in newer versions

::::::::::::::::::::::::::::::::::::: challenge

## License selection exercise 2

Q: choose a license for a scenario involving code and data

:::::::::::::::: solution

A: 

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::


## Adding a license to your code/data

* Add a license file
* Add license statement to the top of every file


::::::::::::::::::::::::::::::::::::: challenge

## License file exercise
Q: add a license file to your git repo

:::::::::::::::: solution

A: 

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::



## Relicensing 

* License compatibility
* CC0/PD to anything
* Permissive to Copyleft

## Going commercial 
* Dual licensing
* Contributor license agreements
* Don't try to write your own

::::::::::::::::::::::::::::::::::::: challenge

## Relicensing exercise

Q: somebody has code under license X, can they relicense under Y?

:::::::::::::::: solution

A: 

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Sharing your code 
* Make code public
* Transferring to an organisation
* Archive to Zenodo
* Add a DOI
* Add a citation file
* Add a codemeta file, FAIR principles

## Pull Requests
 * show pull request workflow
 * get a helper to pull reuqest a change into a file
 * demonstrate review process

::::::::::::::::::::::::::::::::::::: challenge

## Pull Request Exercise

Q: add yourself to the authors or citation file and submit a pull request

:::::::::::::::: solution

A: 

:::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::


## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- Licencing and citation episodes from the [Software Carpentry's Git Novice lesson][swc-git-lesson]
- [Open source definition][osd-definition], by the [Open Source Initiative][osd]
- [What is free software?][free-software]

Also check the [full reference set](learners/reference.md#litref) for the course.


:::::::::::::::::::::::::::::::::::::::: keypoints

- Open source applies Copyright licenses permitting others to reuse and adapt your code or data.
- Permissive licenses
- Copyleft licenses
- Creative commons
- Open source software can be sold
- Add license file to your repo, add a license to each file in case it gets detached
- Unless you are a lawyer don't try to create your own license.

::::::::::::::::::::::::::::::::::::::::::::::::::

