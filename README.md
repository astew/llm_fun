# Txt2Cmd

Txt2Cmd is a command line utility written in Python that helps you generate or update Python scripts using natural language descriptions. The tool uses Language Learning Models (LLMs) to convert natural language input into code.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Limitations](#limitations)

## Installation
Before using Txt2Cmd, ensure that you have Python 3 installed on your system.

Clone the repository to your local machine and navigate to the project directory:
```
git clone <repository-url>
cd txt2cmd
```
Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```

## Usage
Txt2Cmd provides two functionalities:

1. **Creating a new script**
   You can create a new script by using the `new` command followed by a natural language description of the script's functionality. The generated script is printed to the console by default. 

   Here's an example of creating a script that reads a file and counts the number of words:
    ```
    $ python mkcmd.py new "Create a Python script that reads a file called 'input.txt' and prints the number of words."
    ```
   If you want the script to be written to a file, you can use the `--out-file` option:
    ```
    $ python mkcmd.py new --out-file read_words.py "Create a Python script that reads a file called 'input.txt' and prints the number of words."
    ```

2. **Updating an existing script**
   You can update an existing script by using the `update` command, followed by the file name and a natural language description of the changes to be made. The updated script is printed to the console by default.

   Here's an example of updating a script to also count the number of lines:
    ```
    $ python mkcmd.py update read_words.py "Update the script to also count and print the number of lines in the file."
    ```
   Again, if you want the updated script to be written to a different file, use the `--out-file` option:
    ```
    $ python mkcmd.py update read_words.py --out-file read_lines_words.py "Update the script to also count and print the number of lines in the file."
    ```

## File Structure
The main application directory contains the following files:

- `config.py`: Configuration file for loading secret stuff (like OPENAI_API_KEY) from a `.env` file
- `language_map.py`: Mappings from file extensions to programming languages
- `mkcmd.py`: The command line script itself
- `pyproject.toml`: Project metadata and dependencies file for Poetry
- `requirements.txt`: Python requirements file

## Limitations
- This tool is primarily designed for simple script generation. While it can handle a variety of tasks, complex or specific code generation might not be perfect.
- Although the utility can interpret natural language prompts for many common programming and scripting languages, some languages may not be supported.
- There is no defined limit for the length of the 'prompt' input, but for practical purposes, more than a paragraph is likely to be excessive.

Please note that this tool is still under development and these limitations might be addressed in future releases.
