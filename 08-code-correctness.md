---
title: "Code correctness"
teaching: 60
exercises: 30
---

::: questions

-   How can we verify that our code is correct?
-   How can we automate our software tests?
-   What makes a "good" test?
-   Which parts of our code should we prioritise for testing?

:::

::: objectives

After completing this episode, participants should be able to:

-   Explain why code testing is important and how this supports FAIR software.
-   Describe the different types of software tests (unit tests, integration tests, regression tests).
-   Implement unit tests to verify that function behave as expected using the Python testing framework `pytest`.
-   Interpret the output from `pytest` to identify which functions are not behaving as expected.
-   Write tests using typical values, edge cases and invalid inputs to ensure that the code can handle extreme 
values and invalid inputs appropriately.
-   Evaluate code coverage to identify how much of the codebase is being tested and identify areas that need further 
tests.

:::

Now that we have improved the structure and readability of our code - it is much easier to 
test its functionality and improve it further. 
The goal of software testing is to check that the actual results
produced by a piece of code meet our expectations, i.e. are correct.

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

:::::: instructor

At this point, the code in your local software project's directory should be as in:
https://github.com/carpentries-incubator/astronaut-data-analysis-not-so-fair/tree/08-code-correctness.

::::::

## Why use software testing?

Adopting software testing as part of our research workflow helps us to
conduct **better research** and produce **FAIR software**:

- Software testing can help us be more productive as it helps us to identify and fix problems with our code early and
  quickly and allows us to demonstrate to ourselves and others that our
  code does what we claim. More importantly, we can share our tests
  alongside our code, allowing others to verify our software for themselves.
- The act of writing tests encourages to structure our code as individual functions and often results in a more
  **readable**, modular and maintainable codebase that is easier to extend or repurpose.
- Software testing improves the **accessibility** and **reusability** of our code - well-written software tests
  capture the expected behaviour of our code and can be used alongside documentation to help other developers
  quickly make sense of our code. In addition, a well tested codebase allows developers to experiment with new
  features safe in the knowledge that tests will reveal if their changes have broken any existing functionality.
- Software testing underpins the FAIR process by giving us the
  confidence to engage in open research practices - if we are not sure that our code works as intended and produces accurate
  results, we are unlikely to feel confident about sharing our code with
  others. Software testing brings piece of mind by providing a
  step-by-step approach that we can apply to verify that our code is
  correct.


## Types of software tests

There are many different types of software testing.

-   **Unit tests** focus on testing individual functions in
    isolation. They ensure that each small part of the software performs
    as intended. By verifying the correctness of these individual units,
    we can catch errors early in the development process.

-   **Integration tests** check how different parts
    of the code e.g. functions work together.

-   **Regression tests** are used to ensure that new
    changes or updates to the codebase do not adversely affect the
    existing functionality. They involve checking whether a program or
    part of a program still generates the same results after changes
    have been made.

-   **End-to-end** tests are a special type of integration testing which
    checks that a program as a whole behaves as expected.

In this course, our primary focus will be on unit testing. However, the
concepts and techniques we cover will provide a solid foundation
applicable to other types of testing.

::: challenge
### Types of software tests

Fill in the blanks in the sentences below:

-   \_\_\_\_\_\_\_\_\_\_ tests compare the \_\_\_\_\_\_ output of a
    program to its \_\_\_\_\_\_\_\_ output to demonstrate correctness.
-   Unit tests compare the actual output of a \_\_\_\_\_\_
    \_\_\_\_\_\_\_\_ to the expected output to demonstrate correctness.
-   \_\_\_\_\_\_\_\_\_\_ tests check that results have not changed since
    the previous test run.
-   \_\_\_\_\_\_\_\_\_\_ tests check that two or more parts of a program
    are working together correctly.

::: solution
-   End-to-end tests compare the actual output of a program to the
    expected output to demonstrate correctness.
-   Unit tests compare the actual output of a single function to the
    expected output to demonstrate correctness.
-   Regression tests check that results have not changed since the
    previous test run.
-   Integration tests check that two or more parts of a program are
    working together correctly.
:::
:::

## Informal testing

How should we test our code? 
One approach is to copy/paste the code or a function into a Python terminal (different from a command line terminal), 
which allows you to interact with the Python interpreter more directly.  
From the Python terminal we can then run one function or a piece of code at a time and check that they behave as 
expected. 
As input to our code/function we are testing, we typically use some input values for which we know what the correct 
return value should be.

