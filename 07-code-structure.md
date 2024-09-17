---
title: Code structure
teaching: 60
exercises: 30
---

:::::::::::::::::::::::::::::::::::::: questions

- How can be bests structure code into reusable components with a single responsibility?
- What is a common code structure (pattern) for creating software that can read input from command line?
- What are conventional places to store data, code, results, tests and auxiliary information and metadata 
within our software or research project? 

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives
After completing this episode, participants should be able to:

- Structure code that is modular and split into small, reusable functions.
- Use the common code pattern for creating software that can read input from command line
- Follow best practices in structuring code and organising software/research project directories for improved 
readability, accessibility and reproducibility.

::::::::::::::::::::::::::::::::::::::::::::::::

In the previous episode we have seen some tools and practices that can help up improve readability of our code - 
including breaking our code into small, reusable functions that perform one specific task.
We are going to explore a bit more how using common code structures can improve readability, accessibility and 
reusability of our code, and will expand these practices on our (research or code) projects as a whole.

Before we move on with further code modifications, make sure your virtual development environment is active.

:::::: instructor

::: callout

### Activate your virtual environment
If it is not already active, make sure to remind learners to activate their virtual environments from the root of
the software project directory in command line terminal (e.g. Bash or GitBash):

```bash
$ source venv_spacewalks/bin/activate # Mac or Linux
$ source venv_spacewalks/Scripts/activate # Windows
(venv_spacewalks) $
```
:::


At this point, the state of the software repository should be as in 
https://github.com/carpentries-incubator/astronaut-data-analysis-not-so-fair/tree/07-code-structure
and the `eva_data_analysis.py` code should look like as follows:

``` python
import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe.
    Clean the data by removing any incomplete rows and sort by date

    Args:
        input_file_ (str): The path to the JSON file.

    Returns:
         eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe structure
    """
    print(f'Reading JSON file {input_file}')
    # Read the data from a JSON file into a Pandas dataframe
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)
    # Clean the data by removing any incomplete rows and sort by date
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    """
    Write the dataframe to a CSV file.

    Args:
        df (pd.DataFrame): The input dataframe.
        output_file (str): The path to the output CSV file.

    Returns:
        None
    """
    print(f'Saving to CSV file {output_file}')
    # Save dataframe to CSV file for later analysis
    df.to_csv(output_file, index=False)


# Main code

print("--START--")

input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'

# Read the data from JSON file
eva_data = read_json_to_dataframe(input_file)

# Convert and export data to CSV file
write_dataframe_to_csv(eva_data, output_file)

print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
# Plot cumulative time spent in space over years
eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()
plt.plot(eva_data['date'], eva_data['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()

print("--END--")


```
::::::

## Functions for Modular and Reusable Code 

As we have already seen in the previous episode - functions play a key role in creating modular and reusable code.
We are going to carry on improving our code following these principles:

- Each function should have a single, clear responsibility. This makes functions easier to understand, test, and reuse.
- Functions should accept parameters to allow flexibility and reusability in different contexts; avoid hard-coding 
values inside functions/code (e.g. data files to read from/write to); instead, pass them as arguments.
- Split complex tasks into smaller, simpler functions that can be composed; each function should handle a distinct 
part of a larger task.
- Write functions that can be easily combined or reused with other functions to build more complex functionality.

Bearing in mind the above principles, we can further simplify our code by extracting the code to process, 
analyse our data and plot a graph into a separate function `plot_cumulative_time_in_space`, and then further break down
the code to convert the data column containing spacewalk durations as text into numbers which we can perform 
arithmetic operations over, and add that numerical data as a new column in our dataset. 

The main part of our code then becomes much simpler and more readable, only 
containing the invocation of the following three functions:

```python
eva_data = read_json_to_dataframe(input_file)
write_dataframe_to_csv(eva_data, output_file)
plot_cumulative_time_in_space(eva_data, graph_file)
```
Remember to add docstrings and comments to the new functions to explain their functionalities. 

