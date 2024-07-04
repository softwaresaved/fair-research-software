---
title: "Code testing"
teaching: 60
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions 

- How can we verify that our code is correct?
- How can we automate our software tests?
- What makes a "good" test?
- Which parts of our code should we prioritize for testing?


::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives
After completing this episode, participants should be able to:

- Explain why code testing is important and how this supports FAIR software.
- Describe the different types of software tests (unit tests, integration tests, regression tests).
- Implement unit tests to verify that function(s) behave as expected using the Python testing framework `pytest`.
- Interpret the output from `pytest` to identify which function(s) are not behaving as expected. 
- Write tests using typical values, edge cases and invalid inputs to ensure that the code can handle extreme values and invalid 
inputs appropriately.
- Evaluate code coverage to identify how much of the codebase is being tested and identify areas that need further 
tests.

::::::::::::::::::::::::::::::::::::::::::::::::

## Motivation for Code Testing

The goal of software testing is to check that the actual results produced by a piece 
of code meet our expectations i.e. are correct. 

Adopting software testing as part of our research workflow helps us to conduct 
better research and produce FAIR software.

### Better Research

Software testing can help us be better, more productive researchers.  

Testing helps us to identify and fix problems with our code early and quickly and 
allows us to demonstrate to ourselves and others that our code does what we claim. 
More importantly, we can share our tests alongside our code, 
allowing others to check this for themselves. 

### FAIR Software
Software testing also underpins the FAIR process by giving us the confidence to 
engage in open research practices. 

If we are not sure that our code works as intended and produces accurate results, 
we are unlikely to feel confident about sharing our code with others.  Software testing 
brings piece of mind by providing a step-by-step approach that we can apply to verify that our code is correct. 

Software testing also supports the FAIR process by improving the 
**accessibility** and **reusability** of our code.

**Accessible**: 

+ Well written software tests capture the expected behaviour of our code and 
  can be used alongside documentation to help developers quickly make sense of our code.  

**Reusable**:

+ A well tested codebase allows developers to experiment with new features safe 
  in the knowledge that tests will reveal if their changes have broken any existing 
  functionality.   
+ The act of writing tests encourages to structure our code as individual functions and often results in a more modular, readable, maintainable 
  codebase that is easier to extend or repurpose. 


### Types of Software Tests

There are many different types of software testing including:

+ **Unit Tests**: Unit tests focus on testing individual functions in isolation. They ensure that each small part of the software performs as intended. By verifying the correctness of these individual units, we can catch errors early in the development process.

+ **Integration Tests**: Integration tests, check how different parts of the code e.g. functions work together. 

+ **Regression Tests**: Regression tests are used to ensure that new changes or updates to the codebase do not adversely affect the existing functionality. They involve checking whether a program or part of a program still generates the same results after changes have been made.

+ **End-to-end** tests are a special type of integration testing which checks that a program as a whole behaves as expected.  

In this course, our primary focus will be on unit testing. However, the concepts and techniques we cover will provide a solid foundation applicable to other types of testing. 

:::  challenge 

## Types of Software Tests

Fill in the blanks in the sentences below:

+ __________ tests compare the ______ output of a program to its ________ output
  to demonstrate correctness.
+ Unit tests compare the actual output of a ______ ________ to the expected output
  to demonstrate correctness.
+ __________ tests check that results have not changed since the previous test run.
+ __________ tests check that two or more parts of a program are working together correctly.

:::  solution 

+ End-to-end tests compare the actual output of a program to the expected output
  to demonstrate correctness.
+ Unit tests compare the actual output of a single function to the expected output
  to demonstrate correctness.
+ Regression tests check that results have not changed since the previous test run.
+ Integration tests check that two or more parts of a program are working together correctly.

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

### Informal Testing

**How should we test our code?** Let’s start by considering the following scenario. A collaborator on our project 
has sent us the following code to add a `crew_size` variable to
our data frame - a column which captures the number of astronauts participating in a given spacewalk. How do we know that it works as intended?

```python
import re
import pandas

def calculate_crew_size(crew):
    """
    Calculate crew_size for a single crew entry

    Args:
        crew (str): The text entry in the crew column

    Returns:
        int: The crew size
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew))-1


def add_crew_size_variable(df_):
    """
    Add crew size (crew_size) variable to the dataset

    Args:
        df_ (pd.DataFrame): The input data frame.

    Returns:
        df_copy (pd.DataFrame): A copy of df_ with the new crew_size variable added
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df_.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy
    
```