Let's do this for our `text_to_duration` function.
Recall that the `text_to_duration` function converts a spacewalk duration stored as a string
in format "HH:MM" to a duration in hours - e.g. duration `01:15` (1 hour and 15 minutes) should return a numerical 
value of `1.25`.

```python
def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration_hours (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/6
    return duration_hours
```

To start a Python terminal, you simply type `python3` (with no other parameters) from the root directory of your 
project in a command line terminal.

```bash
(venv_spacewalks)$ python3
```

This will open an interactive Python terminal for you, which may look like this:

```python
(venv_spacewalks) mbassan2@C-U-LOSXQ677L astronaut-data-analysis % python3
Python 3.11.7 (main, Dec  4 2023, 18:10:11) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Once inside the Python terminal, you can start typing Python code.
The Python terminal will interactively run your code and return and print results.
We could copy and paste the code of our `text_to_duration` function, but it is much simpler and more elegant 
to import and then invoke it.

```python
>>> from eva_data_analysis import text_to_duration
>>> text_to_duration("10:00")
10.0
```

So, we have invoked our function with the value "10:00" and it returned the floating point value "10.0" as expected.

We can then further explore the behaviour of our function by running:

``` python
>>> text_to_duration("00:00")
0.0
```

This all seems correct so far.

Testing code in this "informal" way in an important process to go through as we draft our code for the first time.
Another tool that can help here is the [Jupyter Notebook](https://jupyter.org/) - like the Python terminal, 
the Jupyter Notebook is an interactive environment for writing and running code. 
It is a GUI tool which supports all kinds of interactive outputs, including many interactive visualisation libraries.

However, there are some serious drawbacks to this approach if used as our only form of testing.

:::::: challenge

### What are the limitations of informally testing code? (5 minutes)

Think about the questions below. Your instructors may ask you to share
your answers in a shared notes document and/or discuss them with other
participants.

-   Why might we choose to test our code informally?
-   What are the limitations of relying solely on informal tests to
    verify that a piece of code is behaving as expected?

::: solution
### 

It can be tempting to test our code informally because this approach:

- is quick and easy
- provides immediate feedback

However, there are limitations to this approach:

- Working interactively is error prone
- We must reload our function in Python terminal each time we change our code
- We must repeat our tests every time we update our code which is time consuming
- We must rely on memory to keep track of how we have tested our code, e.g. what input values we tried
- We must rely on memory to keep track of which functions have been tested and which have not 
(informal testing may work well on smaller pieces of code but it becomes unpractical for a large codebase)
- Once we close the Python terminal, we lose all the test scenarios we have tried
:::
::::::

## Formal testing

We can overcome some of these limitations by formalising our testing process. 
A formal approach to testing our code is to write dedicated test functions to check it. 
These test functions:

-   Run the function we want to test - the target function with known inputs
-   Compare the output to known, valid results
-   Raise an error if the function’s actual output does not match the expected output
-   Are recorded in a test script that can be re-run on demand.

Let’s explore this process by writing some formal tests for our `text_to_duration` function. 

In VS Code, create a new Python file `test_code.py` in the root of our project directory to store our tests.

Like before in the Python terminal, we need to import `text_to_duration` into our test script. 
Then, we add our first test function:

``` python

from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    input_value = "10:00"
    test_result = text_to_duration("10:00") == 10
    print(f"text_to_duration('10:00') == 10? {test_result}")

test_text_to_duration_integer()
```

We can run this code from the command line terminal as:

```bash
(venv_spacewalks)$ python3 test_code.py 
```

This test checks that when we apply `text_to_duration` to input value `10:00`, the output matches the expected value
of `10`.

In this example, we use a print statement to report whether the actual output from `text_to_duration` meets our 
expectations.

However, this does not meet our requirement to “Raise an error if the function’s output does not match the expected 
output” and means that we must carefully read our test function’s output to identify whether it has failed.

To ensure that our code raises an error if the function’s output does not match the expected output, we use Python's 
`assert` statement. 
The `assert statement` in Python checks whether a condition is `True` or `False`. 
If the statement is `True`, `assert` does not return a value and the code continues to run. 
However, if the statement is `False`, `assert` raises an `AssertError`.

Let's rewrite our test with an `assert` statement:

``` python

