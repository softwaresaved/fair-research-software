---
title: Software licensing
teaching: 20
exercises: 15
---

::::::::::::::::::::::::::::::::::::: objectives
After completing this episode, participants should be able to:

- Understand different types of open source licences and that some licenses are intended for code and others for data
  and other creative work.
- Apply an appropriate open source license to a code repository that is shared on Github.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: questions

- Why is adding licensing information to a repository important?
- What licensing information should I include with my code and data?

::::::::::::::::::::::::::::::::::::::::::::::::

## What is copyright and licensing?

Copyright allows a creator to state that they own the work (e.g. written text, photographs, films, music, software
code) they have created.
This declaration is optional - even if the creator does not explicitly assert it, copyright of the work exists from the
moment of creation.
A licence is a legal document which sets down the terms under which the creator is releasing what
they have created for others to use, modify, extend or exploit.

### What does it mean for software?

Because any creative work is copyrighted the moment it is created, even without any kind of copyright statement,
registration or license agreement, it is important to state the terms under which software can be reused.
The lack of a licence implies that no one can use the software at all.

A common way to declare your copyright of a piece of software and the license you are distributing it under is to
include a file called LICENSE in your code repository, to display it in comments at the top of a code file or to display
it on screen when the program is run.
At the very least each source file should state what license the code is under and tell the reader to refer
to the LICENSE file.
This means that if the code ever gets (accidentally) redistributed without the license file then the reader will
still know about the license that was used.

### Free software

In the early history of computing there were often informal agreements where programmers would share source code with
each other, but this was rarely backed up with any formal copyright license.
As the field grew this was first formalised in the 1980s by Richard Stallman who formed the
Free Software Foundation and defined "free software" as software which
which respects users freedoms by granting them **four freedoms**:

1. The freedom to run the program as you wish, for any purpose.
2. The freedom to study how the program works, and change it so it does your computing as you wish.
   Access to the source code is a precondition for this.
3. The freedom to redistribute copies so you can help your neighbor.
4. The freedom to distribute copies of your modified versions to others. By doing this you can give the whole
   community a chance to benefit from your changes. Access to the source code is a precondition for this.

The term "free" in English often causes some confusion here as it can mean both "free as in freedom" and 
"free as in beer" (no charge). 
The term "libre" software is sometimes used instead of "free" to help clarify this.

### Open source software

In the 1990s the "open source" movement wanted to make a more business friendly term and thought using the term "free" 
might lead to confusion when people wanted to charge for software. 
Despite "free software" often being given away for no charge (or just a small charge/suggested donation
to cover media or distribution costs), nothing in the four freedoms and the software licenses that were designed 
around it prohibits charging for software.

In 1998 the "open source definition" was created and says that software which is open source must be distributed 
under the a license which allows the following:

1. Free redistribution must be allowed
2. Source code must be included
3. Derived works must be allowed
4. Integrity of the author’s source code - there can only be restrictions on the distribution of modifications if
   patches can be distributed instead. Must explicitly permit distribution of software built from modified source code.
   The license may require derived works to carry a different name or version number from the original software.
5. No discrimination against persons or groups
6. No discrimination against fields of endeavor
7. Distribution of license - license applies to anyone the software is distributed to
8. License must not be specific to a product - the program can be extracted from other software it is distributed with
9. License must not restrict other Software, e.g. cannot insist it is only distributed alongside other open source
   software.
10. License must be technology-neutral

### Free and open source software (FOSS)

Because of these two terms many people use the term "free and open source
software" (FOSS), while others simple say "open source software" and some
will say "free software". In reality these all have very similar meanings
that will respect the four freedoms and the open source definition. For
the rest of this chapter we will refer to "open source", but could have
equally said "Free and Open Source Software" or "free software".

## Types of software licenses

What licence to choose for your research software depends on the licence of other people’s software you are including 
in your work (dependencies of your software) and also how you want this new combined work to be available to others.
In addition, it might be governed by your employer policy or funders’ mandates - your employer is 
likely to own all intellectual property over the work you produce while in employment and may influence the type of the 
licence you should use.

