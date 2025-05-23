# TurriLang
GPT-4o's attempt at making a programming language using Python that supports Python code and it's own interpreter.
# Commands
## Commands:

`print <text>` - Prints text to the screen.

`loop_print <number> <text>` - Print text a number of times

`func <name> <arg1> <arg2>` - Creates a function named with two arguments: arg1 and arg2

`if, elif, else, for, while` - Basic Python functions

`end` - Ends `if`, `elif`, `else`, `for`, etc.

`double <name>` - Creates a double variable

`increment <variable>` - The equivalent of += in TurriLang

`check_even <variable>` - Checks if a variable is even

## Precaution before using Python and Turrilang at the same time 
If you start with a Python command, you can ONLY use Python commands for the rest of the line.
Same vice versa: If you start with a TurriLang command, you can ONLY use TurriLang commands for the rest of the line.
## Windows
### Easy Setup
Download the latest version of `compiler.exe` and in CMD/PowerShell, run:
```
compiler.exe file.tl
```
### Manual Setup
#### Get Pip with Python
Open PowerShell in the turrilang folder and type:
```batch

portable-python/python.exe get-pip.py
```
And then ensure `pip` is installed:
```batch
portable-python/python.exe -m pip
```
##### Troubleshooting
If you get the error:
```
ModuleNotFoundError: No module named 'pip'
```
or:
```
portable-python_XXX\python.exe: No module named pip
```
or:
```
portable-python_XXX\python.exe: No module named ensurepip
```
then solve it by editing [portable python directory]/pythonXXX._pth and remove the `#` from `#import site`.
#### Install PyInstaller
Install pyinstaller using CMD/PowerShell in the turrilang directory, **NOT** in the portable-python directory using this command:
```batch
portable-python/python.exe -m pip install pyinstaller
```
#### Make a compiler
##### Compiler
To compile main.exe/compiler.exe, run this command for the compiler in the turrilang directory:
```
portable-python/python.exe -m PyInstaller --onefile main.py
```
and then run
```
dist/main.exe < .tl file > and it will print the results.
```
### Make a compiled standalone EXE file
#### Dependencies
- Python - Download them from [Python's official website.](https://python.org)
- pip
- create-exe.py from the latest release
- A .tl file for compiling

#### Creating the EXE
##### Install PyInstaller
Enter the command:
```
python -m pip install pyinstaller
```
##### Create the EXE
Enter this command in the directory that contains create-exe.py:
```
python -m PyInstaller --onefile --add-data "file.tl;." create-exe.py
```
and replace file.tl with your TurriLang file.
Then to run the application:
```
dist/create-exe.exe
```
and it will print the results.
## macOS

### Dependencies
- Python - Get it from [Python's official website.](https://python.org)
- Latest compiler.app.zip
### Run a file
Run the command:
```
compiler.app <file>
```
and it will print the results, or:
```
python compiler-unix.py
```
and enter the file path when prompted.
## Linux
### Dependencies
- Python - Get it from [Python's official website.](https://python.org)
- Latest compiler-linux.py
### Run a file
Run the command:
```
python compiler-linux.py <file>
```
and it will print the results, or:
```
python compiler-linux.py
```
and enter the file path when prompted.