from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

test_text_to_duration_integer()
```

Notice that when we run `test_text_to_duration_integer()`, nothing
happens - there is no output. That is because our function is working
correctly and returning the expected value of 10.

Let's add another test to check what happens when duration is not an integer number and if our function can handle 
durations with a non-zero minute component, and rerun our test code.

``` python
from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

test_text_to_duration_float()
test_text_to_duration_integer()
```

``` error
(venv_spacewalks) $ python3 test_code.py 
Traceback (most recent call last):
  File "/Users/user/Desktop/spacewalks/test_code.py", line 9, in <module>
    test_text_to_duration_float()
  File "/Users/user/Desktop/spacewalks/test_code.py", line 4, in test_text_to_duration_float
    assert text_to_duration("10:15") == 10.25
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

Notice that this time, our test `test_text_to_duration_float` fails.
Our assert statement has raised an `AssertionError` - a clear signal that there is a problem in our code that we
need to fix. 
We know that duration `10:15` should be converted to number `10.25`. 
What is wrong with our code?
If we look at our `text_to_duration` function, we may identify the following line of our code as problematic:

```python
def text_to_duration(duration):
    ...
    duration_hours = int(hours) + int(minutes)/6 
    ...
```

You may notice that our conversion code is wrong - the minutes component should have been divided by 60 and not 6.
We were able to spot this tiny bug by testing our code.

Let's fix the problematic line and rerun out tests. 

```python
...
duration_hours = int(hours) + int(minutes)/60 
...
```

This time our tests run without problem. 

Should we add more tests or the tests we have so far are enough? 
What happens if our duration value is `10:20` (ten hours and 20 minutes) and our result is not a rational floating 
point number (like `10.25`) but an irrational number such as `10.333333333`? 
Let's tests for this.

```python
from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    assert text_to_duration("10:20") == 10.333333

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

test_text_to_duration_float()
test_text_to_duration_integer()

```

```error
(venv_spacewalks) $ python3 test_code.py
Traceback (most recent call last):
  File "/Users/user/work/SSI/lessons/astronaut-data-analysis/test_code.py", line 17, in <module>
    test_text_to_duration_float()
  File "/Users/user/work/SSI/lessons/astronaut-data-analysis/test_code.py", line 9, in test_text_to_duration_float
    assert text_to_duration("10:20") == 10.333333
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

On computer systems, representation of irrational numbers is typically not exact as they do not have an exact binary 
representation.
For this reason, we cannot use a simple double equals sign (`==`) to compare the equality of floating point numbers. 
Instead, we check that our floating point numbers are equal within a very small tolerance (e.g. 1e-5).
Hence, our code should look like: 

``` python
...
def test_text_to_duration_float():
    assert abs(text_to_duration("10:20") - 10.33333333) < 1e-5
...
```

You may have noticed that we have to repeat a lot of code to add each individual test for each test case. 
You may also have noticed that our test script stopped after the first test failure and none of the tests after that 
were run. 
To run our remaining tests we would have to manually comment out our failing test and re-run the test script. 
As our code base grows, testing in this way becomes cumbersome and error-prone. 
These limitations can be overcome by automating our tests using a **testing framework**.

## Testing frameworks

Testing frameworks can automatically find all the tests in our code base, run all of them (so we do not have to invoke 
them explicitly or, even worse, forget to invoke them), and present the test results as a readable summary.

We will use the Python testing framework `pytest` with its code coverage extension `pytest-cov`. 
To install these libraries into our virtual environment, from the command line terminal do:

``` bash
(venv_spacewalks) $ python3 -m pip install pytest pytest-cov
```

Let’s make sure that our tests are ready to work with `pytest`.

-   `pytest` automatically discovers tests based on specific naming
    patterns. It looks for files that start with "test\_" or end with
    "\_test.py". Then, within these files, `pytest` looks for functions
    that start with "test_".
    Our test file already meets these requirements, so there is nothing
    to do here. However, our script does contain lines to run each of
    our test functions. These are no-longer required as pytest will run
    our tests so we can remove them:

    ``` python
    # Delete these 2 lines
    test_text_to_duration_float()
    test_text_to_duration_integer()
    ```

-   It is also conventional when working with a testing framework to
    place test files in a `tests` directory at the root of our project and
    to name each test file after the code file that it targets. This
    helps in maintaining a clean structure and makes it easier for
    others to understand where the tests are located.

A set of tests for a given piece of code is called a test suite. 
Our test suite is currently located in the root folder of our project. 
Let’s move it to a dedicated test folder and rename our `test_code.py` file to
`test_eva_analysis.py`.

You can do it from VS Code or by typing the following commands in the command line terminal:

``` bash
(venv_spacewalks) $ mkdir tests
(venv_spacewalks) $ mv test_code.py tests/test_eva_analysis.py
```

Before we re-run our tests using `pytest`, let's update our second test
to use `pytest`'s function `approx()` which is specifically intended for
comparing floating point numbers within a tolerance.

``` python
import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    assert text_to_duration("10:20") == pytest.approx(10.33333333)

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