Our new code may look like the following.

```python


import matplotlib.pyplot as plt
import pandas as pd


def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe.
    Clean the data by removing any incomplete rows and sort by date

    Args:
        input_file_ (str): The path to the JSON file.

    Returns:
         eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe structure
    """
    print(f'Reading JSON file {input_file}')
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    """
    Write the dataframe to a CSV file.

    Args:
        df (pd.DataFrame): The input dataframe.
        output_file (str): The path to the output CSV file.

    Returns:
        None
    """
    print(f'Saving to CSV file {output_file}')
    df.to_csv(output_file, index=False)

def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration_hours (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60
    return duration_hours


def add_duration_hours_variable(df):
    """
    Add duration in hours (duration_hours) variable to the dataset

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        df_copy (pd.DataFrame): A copy of df_ with the new duration_hours variable added
    """
    df_copy = df.copy()
    df_copy["duration_hours"] = df_copy["duration"].apply(
        text_to_duration
    )
    return df_copy


def plot_cumulative_time_in_space(df, graph_file):
    """
    Plot the cumulative time spent in space over years

    Convert the duration column from strings to number of hours
    Calculate cumulative sum of durations
    Generate a plot of cumulative time spent in space over years and
    save it to the specified location

    Args:
        df (pd.DataFrame): The input dataframe.
        graph_file (str): The path to the output graph file.

    Returns:
        None
    """
    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    df = add_duration_hours_variable(df)
    df['cumulative_time'] = df['duration_hours'].cumsum()
    plt.plot(df.date, df.cumulative_time, 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()


# Main code

print("--START--")

input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'

eva_data = read_json_to_dataframe(input_file)

write_dataframe_to_csv(eva_data, output_file)

plot_cumulative_time_in_space(eva_data, graph_file)

print("--END--")


```

## Command-line interface to code

A common way to structure code is to have a command-line interface to allow the passing of input data file to be 
read and the output file to be written to as parameters to our script and avoid hard-coding them.
This improves interoperability and reusability of our code as it can now be run from the
command line terminal and integrated into other scripts or workflows/pipelines. 
For example, another script can produce 
our input data and can be "chained" with our code in a more complex data analysis pipeline.
Or we can invoke our script in a loop to quickly analyse a number of input data files from a directory.

There is a common code structure (pattern) for this:

```python
# import modules

def main(args):
    # perform some actions

if __name__ == "__main__":
    # perform some actions before main()
    main(args)
```

In this pattern the actions performed by the script are contained within the `main` function
(which does not need to be called `main`, but using this convention helps others in understanding your code).
The `main` function is then called within the `if` statement `__name__ == "__main__"`,
after some other actions have been performed (usually the parsing of command-line arguments, 
which will be explained below).
`__name__` is a special variable which is set by the Python interpreter before the execution of any code in the 
source file.
What value is given by the interpreter to `__name__` is determined by the manner in which the script is loaded.

If we run the source file directly using the Python interpreter, e.g.:

```bash
$ python3 eva_data_analysis.py
```

then the interpreter will assign the hard-coded string `"__main__"` to the `__name__` variable:

```python
__name__ = "__main__"
...
# rest of your code
```

However, if your source file is imported by another Python script, e.g:

```python
import eva_data_analysis
```

then the Python interpreter will assign the name "eva_data_analysis" from the import statement to the 
`__name__` variable:

```python
__name__ = "eva_data_analysis"
...
# rest of your code
```

Because of this behaviour of the Python interpreter, we can put any code that should only be executed when running 
the script directly within the `if __name__ == "__main__":` structure,
allowing the rest of the code within the script to be safely imported by another script if we so wish.

While it may not seem very useful to have your script importable by another script,
there are a number of situations in which you would want to do this:

- for testing of your code, you can have your testing framework import the main script,
  and run special test functions which then call the `main` function directly;