There are a number of licences that conform to the **four freedoms** and/or the 
[open source definition](https://opensource.com/resources/what-open-source).
Here are the most commonly used ones that will likely satisfy your needs.

### Public domain

While not strictly a licence, [public domain](https://en.wikipedia.org/wiki/Public_domain) is a concept that enables you to waive all your interests that may
exist in your work and declare your work not protected by copyright.
The [public domain](https://en.wikipedia.org/wiki/Public_domain) consists of all the creative work to which no exclusive intellectual property rights apply.
Because no one holds the exclusive rights, anyone can legally use or reference those works without permission.
Note that not having a licence is not the same as releasing your work into the public domain - the former means no one can reuse your work whereas the latter means everyone can.
For software, this may mean using an [unlicence](https://unlicense.org/) - a template for dedicating your software to the public domain.

### Permissive licences

Permissive licences impose minimal restrictions on the use and redistribution of covered software. Broadly speaking, these licences require anyone redistributing the code
to only include the licence text and a copyright statement crediting the authors.
This allows software released under these licences to also be made into part of closed source programs.

The most commonly used and popular choices of permissive licences include the [MIT licence](https://en.wikipedia.org/wiki/MIT_License),
the [BSD licences](https://en.wikipedia.org/wiki/BSD_licenses) (there are a few variants) and the [Apache 2.0 licence](https://en.wikipedia.org/wiki/Apache_License#Apache_License_2.0).

The MIT and BSD licences are very simple and generally state that anybody receiving the software can copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the software to anybody they like.
The Apache 2.0 licence is similar, but in addition includes clauses about patent licensing which require any 
contributor to a program which is licensed under Apache 2.0 to allow their patents to be used free of charge by any 
user of the software.

<!-- 
The MIT license is a very simple and popular choice of license stating that:

- Anybody receiving the software can copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software to anybody they like.
- They must include the license text and copyright statement when they redistribute it.
- There is no warranty included and you cannot hold the authors liable for any problems or damages that might arise.

The BSD license is very similar to the MIT license and has several variants. The oldest is the 4-clause version which requires:

- Source code redistributions must include the copyright statement and license text.
- Binary redistributions must include the copyright notice and license text in their documentation.
- Any advertising for the software incorporating this software must include a statement saying that it includes software written by the author.
- That the author does not endorse any derived products.
- That the author does nor provide a warranty (this is written in a separate section and is not one of the 4 clauses).

The acknowledgement/advertising clause caused some controversy and some people thought that it did not meet the open 
source definition or comply with the four freedoms. 
It also became impractical and lead to very long statements where there were multiple authors of large pieces of software.

To address this a new version of the license known as the 3-clause BSD license was created which removed 
the acknowledgement clause. An even simpler 2-clause version also exists that removes the endorsement clause.

The Apache 2.0 license is similar to the MIT and BSD licenses, but in addition includes some clauses about patent licensing. 
These require any contributor to a program which is licensed under Apache 2.0 to allow their patents to be used free 
of charge by any user of the software. 
This was done to head off some concerns about software patent legislation at the time the license was developed.
-->

### Copyleft licences

Copyleft licences are a family of open source licences that require any modifications, copies or redistributions of the original work be released under a compatible copyleft licence.
This can cause complications when combining code that is under copyleft with other licences as now the entire new codebase must be released under the copyleft licence.
If there are any incompatible terms in the other licence used  then this can prevent the two codebases from being combined.

The main advantage of copyleft licences is that anyone who incorporates the code into another product must also keep that product open and this makes it harder for it to be subsumed
into a commercial product that does not contribute improvements to the code back to the community which created it.

The most commonly known copyleft licence is the [GNU Public License or GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License) (has several versions and used by a lot of popular software including the Linux kernel).
Compared with the permissive licences, GPL is quite a long licence agreement and many of its clauses can be quite difficult for non-lawyers to fully understand.

[GNU Lesser General Public License ](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) (LGPL) - a special version of GPL -
allows developers and companies to use and integrate a software component released under the open source LGPL into their own (even proprietary) software without being required by the terms of a strong copyleft licence
to release the source code of their own components (which is the requirement of GPL). GPL requires that all its derivative works be licensed as a whole under the terms of the GPL.
If an application links to a library licensed under GPL, it must also be licensed under GPL and the source code of the application must be provided. By contrast, libraries licensed under the LGPL may be linked to proprietary applications.
If linked statically, the application code must also be released as LGPL, or everything that allows the user to re-link the application with a different version of the LGPL source code must be provided.
As long as the application is linked dynamically to LGPL software, the proprietary code can be kept proprietary.

[GNU Affero General Public License](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License) (AGPL) is designed to address the issue for GPL software running on remote web servers -
users are not receiving copies of such software on their machines but are interacting with them over computer networks and hence the person running the web server has no obligation to supply users with the source code.
The AGPL requires that people running web applications licensed under the AGPL need to make the source code of such applications available to their users.

### Creative Commons licences

All of the licences we have  discussed so far are really only intended for source code.
They are not suitable for documentation, datasets, drawings, logos, music, maps, etc. - which you may want to include as part of your software project.
To solve this problem there are the [Creative Commons (CC) licences,](https://creativecommons.org/share-your-work/cclicenses/) which are expressly built for anything other than source code.

The CC licences grant the following baseline rights:

* Attribution (BY) - all the Creative Commons licences require you to give credit to the original creator (so all will have the BY component). This is very similar to what is required by all of the permissive code licences.
* Share-Alike (SA) - requires any derivative works to be released under a compatible creative commons licence. This is very similar to the way that copyleft licences work.
* Non-Commercial (NC) - only allow for non-commercial use of the work.
* No Derivatives (ND) - users of the work cannot redistribute modified versions of it.

Combinations of various rights that are granted give us the following six Creative Commons licences:

* [CC BY](https://creativecommons.org/licenses/by/4.0/) - Creative Commons Attribution
* [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) - Creative Commons Attribution Share Alike
* [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/) - Creative Commons Non Commercial
* [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) - Creative Commons Non Commercial Share Alike
* [CC BY-ND](https://creativecommons.org/licenses/by-nd/4.0/) - Creative Commons No Derivatives
* [CC BY-ND-NC](https://creativecommons.org/licenses/by-nc-nd/4.0/) - Creative Commons No Derivatives Non Commercial

In addition to the licences above, Creative Commons also offers [CC0](https://creativecommons.org/publicdomain/zero/1.0/) - 
a public dedication tool, which enables creators to give up their copyright and put their works into the worldwide 
public domain. 

## Choosing a licence

When choosing a license for your code there is a number of things you might want to consider:

- Are you reusing code which is already under an open source licence? What obligations do you have under those licences?
- Do you want to ensure that anybody modifying and redistributing your code will release the source code of their changes?
- Do you want to ensure the least number of restrictions and that your code will be used as widely as possible? Even if that means it might end up in commercial products that do not release their source code and do not compensate you. 
- Is there a preferred license used in your research community?
- Do not be tempted to write your own licence (or modify an existing one) unless you are a copyright lawyer. 
The common open source licenses have been carefully written by copyright lawyers, many of them have undergone
multiple iterations in response to cases that have arisen and the implications of many different legal jurisdictions 
have been considered. The common licenses are also well known, meaning that potential users and contributors have a 
better understanding of what their rights and responsibilities are leaving less room for misunderstanding.
- Remember that the rights granted in a licence cannot be revoked once it has been applied.

:::::: callout
### Tools to help you choose

The website [choosealicense.com](https://choosealicense.com) has some great
resources to help you choose a license that is appropriate for your needs.
::::::

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

::::::  challenge

### Select a license

You have created a library of functions that are commonly used by
researchers in your field. You would like to share this code with your
research community and ensure that the code remains as open as possible
to benefit the community. But you would also like to see it being
integrated into as many different research codes and even commercial
products as possible. What would be a good choice of license?

:::  solution

The LGPL license could be a good choice for library code. It can be
linked to software that is not GPL licensed but any modifications to the
library itself must be released under a GPL compatible license.

:::
::::::


## Relicensing

### License compatibility

Generally, you can relicense someone else's code under more permissive
licenses to less permissive ones without their permission. For example,
you could relicense code from the MIT license to the GPL. This is because
nothing in the GPL contradicts anything in the MIT license, but you will
still have to display the MIT license for the original code and the GPL
for your modifications.

This does not work the other way though, you cannot take code released
under GPL and relicense it as MIT since MIT is a more liberal license
that does not match the terms of the GPL.

Creative Commons Zero (CC0) or public domain code can usually be relicensed to
any open source license (or a commercial license for that matter).

Sometimes there are contradictory statements in licenses which prevent
relicensing. For example, the Apache 2.0 license has some provisions about software
patents, you will not be able to relicense the Apache 2.0 code under the 
MIT license since the latter does not have an equivalent patent clause.

The GNU project has a
[useful guide on license compatibility][gnu-license-guide].

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


::::::  challenge

### Relicensing code

Find the website of a major open source project that is relevant to your research or the `Spacewalks` codebase we have 
been working with. 
See if you can find a contributor license agreement - share a link to this in the shared notes document.

::: hint
Hint: try looking at Matplotlib - https://matplotlib.org which Spacewalks uses for plotting.
:::

:::  solution

Here are a few examples:

- Python - https://www.python.org/psf/contrib/
- Scipy - https://github.com/scipy/scipy/blob/main/CONTRIBUTING.rst
- Matplotlib - https://matplotlib.org/stable/project/license.html

:::
::::::