```

Let's also add some inline comments to clarify what each test is doing
and expand our syntax to highlight the logic behind our approach:

``` python
import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    actual_result = text_to_duration("10:20") 
    expected_result = 10.33333333
    assert actual_result == pytest.approx(expected_result)
    
def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations 
    """
    actual_result =  text_to_duration("10:00")
    expected_result = 10
    assert actual_result == expected_result
    
```

Writing our tests this way highlights the key idea that each test should compare the actual results returned by our 
function with expected values.

Similarly, writing inline comments for our tests that complete the sentence "Test that ..." helps us to understand 
what each test is doing and why it is needed.

Before running out tests with `pytest`, let's reintroduce our old bug in function `text_to_duration` that affects 
the durations with a non-zero minute component like "10:20" but not those that are whole hours, e.g. "10:00":

```python
    ...
    duration_hours = int(hours) + int(minutes)/6  # Divide by 6 instead of 60
    ...
```

Finally, let's run our tests with `pytest` from our project's root directory (and not `tests` directory):

``` bash
(venv_spacewalks) $ python3 -m pytest 
```

``` error
========================================== test session starts ===========================================
platform darwin -- Python 3.11.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/user/work/SSI/lessons/astronaut-data-analysis-not-so-good
plugins: cov-5.0.0
collected 2 items                                                                                                                                                                                                                                                                                                     

tests/test_code.py F.                                                                                                                                                                                                                                                                                           [100%]

================================================ FAILURES ================================================
________________________________________ test_text_to_duration_float _____________________________________

    def test_text_to_duration_float():
>       assert text_to_duration("10:20") == pytest.approx(10.33333333)
E       assert 13.333333333333334 == 10.33333333 ± 1.0e-05
E         
E         comparison failed
E         Obtained: 13.333333333333334
E         Expected: 10.33333333 ± 1.0e-05

tests/test_code.py:5: AssertionError
=========================================== short test summary info =======================================
FAILED tests/test_code.py::test_text_to_duration_float - assert 13.333333333333334 == 10.33333333 ± 1.0e-05
========================================= 1 failed, 1 passed in 0.67s =====================================

```

From the above output from `pytest`'s execution of out tests, we notice that: 

- If a test function finishes without triggering an assertion, the test is considered successful and is marked with a
    dot (`.`).
- If an assertion fails or an error occurs, the test is marked as a failure with an `F`, 
and the output includes details about the error to help identify what went wrong.

Let's fix our bug once again, and rerun our tests using `pytest`.

```output
========================================== test session starts ===========================================
platform darwin -- Python 3.11.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/user/work/SSI/lessons/astronaut-data-analysis-not-so-good
plugins: cov-5.0.0
collected 2 items                                                                                                                                                                                                                                                                                                     

tests/test_code.py ..                                                                                                                                                                                                                                                                                           [100%]

=========================================== 2 passed in 0.63s =============================================
```

This time, all out tests passed.

::: challenge

### Interpreting pytest output

A colleague has asked you to conduct a pre-publication review of their code which analyses time spent in 
space by various individual astronauts.

You tested their code using `pytest`, and got the following output.
Inspect it and answer the questions below.

#### Example `pytest` output

``` output
============================================================ test session starts 
platform darwin -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/Desktop/AnneResearcher/projects/Spacetravel
collected 9 items                                                                                                                                                              

tests/test_analyse.py FF....                                              [ 66%]
tests/test_prepare.py s..                                                 [100%]

====================================================================== FAILURES 
____________________________________________________________ test_total_duration

    def test_total_duration():
    
      durations = [10, 15, 20, 5]
      expected  = 50/60
      actual  = calculate_total_duration(durations)
>     assert actual == pytest.approx(expected)
E     assert 8.333333333333334 == 0.8333333333333334 ± 8.3e-07
E       
E       comparison failed
E       Obtained: 8.333333333333334
E       Expected: 0.8333333333333334 ± 8.3e-07

tests/test_analyse.py:9: AssertionError
______________________________________________________________________________ test_mean_duration 

    def test_mean_duration():
       durations = [10, 15, 20, 5]
    
       expected = 12.5/60
>      actual  = calculate_mean_duration(durations)

tests/test_analyse.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

durations = [10, 15, 20, 5]

    def calculate_mean_duration(durations):
        """
        Calculate the mean of a list of durations.
        """
        total_duration = sum(durations)/60
>       mean_duration = total_duration / length(durations)
E       NameError: name 'length' is not defined

Spacetravel.py:45: NameError
=========================================================================== short test summary info 
FAILED tests/test_analyse.py::test_total_duration - assert 8.333333333333334 == 0.8333333333333334 ± 8.3e-07
FAILED tests/test_analyse.py::test_mean_duration - NameError: name 'length' is not defined
============================================================== 2 failed, 6 passed, 1 skipped in 0.02s 
```

a.  How many tests has our colleague included in the test suite?
b.  The first test in test_prepare.py has a status of s; what does this
    mean?
c.  How many tests failed?
d.  Why did "test_total_duration" fail?
e.  Why did "test_mean_duration" fail?

::: solution
a.  9 tests were detected in the test suite
b.  s - stands for "skipped",
c.  2 tests failed: the first and second tests in test file
    `test_analyse.py`
d.  `test_total_duration` failed because the calculated total duration
    differs from the expected value by a factor of 10 i.e. the assertion
    `actual == pytest.approx(expected)` evaluated to `False`
e.  `test_mean_duration` failed because there is a syntax error in
    `calculate_mean_duration`. Our colleague has used the command
    `length` (not a python command) instead of `len`. As a result,
    running the function returns a `NameError` rather than a calculated
    value and the test assertion evaluates to `False`.
:::
:::

## Test suite design

We now have the tools in place to automatically run tests. 
However, that alone is not enough to properly test code.
We will now look into what makes a good test suite and good practices for testing code.

Let’s start by considering the following scenario. 
A collaborator on our project has sent us the following code which adds a new column called `crew_size` 
to our data containing the number of astronauts participating in any given spacewalk. 
How do we know that it works as intended and that it will not break the rest of our code?
For this, we need to write a test suite with a comprehensive coverage of the new code.
 
``` python
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re # added this line

# https://data.nasa.gov/resource/eva.json (with modifications)

def main(input_file, output_file, graph_file):
    print("--START--")

    eva_data = read_json_to_dataframe(input_file)

    eva_data = add_crew_size_column(eva_data) # added this line

    write_dataframe_to_csv(eva_data, output_file)

    plot_cumulative_time_in_space(eva_data, graph_file)

    print("--END--")

... 

def calculate_crew_size(crew):
    """
    Calculate the size of the crew for a single crew entry

    Args:
        crew (str): The text entry in the crew column containing a list of crew member names

    Returns:
        int: The crew size
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew))-1