One approach is to copy/paste the function(s) into a python interpreter and 
check that they behave as expected with some input values where we know what
the correct return value should be. 

Since `add_crew_size_variable` contains boiler plate code for deriving 
one column from another let's start with `calculate_crew_size`:

```python
calculate_crew_size("Valentina Tereshkova;")
calculate_crew_size("Judith Resnik; Sally Ride;")
```

```output
1
2
```

We can then explore the behaviour of `add_crew_size_variable` by creating a toy
data frame:

```python
# Create a toy DataFrame
data = pd.DataFrame({
    'crew': ['Anna Lee Fisher;', 'Marsha Ivins; Helen Sharman;']
})

add_crew_size_variable(data)
```

```output
Adding crew size variable (crew_size) to dataset
                           crew  crew_size
0              Anna Lee Fisher;          1
1  Marsha Ivins; Helen Sharman;          2
```

Although this is an important process to go through as we draft our code for
the first time, there are some serious drawbacks to this approach if used as our only
form of testing.

::::::::::::::::::::::::::::::::::::: discussion 

## What are the limitations of informally testing code? (5 minutes)
Think about the questions below. Your instructors may ask you to share your answers in a shared notes document and/or discuss them with other participants.

- Why might we choose to test our code informally?
- What are the limitations of relying solely on informal tests to verify that a piece of code is behaving as expected?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: spoiler 

## Discussion Spoilers

It can be tempting to test our code informally because this approach:

+ is quick and easy
+ provides immediate feedback

However, there are limitations to this approach: 

+ Working interactively is error prone
+ We must repeat our tests every time we update our code; this is time consuming
+ We must rely on memory to keep track of how we have tested our code e.g. what input values we tried
+ We must rely on memory to keep track of which functions have been tested and which have not

:::::::::::::::::::::::::::::::::

## Formal Testing

We can overcome some of these limitations by formalising our testing process. 
A formal approach to testing our function(s) is to write dedicated test functions 
to check our code. These test functions: 

+ Run the function we want to test - the target function with known inputs
+ Compare the output to known, valid results
+ Raises an error if the function’s actual output does not match the expected output 
+ Are recorded in a test script that can be re-run on demand.

Let’s explore this process by writing some formal tests for our `text_to_duration` function. 
(We'll come back to our colleague's calculate_crew_size function later).

The `text_to_duration` function converts a duration stored as a string (HH:MM) 
to a duration in hours e.g. duration "1.15" should return a value of 1.25.  

```python
def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        float: The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60
    return duration_hours
```

Let's create a new python file `test_code.py` in the root of
our project folder to store our tests.

```bash
cd Spacewalks
touch test_code.py
```

First, we import text_to_duration into our test script. 
Then, we then add our first test function: 
```python

from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    input_value = "10:00"
    test_result = text_to_duration("10:00") == 10
    print(f"text_to_duration('10:00') == 10? {test_result}")

test_text_to_duration()

```

This test checks that when we apply text_to_duration to input value "10:00", 
the output matches the expected value of 10.

In this example, we use a print statement to report whether the actual output 
from text_to_duration meets our expectations.

However, this does not meet our requirement to “Raise an error if the function’s output does not match the expected output” 
and means that we must carefully read our test function’s output to identify whether it has failed. 

To ensure that our code raises an error if the function’s output does not match the expected output, 
we can use an assert statement.

The assert statement in Python checks whether a condition is True or False. 
If the statement is True, then assert does not return a value
but if the statement is false, then assert raises an AssertError.

Let's rewrite our test with an assert statement:
```python

from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

test_text_to_duration_integer()
```

Notice that when we run test_text_to_duration_integer(), nothing happens - there is no output. That is because
our function is working correctly and returning the expected value of 10.

Let’s see what happens when we deliberately introduce a bug into `text_to_duration`:
In  the Spacewalks data analysis script let's change `int(hours)`
to `int(hour)/60` and `int(minutes)/60` to `int(minutes)`to mimic a simple mistake in our code
where the wrong element is divided by 60.

```python
def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours)/60 + int(minutes) # Divide the wrong element by 60
    return duration_hours
```

Notice that this time, our test fails noisily.  Our assert statement has raised an
`AssertionError` -  a clear signal that there is a problem in our code that we need to fix.

```python
test_text_to_duration_integer()
```

