---
title: Ethical considerations for research software
teaching: 45
exercises: 15
---

:::::::::::::::::::::::::::::::::::::: questions

- What ethical considerations are there when using and writing research software?
- How can our research software impact the rights and well-being of others?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives
After completing this episode, participants should be able to:

- Understand some ethical issues around research software development and usage and how they impact others.

::::::::::::::::::::::::::::::::::::::::::::::::


Research software development and its use (along with data it handles) does not happen in a vacuum - 
it can pose a number of ethical concerns and challenges for society and the environment, such as contributing to 
social inequality, compromising privacy and security, increasing environmental impact, and creating social and 
psychological issues. 
While these concerns do not strictly fall under
the FAIR principles, they all contribute to research software quality, reliability and responsibility.

Some of the ethical considerations around software are listed below.

### Software development practices

- Transparency: openly sharing source code and methodologies to allow for scrutiny and replication of research.
- Software quality and reliability: rigorous testing to ensure that software performs as documented and
  produces reliable results.
- Accountability: ensuring that developers are accountable for the software they create, particularly in terms of
  accuracy and reliability.

TODO: Exercise - perhaps a discussion around transparency, quality and accountability?


### Intellectual property and licensing

- Open vs closed source: balancing the benefits of open-source software and data with the rights of creators
  to protect their intellectual property and data privacy.
- License compliance: ensuring that software use complies with licensing agreements and avoiding unlicensed
- (and illegal) use of software and data.

:::::: challenge

### Which of the following statements are true and which are false?

1. I don’t need permission because I am only using the copyrighted work in educational or non-profit purposes.
2. I should always know the licence of any code, data, libraries, pictures or other work that you reuse or redistribute.
3. Since I’m planning to give credit to the authors who created the work I reuse, I do not have to worry about or need
   permission.
4. Material I obtain from the Internet is publicly accessible so no explicit permission is required.
5. The work I want to use does not have a copyright notice on it, so it’s not protected by copyright and I am free to
   use it.

::: solution

The answers are as follows:

1. False - you always need an explicit permission from the creator to use their work.
2. True - you should make sure that you have the permission for all the work that you are reusing, modifying or sharing.
3. False - if you give credit to a work’s owner, that only means you are not plagiarising other people’s work and 
claiming it as your own, however that does not mean that you have the permission to use it.
4. False - publicly accessible work is not the same the work in the public domain. The owner explicitly must put their 
work in the public domain but attaching the appropriate licence to it, before you can freely reuse it.
5. False - the use of copyright notice is optional as copyright exists implicitly from the moment the work is created.

:::

::::::


### Responsible use of software & data

- Dual use: recognizing and mitigating the potential for software to be used for harmful purposes
  (e.g. cybersecurity tools being used for hacking).
- Social impact: considering the broader social implications of software applications and data used,
  e.g. the use of data that has been collected without permission from the groups or individuals
  (e.g. historically excluded and exploited groups), or data that contains private or upsetting information.
- Bias mitigation: implement measures to detect and mitigate biases in algorithms and data,
  ensuring that the software treats all users fairly.

TODO: Exercise - perhaps some examples or discussion on algorithm or data bias.


### Environmental impact of research software

- Energy consumption: research software often relies on large-scale data centers for storage and computation,
  or the use of HPC systems and supercomputers for complex simulations and data analysis, which can significantly
  increase energy usage (much of which may come from non-renewable sources).
- Carbon footprint: the electricity used to power data centers and HPC systems contributes to CO2 emissions,
  particularly if the energy comes from fossil fuels.

TODO: Exercise: - e.g. get them to think about optimising algorithms, repeated runs of the untested code, etc.

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- ...
- ...

Also check the [full reference set](learners/reference.md#litref) for the course.


:::::::::::::::::::::::::::::::::::::::: keypoints

- Free and open source research software and data, along with FAIR, ethical and environmental considerations, 
offer viable ways to make more transparent, reliable and accountable science, allowing other research scientists to 
verify research findings.
- Building research software requires a ongoing commitment to the FAIR principles as well as engagement with
  ethical principles. By adopting these practices, researchers and developers can create software that not only advances
  scientific knowledge but also respects and protects the rights and well-being of all users.

::::::::::::::::::::::::::::::::::::::::::::::::::

