---
title: Continuous Integration for automated testing
teaching: 20
exercises: 20
---

:::::::::::::::::::::::::::::::::::::: questions

- How can I automate the testing of my repository's code in a way that scales well?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

After completing this episode, participants should be able to:

- Describe the benefits of using Continuous Integration for further automation of testing
- Enable GitHub Actions Continuous Integration for public open source repositories
- Use continuous integration to automatically run unit tests and code coverage when changes are committed to a version control repository

::::::::::::::::::::::::::::::::::::::::::::::::


This extra episode should be followed after the [episode
on code correctness](08-code-correctness.md) and with [the starter code from the end of that episode](https://github.com/carpentries-incubator/astronaut-data-analysis-not-so-fair/blob/09-code-documentation/eva_data_analysis.py).

::: callout

### Activate your virtual environment
If it is not already active, make sure to activate your virtual environment from the root of
the software project directory:

```bash
$ source venv_spacewalks/bin/activate # Mac or Linux
$ source venv_spacewalks/Scripts/activate # Windows
(venv_spacewalks) $
```
:::

So far in this course, we have run our tests locally from our software's root directory using:

``` bash
$ python3 -m pytest
```

A limitation of this approach is that we must remember to run our tests
each time we make any changes. 
Continuous Integration (CI) services provide the infrastructure to
automatically run the test suite for our code every time changes are pushed to our remote code repository.
This means that each time we (or our colleagues) make a change, this will trigger the execution of the test suite
to verify that our tests still pass.

GitHub provides the Continuous Integration service called GitHub Actions for this purpose.
Before we setup GitHub Actions up, let's make sure we have committed all our latest code with tests, 
including our dependencies in `requirements.txt` which should now contain `pytest` and `pytest-cov`.

```bash
(venv_spacewalks) $ python3 -m pip freeze > requirements.txt
(venv_spacewalks) $ git add requirements.txt
(venv_spacewalks) $ git add eva_data_analysis.py tests/ 
(venv_spacewalks) $ git commit -m "Adding test suite"
(venv_spacewalks) $ git push origin main
``` 

Setting GitHub Actions on your code repository requires define the CI integration workflow `main.yml` in a new  
folder called `.github/workflows` off your project root (locally on your machine):

``` bash
(venv_spacewalks) $ mkdir -p .github/workflows
(venv_spacewalks) $ touch .github/workflows/main.yml
```

Next, populate the CI workflow file `main.yml` with GitHub Actions commands.
```yaml
name: CI

# We can specify which Github events will trigger a CI build
on: push

# now define a single job 'build' (but could define more)
jobs:

  build:

    # we can also specify the OS to run tests on
    runs-on: ubuntu-latest

    # a job is a sequence of steps
    steps:

      # Next we need to checkout our repository, and set up Python
      # A 'name' is just an optional label shown in the log - helpful to clarify progress - and can be anything
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"

      - name: Install Python dependencies
        run: |
          python3 -m pip install --upgrade pip
          python3 -m pip install -r requirements.txt

      - name: Test with PyTest
        run: |
          python3 -m pytest --cov
```

This workflow definition file instructs GitHub Actions to run our unit tests using Python version 3.12 each time code 
is pushed to our repository.

Finally, push these changes to your code repository to initiate running of tests on GitHub.

``` bash
(venv_spacewalks) $ git add .github/workflows/main.yml
(venv_spacewalks) $ git commit -m "Add GitHub actions workflow"
(venv_spacewalks) $ git push origin main
```

To check if the workflow has run, navigate to the following page in your browser: 
```         
    https://github.com/YOUR-REPOSITORY/actions
```

On the left of this page a sidebar titled "Actions" lists all the workflows that are active in our repository. 
You should see "CI" here (which is the `name` of the workflow we just added to our repository).
The body of the page lists the outcome of all historic workflow runs. 
If the workflow was triggered successfully when we pushed to the repository, you should see one workflow run listed here.


::: keypoints

- Continuous Integration can run tests automatically to verify changes as code develops in our repository.
- CI builds are typically triggered by commits pushed to a repository.
- We need to write a configuration file to inform a CI service what to do for a build.
- We can run - and get reports from - different CI infrastructure builds simultaneously.

:::