```error
Traceback (most recent call last):
  File "/Users/AnnResearchers/Desktop/Spacewalks/test_code.py", line 7, in <module>
    test_text_to_duration_integer()
  File "/Users/AnnResearchers/Desktop/Spacewalks/test_code.py", line 5, in test_text_to_duration_integer
    assert text_to_duration("10:00") == 10
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

What happens if we add another test to our test script? This time we'll check that our function can handle durations with a non-zero
minute component. Notice that this time our expected value is a floating-point number. Importantly, we cannot use a simple double equals sign  (`==`) to compare the equality of floating-point numbers. Floating-point arithmetic can introduce very small differences due to how computers represent these numbers internally - as a result, we check that our floating point numbers are equal within a very small tolerance (1e-5). 

```python
from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10
    
def test_text_to_duration_float():
    assert abs(text_to_duration("10:20") - 10.33333333) < 1e-5

test_text_to_duration_integer()
test_text_to_duration_float()
```
```output
Traceback (most recent call last):
  File "/Users/AnnResearcher/Desktop/Spacewalks/test_code.py", line 9, in <module>
    test_text_to_duration_integer()
  File "/Users/AnnResearcher/Desktop/Spacewalks/test_code.py", line 4, in test_text_to_duration_integer
    assert text_to_duration("10:00") == 10
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
What happens when we run our updated test script? 
Our script stops after the first test failure and the second test is not run. 
To run our remaining tests we would have to manually comment out our failing test and re-run the test script. As our code base and tests grow, this will become cumbersome.
This is not ideal and can be overcome by automating our tests using a testing framework. 

## Using a Testing Framework

Our approach so far has had two major limitations:

+	We had to carefully examine the output of our test script to work out if our test failed. 
+ Our test script only ran our tests up to the first test failure. 

We can do better than this! Testing frameworks can automatically find all the tests in our code base, run all of them and present the test results as a readable summary.

We will use the python testing framework pytest with its code coverage
plugin pytest-cov. To install these libraries, open a terminal and type:

``` bash
python -m pip install pytest pytest-cov
```

Let’s make sure that our tests are ready to work with pytest.

+ pytest automatically discovers tests based on specific naming patterns. 
  pytest looks for files that start with `test_` or end with `_test.py`. 
  Then, within these files, pytest looks for functions that start with test_.  
  Our test file already meets these requirements, so there is nothing to do here.
  However, our script does contain lines to run each of our test functions. 
  These are no-longer required as pytest will run our tests so we will remove them:
  
  ```python
  # Delete
  test_text_to_duration_integer()
  test_text_to_duration_float()
  ```
  
+ It is also conventional when working with a testing framework to place test files 
  in a tests directory at the root of  our  project and to name each test file 
  after the code file that it targets. 
  This helps in maintaining a clean structure and makes it easier for others to understand where the tests are located.

A set of tests for a given piece of code is called a test suite. 
Our test suite is currently located in the root folder of our project. 
Let’s move it to a dedicated test folder and rename our test_code.py file to test_eva_analysis.py.

```bash
mkdir tests
mv test_code.py tests/test_eva_analysis.py
```

Before we re-run our tests using pytest, let's update our second test.
to use pytest's `approx` function which is specifically intended for
comparing floating point numbers within a tolerance.

```python
import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10
    
def test_text_to_duration_float():
    assert text_to_duration("10:20") == pytest.approx(10.33333333)
```

Let's also add some inline comments to clarify what each test is doing and
expand our syntax to highlight the logic behind our approach:

```python
import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations 
    """
    actual_result =  text_to_duration("10:00")
    expected_result = 10
    assert actual_result == expected_result
    
def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    actual_result = text_to_duration("10:20") 
    expected_result = 10.33333333
    assert actual_result == pytest.approx(expected_result)
```

Writing our tests this way highlights the key idea that each test should
compare the actual results returned by our function with expected values.

Similarly, writing inline comments for our tests that complete the sentence
"Test that ..." helps us to understand what each test is doing and why it is needed.

Finally, let's also modify our bug to something that will affect durations with
a non-zero minute component like "10:20" but not those that are whole hours e.g. "10:00".

Let's change `int(hours)/60 + int(minutes)` to `int(hours) + int(minutes)/6`
a simple typo.

```python
def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/6 # Divide by 6 instead of 60
    return duration_hours
```

Finally, let's run our tests:

```bash
python -m pytest 
```

