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

- Organise code into reusable functions that achieve a singular purpose
- Create function and variable names that help explain the purpose of the function or variable
- Write informative inline comments and docstrings to provide more detail about what the code is doing

::::::::::::::::::::::::::::::::::::::::::::::::

### Variable names

:::::::::::::::::::::::::::::::::::::: challenge

### Give a descriptive name to a variable

Below we have a variable called `var` being set the value of 9.81.
`var` is not a very descriptive name here as it doesn't tell us what 9.81 means, yet it is a very common constant in orbital mechanics!
Go online and find out which constant 9.81 relates to and suggest a new name for this variable.

Hint: the units are _metres per second squared_!

```python
var = 9.81
```

:::::::::::::: solution

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

:::::::::::::::::::::::::::::::::::::: challenge

### Add some comments to a code block

Examine lines 7 to 20 of the `bad-code.py` script.
Add (or change!) as many inline comments as you think is required to help yourself and others understand what that code block is doing.

Hint: Inline comments in Python are denoted by a `#` symbol.

:::::::::::::: solution

### Solution

Some good inline comments may look like the below example.

```python
# Loop through 370 iterations
for count in range(370):
    # Read a line from the CSV file as a string, and split it up into a
    # list wherever the ',' character appears
    line = csvfile.readline().split(',')

    # Create a temporary dictionary to store data in
    l = dict()
    # Loop over the items in the line from the CSV file
    for thing in range(len(line[:7])):
        # Add the item to the temporary dictionary
        l[fieldnames[thing]] = line[thing]

    # Using the json library, output the dictionary to a json file
    import json
    json.dump(l, jsonfile)
    # Add a newline to the json file ready for the next entry
    jsonfile.write('\n')

# Close the json file
jsonfile.close()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Functions

:::::::::::::::::::::::::::::::::::::: challenge

### Create a function

Below is a function that reads in a JSON file into a dataframe structure using the [`pandas` library](https://pandas.pydata.org/) - but the code is out of order!
Reorder the lines of code within the function so that the JSON file is read in using the `read_json` function, any incomplete rows are _dropped_, the values are _sorted_ by date, and then the cleaned dataframe is _returned_.
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

:::::::::::::: solution

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

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Docstrings

:::::::::::::::::::::::::::::::::::::: challenge

### Writing docstrings

Write a docstring for the `read_json_to_dataframe` function from the previous
exercise. Things you may want to consider when writing your docstring are:

- Describing what the function does
- What kind of inputs does the function take? Are they required or optional?
  Do they have default values?
- What output will the function produce?

Hint: Python docstrings are defined by enclosing the text with `"""` above and
below. This text is also indented to the same level as the code defined beneath
it.

:::::::::::::: solution

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

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- [Introducing Functions from Introduction to Python](https://introtopython.org/introducing_functions.html)
- [W3Schools.com Python Functions](https://www.w3schools.com/python/python_functions.asp)

Also check the [full reference set](learners/reference.md#litref) for the course.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Readable code is easier to understand, maintain, debug and extend!
- Creating functions from the smallest, reusable units of code will help compartmentalise which parts of the code are doing what actions
- Choosing descriptive variable and function names will communicate their purpose more effectively
- Using inline comments and docstrings to describe parts of the code will help transmit understanding, and verify that the code is correct

::::::::::::::::::::::::::::::::::::::::::::::::::