- where you want to not only be able to run your script from the command-line,
  but also provide a programmer-friendly application programming interface (API) for advanced users.

We will use `sys` library to read the command line arguments passed to our script and make them available in our
code as a list - remember to import this library first.

Our modified code will now look as follows.

```python
import json
import csv
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import sys

def main(input_file, output_file, graph_file):
    print("--START--")

    eva_data = read_json_to_dataframe(input_file)

    write_dataframe_to_csv(eva_data, output_file)

    plot_cumulative_time_in_space(eva_data, graph_file)

    print("--END--")

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe.
    Clean the data by removing any incomplete rows and sort by date

    Args:
        input_file_ (str): The path to the JSON file.

    Returns:
         eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe structure
    """
    print(f'Reading JSON file {input_file}')
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    """
    Write the dataframe to a CSV file.

    Args:
        df (pd.DataFrame): The input dataframe.
        output_file (str): The path to the output CSV file.

    Returns:
        None
    """
    print(f'Saving to CSV file {output_file}')
    df.to_csv(output_file, index=False)

def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration_hours (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60
    return duration_hours


def add_duration_hours_variable(df):
    """
    Add duration in hours (duration_hours) variable to the dataset

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        df_copy (pd.DataFrame): A copy of df_ with the new duration_hours variable added
    """
    df_copy = df.copy()
    df_copy["duration_hours"] = df_copy["duration"].apply(
        text_to_duration
    )
    return df_copy


def plot_cumulative_time_in_space(df, graph_file):
    """
    Plot the cumulative time spent in space over years

    Convert the duration column from strings to number of hours
    Calculate cumulative sum of durations
    Generate a plot of cumulative time spent in space over years and
    save it to the specified location

    Args:
        df (pd.DataFrame): The input dataframe.
        graph_file (str): The path to the output graph file.

    Returns:
        None
    """
    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    df = add_duration_hours_variable(df)
    df['cumulative_time'] = df['duration_hours'].cumsum()
    plt.plot(df.date, df.cumulative_time, 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()


if __name__ == "__main__":

    if len(sys.argv) < 3:
        input_file = './eva-data.json'
        output_file = './eva-data.csv'
        print(f'Using default input and output filenames')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        print('Using custom input and output filenames')

    graph_file = './cumulative_eva_graph.png'
    main(input_file, output_file, graph_file)

```

We can now run our script from the command line passing the JSON input data file and CSV output data file as:

```bash
(venv_spacewalks) $ python eva_data_analysis.py eva_data.json eva_data.csv
```

Remember to commit our changes.

```bash
(venv_spacewalks) $ git status
(venv_spacewalks) $ git add eva_data_analysis.py
(venv_spacewalks) $ git commit -m "Add command line functionality to script"
```

## Directory structure for software projects

One of the steps to make your work more easily readable and reproducible is to organise your software projects 
following certain conventions on consistent and informative directory structure. 
This way, people will immediately know where to find things within your project.
Here are some general guidelines that apply to all research projects (including software projects):

- Put all files related to a project into a single directory
- Do not mix project files - different projects should have separate directories and repositories (it is OK to copy 
files into multiple places if both projects require them)
- Avoid spaces in directory and file names – they can cause errors when read by computers
- If you have sensitive data - you can put it in a private repository on GitHub
- Use .gitignore to specify what files should not be tracked - e.g. passwords, local configuration, etc.
- Add a README file to your repository to describe the project and instructions on running the code or reproducing 
the results (we will covered this later in this course).

```output
project_name/
├── README.md             # overview of the project
├── data/                 # data files used in the project
│   ├── README.md         # describes where data came from
│   └── sub-folder/       # may contain subdirectories, e.g. for intermediate files from the analysis
├── manuscript/           # manuscript describing the results
├── results/              # results of the analysis (data, tables, figures)
├── src/                  # contains all code in the project
│   ├── LICENSE           # license for your code
│   ├── requirements.txt  # software requirements and dependencies
│   └── ...
├── src/                  # source code for your project
├── doc/                  # documentation for your project
├── index.rst
├── main_script.py        # main script/code entry point
└── ...
```

