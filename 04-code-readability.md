---
title: Code readability
teaching: 60
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions 

- Why does readable code matter?
- How can I organise my code to be more readable?
- What types of documentation can I include to improve the readability of my code?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives
After completing this episode, participants should be able to:

- Organise code into reusable functions that achieve a singular purpose
- Create function and variable names that help explain the purpose of the function or variable
- Write informative inline comments and docstrings to provide more detail about what the code is doing

::::::::::::::::::::::::::::::::::::::::::::::::

In this episode, we will introduce the concept of readable code and consider how it can help create reusable scientific software and empower collaboration between researchers.

### Motivation for code readability

When someone writes code, they do so based on requirements that are likely to change in the future.
Requirements change because software interacts with the real world, which is dynamic.
When these requirements change, the developer (who is not necessarily the same person who wrote the original code) must implement the new requirements.
They do this by reading the original code to understand the different abstractions, and identify what needs to change.
Readable code facilitates the reading and understanding of the abstraction phases and, as a result, facilitates the evolution of the codebase.
Readable code saves future developers' time and effort.

In order to develop readable code, we should ask ourselves: "If I re-read this piece of code in fifteen days or one year, will I be able to understand what I have done and why?"
Or even better: "If a new person who just joined the project reads my software, will they be able to understand what I have written here?"

We will now learn about a few software best practices we can follow to help create readable code.

### Variable names

Variables are the most common thing you will assign when coding, and it's really important that it is clear what each variable means in order to understand what the code is doing.
If you return to your code after a long time doing something else, or share your code with a colleague, it should be easy enough to understand what variables are involved in your code from their names.
Therefore we need to give them clear names, but we also want to keep them concise so the code stays readable.
There are no "hard and fast rules" here, and it's often a case where you will need to use your best judgment.

Some useful tips for naming variables are:

- Short words are better than single character names
  - For example, if we were creating a variable to store the speed to read a file, `s` (for 'speed') is not descriptive enough but `MBReadPerSecondAverageAfterLastFlushToLog` is too long to read and prone to mispellings.
    `ReadSpeed` (or `read_speed`) would suffice.
  - If you're finding it difficult to come up with a variable name that is _both_ short and descriptive, go with the short version and use an inline comment to desribe it further (more on those in the next section!)
  - This guidance doesn't necessarily apply if your variable is a well-known constant in your domain, for example, _c_ represents the speed of light in Physics
- Try to be descriptive where possible, and avoid names like `foo`, `bar`, `var`, `thing`, and so on

There are also some gotchas to consider when naming variables:

- There may be some restrictions on which characters you can use in your variable names.
  For instance in Python, only alphanumeric characters and underscores are permitted.
- Particularly in Python, you cannot _begin_ your variable names with numerical characters as this will raise a syntax error.
  - Numerical characters can be included in a variable name, just not as the first character.
    For example, `thing1` is a valid variable name, but `1thing` isn't.
    (This behaviour may be different for other programming languages.)
- In some programming languages, such as Python, variable names are case sensitive.
  So `speed_of_light` and `Speed_Of_Light` will **not** be equivalent.
- Programming languages often have global pre-built functions, such as `input`, which you may accidentally overwrite if you assign a variable with the same name.
  - Again in Python, you would actually reassign the `input` name and no longer be able to access the original `input` function if you used this as a variable name.
    So in this case opting for something like `input_data` would be preferable.
    (This behaviour may be explicitly disallowed in other programming languages.)

:::  challenge

### Give a descriptive name to a variable

Below we have a variable called `var` being set the value of 9.81.
`var` is not a very descriptive name here as it doesn't tell us what 9.81 means, yet it is a very common constant in physics!
Go online and find out which constant 9.81 relates to and suggest a new name for this variable.

Hint: the units are _metres per second squared_!

```python
var = 9.81
```

:::  solution

### Solution