def add_crew_size_column(df):
    """
    Add crew_size column to the dataset containing the value of the crew size

    Args:
        df (pd.DataFrame): The input data frame.

    Returns:
        df_copy (pd.DataFrame): A copy of df with the new crew_size variable added
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy
...
    
```

### Writing good tests

The aim of writing good tests is to verify that each of our functions behaves as expected with the full range of inputs 
that it might encounter.
It is helpful to consider each argument of a function in turn and identify the range of typical values it can take.
Once we have identified this typical range or ranges (where a function takes more than one argument), we should:

-   Test all values at the edge of the range
-   Test at least one interior point
-   Test invalid values

Let's have a look at the `calculate_crew_size` function from our colleague's new code and write some tests for it.

:::::: challenge

### Unit tests for calculate_crew_size

Implement unit tests for the `calculate_crew_size` function. 
Cover typical cases and edge cases.

Hint - use the following template when writing tests:
```         
def test_MYFUNCTION (): # FIXME
    """
    Test that ...   #FIXME
    """
    
    # Typical value 1
    actual_result =  _______________ #FIXME
    expected_result = ______________ #FIXME
    assert actual_result == expected_result
    
    # Typical value 2
    actual_result =  _______________ #FIXME
    expected_result = ______________ #FIXME
    assert actual_result == expected_result
    
```

::: solution

We can add the following test functions to out test suite.

``` python
import pytest
from eva_data_analysis import (
    text_to_duration,
    calculate_crew_size
)

...

def test_calculate_crew_size():
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size("Valentina Tereshkova;")
    expected_result = 1
    assert actual_result == expected_result

    actual_result = calculate_crew_size("Judith Resnik; Sally Ride;")
    expected_result = 2
    assert actual_result == expected_result

# Edge cases
def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns expected ground truth values
    for edge case where crew is an empty string
    """
    actual_result = calculate_crew_size("")
    assert actual_result is None