```output
========================================================== test session starts 
platform darwin -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/AnnResearcher/Desktop/Spacewalks
plugins: cov-5.0.0
collected 2 items                                                                                                                        

tests/test_eva_data_analysis.py .F                                                                                                 [100%]

================================================================ FAILURES 
______________________________________________________ test_text_to_duration_float 

    def test_text_to_duration_float():
        """
        Test that text_to_duration returns expected ground truth values
        for typical durations with a non-zero minute component
        """
        actual_result = text_to_duration("10:20")
        expected_result = 10.33333333
>       assert actual_result == pytest.approx(expected_result)
E       assert 13.333333333333334 == 10.33333333 ± 1.0e-05
E         
E         comparison failed
E         Obtained: 13.333333333333334
E         Expected: 10.33333333 ± 1.0e-05

tests/test_eva_data_analysis.py:23: AssertionError
======================================================== short test summary info 
FAILED tests/test_eva_data_analysis.py::test_text_to_duration_float - assert 13.333333333333334 == 10.33333333 ± 1.0e-05
====================================================== 1 failed, 1 passed in 0.32s

```

+ Notice how if the test function finishes without triggering an assertion, 
  the test is considered successful and is marked with a dot ('.'). 
+ If an assertion fails or an error occurs, the test is marked as a failure with an 'F'. 
  and the output includes details about the error to help identify what went wrong.

:::  challenge 

## Interpreting pytest output

A colleague has asked you to conduct a pre-publication
review of their code `Spacetravel` which analyses  time spent in space by
various individual astronauts.

Inspect the pytest output provided and answer the questions below.

### pytest output for `Spacetravel`

```output
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

a. How many tests has our colleague included in the test suite?
b. The first test in test_prepare.py has a status of s; what does this mean?
c. How many tests failed?
d. Why did "test_total_duration" fail?
e. Why did "test_mean_duration" fail?

:::  solution 

a. 9 tests were detected in the test suite
b. s - stands for "skipped", 
c. 2 tests failed: the first and second tests in test file `test_analyse.py` 
d. `test_total_duration` failed because the calculated total duration differs from
   the expected value by a factor of 10 i.e. the assertion `actual == pytest.approx(expected)`
   evaluated to `False`
e. `test_mean_duration` failed because there is a syntax error in `calculate_mean_duration`.
   Our colleague has used the command `length` (not a python command) instead of `len`. As a result,
   running the function returns a `NameError` rather than a calculated value and the
   test assertion evaluates to `False`. 

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::


## Test Suite Design

Now that we have tooling in place to automatically run our test suite. What makes a good test suite?


### Good Tests

We should aim to test that our function behaves as expected with the full range of inputs that  it might encounter. It is helpful to consider each argument of a function in turn and identify the range of typical values it can take. Once we have identified this typical range or ranges (where a function takes more than one argument), we should:   

+ Test at least one interior point
+ Test all values at the edge of the range
+ Test invalid values 

Let's revisit the `crew_size` functions from our colleague's codebase.
First let's add the the additional functions to `eva_data_analysis.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt
import sys
import re

...

def calculate_crew_size(crew):
    """
    Calculate crew_size for a single crew entry

    Args:
        crew (str): The text entry in the crew column

    Returns:
        int: The crew size
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew))-1


def add_crew_size_variable(df_):
    """
    Add crew size (crew_size) variable to the dataset

    Args:
        df_ (pd.DataFrame): The input data frame.

    Returns:
        df_copy (pd.DataFrame): A copy of df_ with the new crew_size variable added
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df_.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy

if __name__ == '__main__':

    if len(sys.argv) < 3:
        input_file = './eva-data.json'
        output_file = './eva-data.csv'
        print(f'Using default input and output filenames')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        print('Using custom input and output filenames')

    graph_file = './cumulative_eva_graph.png'

    eva_data = read_json_to_dataframe(input_file)

    eva_data_prepared = add_crew_size_variable(eva_data)  # Add this line

    write_dataframe_to_csv(eva_data_prepared, output_file)  # Modify this line

    plot_cumulative_time_in_space(eva_data_prepared, graph_file) # Modify this line

    print("--END--")
```

Now, let's write some tests for `calculate_crew_size`.

:::  challenge 

## Unit Tests for calculate_crew_size

Implement unit tests for the `calculate_crew_size` function. 
Cover typical cases and edge cases.

Hint: use the following template:

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

:::  solution 

```python
import pytest
from eva_data_analysis import (
    text_to_duration,
    calculate_crew_size
)

