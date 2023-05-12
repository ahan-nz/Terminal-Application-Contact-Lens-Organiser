# T1A3 Terminal Application
## By Alicia Han

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