```

Let's run out tests:

```bash
(venv_spacewalks) $ python3 -m pytest

```

:::
::::::

### Parameterising tests

Looking at out new test functions, we may notice that they do not follow the 
[“Don't Repeat Yourself principle”][dry-principle] which prevents software - including testing code - 
from becoming repetitive and too long. 
In our test code, a small block of code is repeated twice with different input values:

``` python
def test_calculate_crew_size():
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size("Valentina Tereshkova;")
    expected_result = 1
    assert actual_result == expected_result

    actual_result = calculate_crew_size("Judith Resnik; Sally Ride;")
    expected_result = 2
    assert actual_result == expected_result
```

To avoid such repetitions in our test code, we use **test parameterisation**. 
This allows us to apply our test function to a list of input/expected output pairs without the need for repetition. 
To parameterise the `test_calculate_crew_size` function, we can rewrite is as follows:

``` python
@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2),
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result
```

Notice the following key changes to our code:

- The unparameterised version of `test_calculate_crew_size` function did not have any arguments and our input/expected values 
were all defined in the body of our test function.
- In the parameterised version of `test_calculate_crew_size`, the body of our test function has been rewritten as a 
parameterised block of code that uses the variables `input_value` and `expected_result` which are now arguments of the
test function.
- A Python decorator `@pytest.mark.parametrize` is placed immediately before the test function and indicates that 
it should be run once for each set of parameters provided.

::: callout
In Python, a decorator is a function that can modify the behaviour of another function. 
`@pytest.mark.parametrize` is a decorator provided by `pytest` that modifies the behaviour of our test 
function by running it multiple times - once for each set of inputs. 
This decorator takes two main arguments:

-   Parameter names: a string with the names of the parameters that the
    test function will accept, separated by commas – in this case
    “input_value” and “expected_value”

-   Parameter values: a list of tuples, where each tuple contains the
    values for the parameters specified in the first argument.
:::

As you can see, the parameterised version of our test function is shorter, more readable and easier to maintain.


### Just enough tests

In this episode, so far we have (only) written tests for two individual functions: `text_to_duration` and 
`calculate_crew_size`.

We can quantify the proportion of our code base that is run (also referred to as "exercised") by a given test suite 
using a metric called code coverage:

$$ \text{Line Coverage} = \left( \frac{\text{Number of Executed Lines}}{\text{Total Number of Executable Lines}} \right) \times 100 $$

We can calculate our test coverage using the `pytest-cov` library as follows.

``` bash
(venv_spacewalks) $ python3 -m pytest --cov 
```

``` output
========================================================== test session starts 
platform darwin -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/AnnResearcher/Desktop/Spacewalks
plugins: cov-5.0.0
collected 4 items                                                                                                                        

tests/test_eva_data_analysis.py ....                                                                                               [100%]

---------- coverage: platform darwin, python 3.12.3-final-0 ----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
eva_data_analysis.py                 56     38    32%
tests/test_eva_data_analysis.py      20      0   100%
-----------------------------------------------------
TOTAL                                76     38    50%