Yes, 9.81 m/s^2 is the [gravitational force exerted by the Earth](https://en.wikipedia.org/wiki/Gravity_of_Earth).
It is often referred to as "little g" to distinguish it from "big G" which is the [Gravitational Constant](https://en.wikipedia.org/wiki/Gravitational_constant).
A more decriptive name for this variable therefore might be:

```python
g_earth = 9.81
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Inline comments

Commenting is a very useful practice to help convey the context of the code.
It can be helpful as a reminder for your future self or your collaborators as to why code is written in a certain way, how it is achieving a specific task, or the real-world implications of your code.

There are many ways to add comments to code, the most common of which is inline comments.

```python
# In Python, inline comments begin with the `#` symbol and a single space.
```

Again, there are few hard and fast rules to using comments, just apply your best judgment.
But here are a few things to keep in mind when commenting your code:

- **Avoid using comments to explain _what_ your code does.**
  If your code is too complex for other programmers to understand, consider rewriting it for clarity rather than adding comments to explain it.
- Focus on the **_why_** and the **_how_**.
- Make sure you're not reiterating something that your code already conveys on its own.
  Comments shouldn't echo your code.
- Keep them short and concise.
  Large blocks of text quickly become unreadable and difficult to maintain.
- Comments that contradict the code are worse than no comments.
  Always make a priority of keeping comments up-to-date when code changes.

#### Examples of helpful vs. unhelpful comments

##### Unhelpful:

```python
statetax = 1.0625  # Assigns the float 1.0625 to the variable 'statetax'
citytax = 1.01  # Assigns the float 1.01 to the variable 'citytax'
specialtax = 1.01  # Assigns the float 1.01 to the variable 'specialtax'
```

The comments in this code simply tell us what the code does, which is easy enough to figure out without the inline comments.

##### Helpful:

```python
statetax = 1.0625  # State sales tax rate is 6.25% through Jan. 1
citytax = 1.01  # City sales tax rate is 1% through Jan. 1
specialtax = 1.01  # Special sales tax rate is 1% through Jan. 1
```

In this case, it might not be immediately obvious what each variable represents, so the comments offer helpful, real-world context.
The date in the comment also indicates when the code might need to be updated.

:::  challenge

### Add some comments to a code block

Examine lines 7 to 20 of the `bad-code.py` script.
Add (or change!) as many inline comments as you think is required to help yourself and others understand what that code block is doing.

Hint: Inline comments in Python are denoted by a `#` symbol.

:::  solution

### Solution

Some good inline comments may look like the below example.

```python
for count in range(370):
    line = csvfile.readline().split(',')

    # Create a temporary dictionary to store data in
    l = dict()
    # For each item in the line from the CSV file, store
    # the item in the temporary dictionary
    for thing in range(len(line[:7])):
        l[fieldnames[thing]] = line[thing]

    import json
    json.dump(l, jsonfile)

    # Add a newline to the json file ready for the next entry
    jsonfile.write('\n')

jsonfile.close()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Functions

Functions are a fundamental concept in writing software and are one of the core ways you can organise your code to improve its readability.
A function is an isolated section of code that performs a single, _specific_ task that can be simple or complex.
It can then be called multiple times with different inputs throughout a codebase, but it's definition only needs to appear once.

Breaking up code into functions in this manner benefits readability since the smaller sections are easier to read and understand.
Since functions can be reused, codebases naturally begin to follow the [Don't Repeat Yourself principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) which prevents software from becoming overly long and confusing.
The software also becomes easier to maintain because, if the code encapsulated in a function needs to change, it only needs updating in one place instead of many.
As we will learn in a future episode, testing code also becomes simpler when code is written in functions.
Each function can be individually checked to ensure it is doing what is intended, which improves confidence in the software as a whole.

:::  challenge

### Create a function

Below is a function that reads in a JSON file into a dataframe structure using the [`pandas` library](https://pandas.pydata.org/) - but the code is out of order!
Reorder the lines of code within the function so that the JSON file is read in using the `read_json` method, any incomplete rows are _dropped_, the values are _sorted_ by date, and then the cleaned dataframe is _returned_.
There is also a `print` statement that will display which file is being read in on the command line for verification.

```python
import pandas as pd

def read_json_to_dataframe(input_file):
    eva_df.sort_values('date', inplace=True)
    eva_df.dropna(axis=0, inplace=True)
    print(f'Reading JSON file {input_file}')
    return eva_df
    eva_df = pd.read_json(input_file, convert_dates=['date'])
```

:::  solution

### Solution

Here is the correct order of the code for the function.

```python
import pandas as pd

def read_json_to_dataframe(input_file):
    print(f'Reading JSON file {input_file}')
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df
```

We have chosen to create a function for reading in data files since this is a very common task within research software.
While this isn't that many lines of code, thanks to using pandas inbuilt methods, it can be useful to package this together into a function if you need to read in a lot of similarly structured files and process them in the same way.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Docstrings

Docstrings are a specific type of documentation that are provided within functions, and [classes](https://docs.python.org/3/tutorial/classes.html) too.
A function docstring should explain what the isolated code is doing, what parameters the function needs (these are inputs) and what form they should take, what the function outputs (you may see words like 'returns' or 'yields' here), and errors (if any) that might be raised.

Providing these docstrings helps improve code readability since it makes the function code more transparent and aids understanding.
Particularly, docstrings that provide information on the input and output of functions makes it easier to reuse them in other parts of the code, without having to read the full function to understand what needs to be provided and what will be returned.

Docstrings are another case where there are no hard and fast rules for writing them.
Acceptable docstring formats can range from single- to multi-line.
You can use your best judgment on how much documentation a particular function needs.

#### Example of a single-line docstring:

```python
def add(x, y):
    """Add two numbers together"""
    return x + y
```

#### Example of a multi-line docstring:

```python
def add(x, y = 1.0):
    """
    Add two integers together

    Parameters
    ----------
    x         : A number to be included in the addition
    y (float) : A float number to be included in the addition. Default: 1.0.

    Returns
    -------
    float : The sum of x and y. This value will be a float type since y takes
            float type.
    """
    return x + y
```

Some projects may have their own guidelines on how to write docstrings, such as [numpy](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard).
If you are contributing code to a wider project or community, try to follow the guidelines and standards they provide for codestyle.

As your code grows and becomes more complex, the docstrings can form the content of a reference guide allowing developers to quickly look up how to use the APIs, functions, and classes defined in your codebase.
Hence, it is common to find tools that will automatically extract docstrings from your code and generate a website where people can learn about your code without downloading/installing and reading the code files - such as [sphinx for Python](https://www.sphinx-doc.org/en/master/tutorial/automatic-doc-generation.html).

:::  challenge

### Writing docstrings

Write a docstring for the `read_json_to_dataframe` function from the previous
exercise. Things you may want to consider when writing your docstring are:

- Describing what the function does
- What kind of inputs does the function take?
  Are they required or optional?
  Do they have default values?
- What output will the function produce?

Hint: Python docstrings are defined by enclosing the text with `"""` above and
below. This text is also indented to the same level as the code defined beneath
it, which is 4 whitespaces.

:::  solution

### Solution

A good enough docstring for this function would look like this:

```python
def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe
    Clean the data by removing any incomplete rows and sort by date
    """
    print(f'Reading JSON file {input_file}')
    eva_df = pd.read_json(input_file, 
                          convert_dates=['date'])
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df
```

Using [numpy's docstring convention](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard),
the docstring may look more like this:

```python
def read_json_to_dataframe(input_file):
    """
    Ingest data from a JSON file into a pandas DataFrame.

    Parameters
    ----------
    input_file
        The path to the target JSON file
    
    Returns
    -------
    eva_df : pandas.DataFrame
        The cleaned and sorted data as a dataframe structure
    """
    print(f'Reading JSON file {input_file}')
    eva_df = pd.read_json(input_file, 
                          convert_dates=['date'])
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Summary

During this episode, we have discussed the importance of code readability and explored some software engineering practices that help facilitate this.

Code readability is important because it makes it simpler and quicker for a person (future you or a collaborator) to understand what purpose the code is serving, and therefore begin contributing to it more easily, saving time and effort.

Some best practices we have covered towards code readability include:

- Variable naming practices for descriptive yet concise code
- Inline comments to provide real-world context
- Functions to isolate specific code sections for re-use
- Docstrings for documenting functions to facilitate their re-use

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- ['Code Readability Matters' from the Guardian's engineering blog](https://www.theguardian.com/info/2019/jan/29/code-readability-matters)
- [PEP 8 Style Guide for Python](https://peps.python.org/pep-0008/#comments)
- [Coursera: Inline commenting in Python](https://www.coursera.org/tutorials/python-comment#inline-commenting-in-python)
- [Introducing Functions from Introduction to Python](https://introtopython.org/introducing_functions.html)
- [W3Schools.com Python Functions](https://www.w3schools.com/python/python_functions.asp)

Also check the [full reference set](learners/reference.md#litref) for the course.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Readable code is easier to understand, maintain, debug and extend!
- Creating functions from the smallest, reusable units of code will help compartmentalise which parts of the code are doing what actions
- Choosing descriptive variable and function names will communicate their purpose more effectively
- Using inline comments and docstrings to describe parts of the code will help transmit understanding, and verify that the code is correct

::::::::::::::::::::::::::::::::::::::::::::::::::
