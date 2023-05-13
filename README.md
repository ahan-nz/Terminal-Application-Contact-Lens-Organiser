# T1A3 Terminal Application
## By Alicia Han

[Github Repository](https://github.com/ahan-nz/CA-T1A3-TerminalApplication)

[Video Presentation](https://youtu

[My Trello Board](https://trello.com/b/ZHAu8luF/ca-t1a3-terminal-app)

### Style Guide

This application in Python follows the PEP8 Style Guide (van Rossum, Warsaw and Coghlan, 2023). This includes, but isn't limited to, the following guidelines:
* 4 spaces per indentation level
* Maximum line length is 79 characters
* Imports on separate lines
* Using single-quoted strings consistently, except when an apostrophe appears in the string, in which case double-quotes were used to avoid backslashes, and hence improve readability
* Comments in complete sentences and the first word is capitalised. Also inline comments were avoided
* Function names are in lower case and words are separated by underscores to improve readability.


### Implementation Plan

Trello

### Bash Script

```
#!/bin/bash
cd ./src
if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 -m venv .venv 
        source .venv/bin/activate
        pip3 install -r ./requirements.txt
        python3 main.py
    else
        echo "Please update your version of Python." >&2
    fi 
else
    echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi

```

### Dependencies

* iniconfig==2.0.0
* packaging==23.1
* pluggy==1.0.0
* pytest==7.3.1

### Key Features

### Imported Packages and Modules

* csv
* datetime
* sys
* pytest
* unittest

### References

* van Rossum, G., Warsaw, B. and Coghlan, N. (2023). PEP 8 – Style Guide for Python Code | peps.python.org. [online] peps.python.org. Available at: https://peps.python.org/pep-0008/.

(cite each package/module)