=========================================================== 4 passed in 1.04s
```

To get an in-depth report about which parts of our code are tested and
which are not, we can add the option `--cov-report=html`.

``` bash
(venv_spacewalks) $ python -m pytest --cov --cov-report=html 
```

This option generates a folder `htmlcov` in the project root directory containing a code coverage report in HTML format. 
This provides structured information about our test coverage including: 

- a table showing the proportion of lines in each function that are currently tested, and 
- an annotated copy of our code where untested lines are highlighted in red.

Ideally, all the lines of code in our code base should be exercised by at least one test. 
However, if we lack the time and resources to test every line of our code we should:

- avoid testing Python's built-in functions or functions imported from well-known and well-tested libraries like 
`pandas` or `numpy`.
- focus on the the parts of our code that carry the greatest "reputational risk", i.e. that could affect the accuracy 
of our reported results.

::: callout

Test coverage of less than 100% indicates that more testing may be helpful.

Test coverage of 100% does not mean that our code is bug-free.

:::

::: challenge

### Evaluating code coverage

Generate the code coverage report for your software using the `python3 -m pytest --cov --cov-report=html` command, 
inspect it and and extract the following information:

a.  What proportion of the code base is currently "not" exercised by the test suite?
b.  Which functions in our code base are currently untested?

::: solution

a.  You can find this information on the "Files" tab of the HTML report. 
The proportion of the code base NOT covered by our tests is 68% (100% - 32%) - this may differ for your 
version of the code.
b.  You can find this information on the "Functions" tab of the HTML report. 
The following functions in our code base are currently untested:
    -   read_json_to_dataframe
    -   write_dataframe_to_csv
    -   add_duration_hours_variable
    -   plot_cumulative_time_in_space
    -   add_crew_size_variable
:::
:::

At this point, now is a good time to commit our test suite to our codebase and push the changes to GitHub.

``` bash
(venv_spacewalks) $ git add eva_data_analysis.py 
(venv_spacewalks) $ git commit -m "Add additional analysis functions"
(venv_spacewalks) $ git add tests/
(venv_spacewalks) $ git commit -m "Add test suite"
(venv_spacewalks) $ python3 -m pip freeze > requirements.txt
(venv_spacewalks) $ git add requirements.txt
(venv_spacewalks) $ git commit -m "Added pytest and pytest-cov libraries."
(venv_spacewalks) $ git push origin main
```

### (Optional) More practice with a test suite

There is an [optional exercise](../learners/test-suite-exercise.md) to implement additional tests and practice writing tests some more.

## Continuous Integration for automated testing

Continuous Integration (CI) services provide the infrastructure to automatically run every test function in 
the test code suite every time changes are pushed to a remote repository.
There is an [extra episode on configuring CI for automated tests on GitHub](../learners/ci-for-testing.md)
for some additional reading.

## Summary

During this episode, we have covered how to use software tests to verify
the correctness of our code. We have seen how to write a unit test, how
to manage and run our tests using the `pytest` framework and how identify
which parts of our code require additional testing using test coverage
reports.

These skills reduce the probability that there will be a mistake in our
code and support reproducible research by giving us the confidence to
engage in open research practices. 
Tests also document the intended behaviour of our code for other developers and mean that we can
experiment with changes to our code knowing that our tests will let us
know if we break any existing functionality. 
In other words, software testing supports the FAIR software principles by making our code more **accessible** and
**reusable**.

## Further reading

We recommend the following resources for some additional reading on the
topic of this episode:

-   [The Defensive Programming episode][python-novice-defensive] from
    the Software Carpentry Python Programming lesson
-   [Using Python to double check your work][ssi-blog-python-check]
    (Software Sustainability Blog Post) by Peter Inglesby
-   [The Python Testing and Continuous
    Integration][incubator-python-testing] lesson on The Carpentries
    Incubator by François Michonneau
-   [Test Driven Development][[york-tdd-blog] (University of York
    Research Coding Club Blog Post) by Peter Hill and Stephen Biggs-Fox
-   [Automated testing - Preventing yourself and others from breaking
    your functioning code][coderefinery-testing] Coderefinery lesson
-   [The Automatically Testing Software
    episode][python-irsd-automated-testing] from the Intermediate
    Research Software Development lesson on The Carpentries Incubator by
    Aleksandra Nenadic et al.

Also check the [full reference set](learners/reference.md#litref) for
the course.

::: keypoints

1.  Code testing supports the FAIR principles by improving the
    accessibility and re-usability of research code.
2.  Unit testing is crucial as it ensures each functions works
    correctly.
3.  Using the `pytest` framework, you can write basic unit tests for
    Python functions to verify their correctness.
4.  Identifying and handling edge cases in unit tests is essential to
    ensure your code performs correctly under a variety of conditions.
5.  Test coverage can help you to identify parts of your code that
    require additional testing.
6. 
:::