def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations
    """
    actual_result =  text_to_duration("10:00")
    expected_result = 10
    assert actual_result == expected_result

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    actual_result = text_to_duration("10:20")
    expected_result = 10.33333333
    assert actual_result == pytest.approx(expected_result)

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
```output
========================================================== test session starts 
platform darwin -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/AnnResearcher/Desktop/Spacewalks
plugins: cov-5.0.0
collected 4 items                                                                                                                        

tests/test_eva_data_analysis.py .F..                                                                                               [100%]

================================================================ FAILURES 
______________________________________________________ test_text_to_duration_float 

    def test_text_to_duration_float():
        """
        Test that text_to_duration returns expected ground truth values
        for typical durations with a non-zero minute component
        """
        actual_result = text_to_duration("10:20")
        expected_result = 10.33333333
>       assert actual_result == pytest.approx(expected_result)
E       assert 13.333333333333334 == 10.33333333 ± 1.0e-05
E         
E         comparison failed
E         Obtained: 13.333333333333334
E         Expected: 10.33333333 ± 1.0e-05

tests/test_eva_data_analysis.py:23: AssertionError
======================================================== short test summary info 
FAILED tests/test_eva_data_analysis.py::test_text_to_duration_float - assert 13.333333333333334 == 10.33333333 ± 1.0e-05
====================================================== 1 failed, 3 passed in 0.33s 

```
:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::


### Enough Tests

In this episode, so far we've (only) written tests for two individual functions
`text_to_duration` and `calculate_crew_size`.

We can quantify the proportion of our code base that is run (also referred to as "exercised") by a given test suite using a metric called code coverage:

$$ \text{Line Coverage} = \left( \frac{\text{Number of Executed Lines}}{\text{Total Number of Executable Lines}} \right) \times 100 $$

We can calculate our test coverage using the pytest-cov library. Before we do so, let's fix our bug so that our output is cleaner and 
we can focus on the code coverage information.

```python
def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60 # Bug-free line
    return duration_hours
```

``` bash
python -m pytest --cov 
```
```output
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

To get an in-depth report about which parts of our code are tested and which are not, we 
can add the option ` --cov-report=html`.

``` bash
python -m pytest --cov --cov-report=html 
```

This option generates a folder `htmlcov` which contains a html code coverage report.
This provides structured information about our test coverage including (a)
a table showing the proportion of lines in each function that are currently tested (b) an annotated
copy of our code where untested lines are highlighted in red.

Ideally, all the lines of code in our code base should be exercised by at
least one test. However, if we lack the time and resources to test every line
of our code we should:

+ Avoid testing Python's built-in functions or functions imported from 
  well-known and well-test libraries like Pandas or numpy.
+ Focus on the the parts of our code that carry the greatest "reputational risk"
  i.e. that could affect the accuracy of our reported results.

One the other hand, it is also important to realise that althought coverage of 
less than 100% indicates that more testing may be helpful, test coverage of 100%
does not mean that our code is bug-free!

:::  challenge 

## Evaluating Code Coverage

Generate a code coverage report for the `Spacewalks` test suite
and extract the following information:

a.  What proportion of the code base is currently NOT exercised by the test suite?
b.	Which functions in our code base are currently untested?

:::  solution 

```bash
python -m pytest --cov --cov-report=html
```

a. The proportion of the code base NOT covered by our tests is `100 - 32%` = 68%
b. The following functions in our code base are currently untested:
    + read_json_to_dataframe
    + write_dataframe_to_csv
    + add_duration_hours_variable
    + plot_cumulative_time_in_space
    + add_crew_size_variable
:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::



### Implementing a minimal test suite

A member of our research team shares the following code
with us to add to the Spacewalks codebase:

```python
def summarise_categorical(df_, varname_):
    """
    Tabulate the distribution of a categorical variable

    Args:
        df_ (pd.DataFrame): The input dataframe.
        varname_ (str): The name of the variable

    Returns:
        pd.DataFrame: dataframe containing the count and percentage of
        each unique value of varname_
        
    Examples:
        >>> df_example  = pd.DataFrame({
            'vehicle': ['Apollo 16', 'Apollo 17', 'Apollo 17'],
            }, index=[0, 1, 2)
        >>> summarise_categorical(df_example, "vehicle")
        Tabulating distribution of categorical variable vehicle
             vehicle  count  percentage
        0  Apollo 16      1        33.0
        1  Apollo 17      2        67.0
    """
    print(f'Tabulating distribution of categorical variable {varname_}')

    # Prepare statistical summary
    count_variable = df_[[varname_]].copy()
    count_summary = count_variable.value_counts()
    percentage_summary = round(count_summary / count_variable.size, 2) * 100

    # Combine results into a summary data frame
    df_summary = pd.concat([count_summary, percentage_summary], axis=1)
    df_summary.columns = ['count', 'percentage']
    df_summary.sort_index(inplace=True)


    df_summary = df_summary.reset_index()
    return df_summary
```

This looks like a useful tool for creating summary statistics tables, so
let's integrate this into our `eva_data_analysis.py`code  and then 
write a minimal test suite to check that this code is behaving as expected. 

```python
import pandas as pd
import matplotlib.pyplot as plt
import sys
import re


...

def add_crew_size_variable(df_):
    """
    Add crew size (crew_size) variable to the dataset

    Args:
        df_ (pd.DataFrame): The input dataframe.

    Returns:
        pd.DataFrame: A copy of df_ with the new crew_size variable added
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df_.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy


def summarise_categorical(df_, varname_):
    """
    Tabulate the distribution of a categorical variable

    Args:
        df_ (pd.DataFrame): The input dataframe.
        varname_ (str): The name of the variable

    Returns:
        pd.DataFrame: dataframe containing the count and percentage of
        each unique value of varname_
    """
    print(f'Tabulating distribution of categorical variable {varname_}')

    # Prepare statistical summary
    count_variable = df_[[varname_]].copy()
    count_summary = count_variable.value_counts() # There is a bug here that we will fix later!
    percentage_summary = round(count_summary / count_variable.size, 2) * 100

    # Combine results into a summary data frame
    df_summary = pd.concat([count_summary, percentage_summary], axis=1)
    df_summary.columns = ['count', 'percentage']
    df_summary.sort_index(inplace=True)


    df_summary = df_summary.reset_index()
    return df_summary


if __name__ == '__main__':

    if len(sys.argv) < 3:
        input_file = './eva-data.json'
        output_file = './eva-data.csv'
        print(f'Using default input and output filenames')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        print('Using custom input and output filenames')

    graph_file = './cumulative_eva_graph.png'

    eva_data = read_json_to_dataframe(input_file)

    eva_data_prepared = add_crew_size_variable(eva_data)

    write_dataframe_to_csv(eva_data_prepared, output_file)

    table_crew_size = summarise_categorical(eva_data_prepared, "crew_size")

    write_dataframe_to_csv(table_crew_size, "./table_crew_size.csv")

    plot_cumulative_time_in_space(eva_data_prepared, graph_file)

    print("--END--")
```

To write tests for this function, we'll need to be able to compare dataframes.
The pandas.testing module in the pandas library provides functions and 
utilities for testing pandas objects and includes a function `assert_frame_equal`
that we can use to compare two dataframes.


::::::  challenge

### Exercise 1 - Typical Inputs

First, check that the function behaves as expected with 
typical input values. Fill in the gaps in the skeleton test below:

```python
import pandas.testing as pdt

def test_summarise_categorical_typical():
    """
    Test that summarise_categorical correctly tabulates
    distribution of values (counts, percentages) for a ground truth
    example (typical values)
    """
    test_input = pd.DataFrame({
        'country': _________________________________________, # FIX-ME
    }, index=[0, 1, 2, 3, 4])

    expected_result = pd.DataFrame({
        'country': ["Russia", "USA"],
        'count': [2, 3],
        'percentage': [40.0, 60.0],
    }, index=[0, 1])

    actual_result = ____________________________________________ # FIX-ME 
    
    pdt.__________________(actual_result, _______________) #FIX-ME

```

:::  solution 

```python
import pandas.testing as pdt

def test_summarise_categorical():
    """
    Test that summarise_categorical correctly tabulates
    distribution of values (counts, percentages) for a simple ground truth
    example
    """
    test_input = pd.DataFrame({
        'country': ['USA', 'USA', 'USA', "Russia", "Russia"],
    }, index=[0, 1, 2, 3, 4])

    expected_result = pd.DataFrame({
        'country': ["Russia", "USA"],
        'count': [2, 3],
        'percentage': [40.0, 60.0],
    }, index=[0, 1])

    actual_result = summarise_categorical(test_input, "country")

    pdt.assert_frame_equal(actual_result, expected_result)
```

:::
::::::

::::::  challenge

### Exercise 2 - Edge Cases

Now let's check that the function behaves as expected with edge cases.  
Does the code behave as expected when the column of interest contains one 
or more missing values (pd.NA)? (write a new test). 

Fill in the gaps in the skeleton test below:

```python
import pandas.testing as pdt

def test_summarise_categorical_missvals():
    """
    Test that summarise_categorical correctly tabulates
    distribution of values (counts, percentages) for a ground truth
    example (edge case where all column contains missing values)
    """
    test_input = _______________
    _______________
    _______________ # FIX-ME
    
    expected_result = _______________
    _______________
    _______________ # FIX-ME
    
    actual_result = summarise_categorical(test_input, "country")

    pdt.assert_frame_equal(actual_result, expected_result)
```    


:::  solution

```python
import pandas.testing as pdt

def test_summarise_categorical_missvals():
    """
    Test that summarise_categorical correctly tabulates
    distribution of values (counts, percentages) for a ground truth
    example (edge case where column contains missing values)
    """
    test_input = pd.DataFrame({
        'country': ['USA', 'USA', 'USA', "Russia", pd.NA],
    }, index=[0, 1, 2, 3, 4])

    expected_result = pd.DataFrame({
        'country': ["Russia", "USA", pd.NA],
        'count': [1, 3, 1],
        'percentage': [20.0, 60.0, 20.0],
    }, index=[0, 1])
    actual_result = summarise_categorical(test_input, "country")

    pdt.assert_frame_equal(actual_result, expected_result)
``` 

:::
:::::::    

::::::  challenge

### Exercise 3 - Invalid inputs

Now write a test to check that the `summarise_categorical` function raises an appropriate error 
when asked to tabulate a column that does not exist in the data frame.

Hint: lookup `pytest.raises` in the pytest documentation.

:::  solution 

```python

def test_summarise_categorical_invalid():
    """
    Test that summarise_categorical raises an
    error when a non-existent column is input
    """
    test_input = pd.DataFrame({
        'country': ['USA', 'USA', 'USA', "Russia", "Russia"],
    }, index=[0, 1, 2, 3, 4])

    with pytest.raises(KeyError):
        summarise_categorical(test_input, "vehicle")
```

:::
:::::: 


## Improving Our Code

At the end of this episode, our test suite in `tests` should look like this:

```python
import pytest
from eva_data_analysis import (
    text_to_duration,
    calculate_crew_size
)

def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations
    """
    actual_result =  text_to_duration("10:00")
    expected_result = 10
    assert actual_result == expected_result

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """
    actual_result = text_to_duration("10:20")
    expected_result = 10.33333333
    assert actual_result == pytest.approx(expected_result)

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


def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns expected ground truth values
    for edge case where crew is an empty string
    """
    actual_result = calculate_crew_size("")
    assert actual_result is None


def test_summarise_categorical():
    """
    Test that summarise_categorical correctly tabulates
    distribution of values (counts, percentages) for a simple ground truth
    example
    """
    test_input = pd.DataFrame({
        'country': ['USA', 'USA', 'USA', "Russia", "Russia"],
    }, index=[0, 1, 2, 3, 4])

    expected_result = pd.DataFrame({
        'country': ["Russia", "USA"],
        'count': [2, 3],
        'percentage': [40.0, 60.0],
    }, index=[0, 1])

    actual_result = summarise_categorical(test_input, "country")

    pdt.assert_frame_equal(actual_result, expected_result)


def test_summarise_categorical_missvals():
    """
    Test that summarise_categorical correctly tabulates
    distribution of values (counts, percentages) for a ground truth
    example (edge case where column contains missing values)
    """
    test_input = pd.DataFrame({
        'country': ['USA', 'USA', 'USA', "Russia", pd.NA],
    }, index=[0, 1, 2, 3, 4])

    expected_result = pd.DataFrame({
        'country': ["Russia", "USA", pd.NA],
        'count': [1, 3, 1],
        'percentage': [20.0, 60.0, 20.0],
    }, index=[0, 1])
    actual_result = summarise_categorical(test_input, "country")

    pdt.assert_frame_equal(actual_result, expected_result)
    


def test_summarise_categorical_invalid():
    """
    Test that summarise_categorical raises an
    error when a non-existent column is input
    """
    test_input = pd.DataFrame({
        'country': ['USA', 'USA', 'USA', "Russia", "Russia"],
    }, index=[0, 1, 2, 3, 4])

    with pytest.raises(KeyError):
        summarise_categorical(test_input, "vehicle")
```

Finally lets commit our test suite to our codebase and push the changes to GitHub.

```bash
git add eva_data_analysis.py 
git commit -m "Add additional analysis functions"
git add tests/
git commit -m "Add test suite"
git push origin main
```

## Continuous Integration (Optional)

:::::::::::::::::::::::::::::::::::::::::  callout
### Continuous Integration 

So far, we have run our tests locally using.

```bash
python -m pytest
```

A limitation of this approach is that we must remember to run our tests each time 
we make any changes.   

Continuous integration services provide the infrastructure to automatically run a  
code's test suite every time changes are pushed to a remote repository. 

This means that each time we (or our colleagues) push to the remote, 
the test suite will be run  to verify that our tests still pass.

If we are using GitHub, we can use the continuous integration service GitHub Actions 
to automatically run our tests.

To setup this up:

+ Navigate to the spacewalks folder:
```bash
cd ~/Desktop/Spacewalks
```

+ To setup continuous integration on GitHub actions, the dependencies of
  our code must be recorded in a `requirements.txt` file in the root of our repository.
+ You can find out more about creating requirements.txt files from 
  CodeRefinery's tutorial on "Recording Dependencies". 
+ For now, add the following list of code dependencies to requirements.txt in the root
  of the spacewalks repository:
  
```bash
touch requirements.txt
```

Content of `requirements.txt`:
```output
numpy
pandas
matplotlib
pytest
pytest-cov
```

+ Commit the changes to your repository:
```bash
git add requirements.txt
git commit -m "Add requirements.txt file"
```

Now let's define out continuous integration workflow:

+ Create a hidden folder .github/workflows
```bash
mkdir -p .github/workflows
touch .github/workflows/main.yml
```

+ Define the continuous integration workflow to run on GitHub actions.
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

    # Next we need to checkout out repository, and set up Python
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

This workflow definition file instructs GitHub Actions to run our unit tests 
using python version 3.12  each time code is pushed to our repository,

+ Let's push these changes to our repository and see if the tests are run on GitHub.

```bash
git add .github/workflows/main.yml
git commit -m "Add GitHub actions workflow"
git push origin main
```

+ To find out if the workflow has run, navigate to the following page in your browser:
```
https://github.com/YOUR-REPOSITORY/actions
```
+ On the left of this page a sidebar titled "Actions" lists all the workflows that are active in
  our repository. You should "CI" here (the `name` of the workflow we just added to our repository ).
+ The body of the page lists the outcome of all historic workflow runs. If the
  workflow was triggered successfully when we pushed to the repository, you should see one
  workflow run listed here.

::::::::::::::::::::::::::::::::::::::::: 


### Summary

During this episode, we have covered how to use software tests to
verify the correctness of our code. We have seen how to write a unit test,
how to manage and run our tests using the pytest framework and how identify which parts of our code
require additional testing using test coverage reports.

These skills reduce the probability that there will be a "mistake in our code"
and support reproducible research by giving us the confidence to engage in open
research practices. Tests also document the intended behaviour of our code 
for other developers and mean that we can experiment with changes to our code knowing
that our tests will let us know if we break any existing functionality.
In other words, software testing suppors FAIR software by making our code more
Accessible and Reusable.

To find out more about this topic, please see the "Further reading" section below.


## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- [The Defensive Programming episode][python-novice-defensive] from the Software Carpentry Python Programming lesson
- [Using Python to double check your work][ssi-blog-python-check] (Software Sustainability Blog Post) by Peter Inglesby 
- [The Python Testing and Continuous Integration][incubator-python-testing] lesson on The Carpentries Incubator by François Michonneau
- [Test Driven Development][[york-tdd-blog] (University of York Research Coding Club Blog Post) by Peter Hill and Stephen Biggs-Fox 
- [Automated testing - Preventing yourself and others from breaking your functioning code][coderefinery-testing] Coderefinery lesson
- [The Automatically Testing Software episode][python-irsd-automated-testing] from the Intermediate Research Software Development lesson on The Carpentries Incubator by Aleksandra Nenadic et al.


Also check the [full reference set](learners/reference.md#litref) for the course.


:::::::::::::::::::::::::::::::::::::::: keypoints

1. Code testing supports the FAIR principles by improving the accessibility and re-usability of research code.
2. Unit testing is crucial as it ensures each functions works correctly.
3. Using the `pytest` framework, you can write basic unit tests for Python functions to verify their correctness.
4. Identifying and handling edge cases in unit tests is essential to ensure your code performs correctly under a variety of conditions.
5. Test coverage can help you to identify parts of your code that require additional testing.



::::::::::::::::::::::::::::::::::::::::::::::::::
