---
title: Code testing
teaching: 60
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions 

- Why do we test scientific code?
- What is a unit-test?
- What makes a good unit-test?
- What are the benefits of writing unit-tests?
- What are the benefits of automating unit-tests?
- How can we ensure that our code is well-tested?
- When should we start writing tests? 
- Which parts of our code should we prioritise for testing?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Setup unit-testing framework pytest 
- Create a simple unit-test to check that a function outputs the expected value for a given set of valid inputs 
- Create a simple unit-test to check that a function raises an error when provided with invalid inputs
- Create a full test suite for a simple piece of code using a range of different assert statements
- Run a pytest test suite and interpret the results 
- Generate a code coverage report with pytest-cov and use it to identify parts of a simple piece of code that require additional tests
- Convert a bug into a failing test 
- Assess whether a piece of third-party code is suitable for reuse based on whether it includes sufficient tests

::::::::::::::::::::::::::::::::::::::::::::::::



Content of the episode goes here.


## Acknowledgements

The content of this episode was inspired / heavily borrowed from the following resources:

- ...
- ...

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- ...
- ...




:::::::::::::::::::::::::::::::::::::::: keypoints

- Formal testing of scientific code is important to demonstrate to ourselves and to our readers that our code does what is supposed to do.  
- An absence of tests makes our software risky for others to use and as a result, may reduce its impact.
- Unit tests are software tests intended to demonstrate that each component of our code e.g. individual functions work as expected. Unit tests typically contain assertions that specify how we expect our code to behave under a given set of conditions.     
- A good unit test should focus on verifying a single aspect of a function’s behaviour.  
- Unit testing has many benefits including: (i) it reduces the probability that our code contains errors and (ii) it encourages us to write readable, modular code.
- Unit tests can be automated using a unit-testing framework such e.g. Pytest for Python. Test automation allows us to add new functionality or refactor parts of our code and easily check whether it still works as expected after our changes.
- Code coverage is a metric that tells us the percentage of lines of code in our software that are run when our tests are executed.  A code coverage report can help us to identify parts of our code that may need additional tests.
- If we need to prioritise where we focus our testing efforts we should focus on the parts of our code that are “highest risk” i.e. could affect the correctness of our research findings.     


::::::::::::::::::::::::::::::::::::::::::::::::::