- Source code is typically placed in the `src/` or `source/` directory (and its subdirectories containing hierarchical 
libraries of your code). The main script or the main entry to your code may remain in the project root.
- Data is typically placed under `data/` 
    - Raw data or input files can also be placed under `raw_data/` - original data should not be modified and should be kept raw
    - Processed or cleaned data or intermediate results from data analysis can be placed under `processed_data/`
- Documentation is typically placed or compiled into `doc/` or `docs/`
- Results are typically placed under results/
- Tests are typically placed under tests/

:::::: challenge

Refactor your software project so that input data is stored in `data/` directory and results (the graph and CSV 
data files) saved in `results/` directory.

::: solution

```python
import matplotlib.pyplot as plt
import pandas as pd
import sys

# https://data.nasa.gov/resource/eva.json (with modifications)

def main(input_file, output_file, graph_file):
    print("--START--")

    eva_data = read_json_to_dataframe(input_file)

    write_dataframe_to_csv(eva_data, output_file)

    plot_cumulative_time_in_space(eva_data, graph_file)

    print("--END--")

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe.
    Clean the data by removing any incomplete rows and sort by date

    Args:
        input_file_ (str): The path to the JSON file.

    Returns:
         eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe structure
    """
    print(f'Reading JSON file {input_file}')
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    """
    Write the dataframe to a CSV file.

    Args:
        df (pd.DataFrame): The input dataframe.
        output_file (str): The path to the output CSV file.

    Returns:
        None
    """
    print(f'Saving to CSV file {output_file}')
    df.to_csv(output_file, index=False)

def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration_hours (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60
    return duration_hours


def add_duration_hours_variable(df):
    """
    Add duration in hours (duration_hours) variable to the dataset

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        df_copy (pd.DataFrame): A copy of df_ with the new duration_hours variable added
    """
    df_copy = df.copy()
    df_copy["duration_hours"] = df_copy["duration"].apply(
        text_to_duration
    )
    return df_copy


def plot_cumulative_time_in_space(df, graph_file):
    """
    Plot the cumulative time spent in space over years

    Convert the duration column from strings to number of hours
    Calculate cumulative sum of durations
    Generate a plot of cumulative time spent in space over years and
    save it to the specified location

    Args:
        df (pd.DataFrame): The input dataframe.
        graph_file (str): The path to the output graph file.

    Returns:
        None
    """
    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    df = add_duration_hours_variable(df)
    df['cumulative_time'] = df['duration_hours'].cumsum()
    plt.plot(df.date, df.cumulative_time, 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()


if __name__ == "__main__":

    if len(sys.argv) < 3:
        input_file = 'data/eva-data.json'
        output_file = 'results/eva-data.csv'
        print(f'Using default input and output filenames')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        print('Using custom input and output filenames')

    graph_file = 'results/cumulative_eva_graph.png'
    main(input_file, output_file, graph_file)

```

```bash
(venv_spacewalks) $ git status
(venv_spacewalks) $ git add eva_data_analysis.py data results
(venv_spacewalks) $ git commit -m "Update project's directory structure"
```
:::

::::::

## Further reading

We recommend the following resources for some additional reading on the topic of this episode:

- [Organizing your projects](https://coderefinery.github.io/reproducible-research/organizing-projects/) chapter from the [CodeRefinery's Reproducible Research tutorial](https://coderefinery.github.io/reproducible-research/intro/)
- [MIT Broad Reseach Communication Lab's "File Structure" guide](https://mitcommlab.mit.edu/broad/commkit/file-structure/)

Also check the [full reference set](learners/reference.md#litref) for the course.

::: keypoints

- Good practices for code and project structure are essential for creating readable, accessible and reproducibile projects.

:::
