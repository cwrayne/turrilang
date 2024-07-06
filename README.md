# TurriLang
GPT-4o's attempt at making a programming language using Python that supports Python code and it's own interpreter.
# Commands
`print <text>` - Prints text to the screen.

`loop_print <number> <text>` - Print <text> <number> times

`func <name> <arg1> <arg2>` - Creates a function named <name> with two arguments: <arg1> and <arg2>

`end_func` - Ends a function

`if`, `elif`, `else`, `for`, `while` - Basic Python functions

`check_even <number>` - Checks if a number is even
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
then solve it by editing [portable python directory]/pythonXXX._pth and remove the `#` from `#import site`
#### Install PyInstaller
Install pyinstaller using CMD/PowerShell in the turrilang directory, **NOT** in the portable-python directory using this command:
```batch
portable-python/python.exe -m pip install pyinstaller
```
#### Compile main.exe
##### Compiler
To compile main.exe/compiler.exe, run this command for the compiler in the turrilang directory:
```
portable-python/python.exe -m PyInstaller --onefile main.py
```
and then run
```
dist/main.exe < .tl file > and it will print the results.
```
##### Standalone
For a standalone exe, run:
```
./portable-python/python.exe -m PyInstaller --onefile --add-data "file.tl;." main-noargs.py
```
and replace file.tl with your TurriLang file.
Then run:
```
dist/main-noargs.exe
```
and it will print the results.
## Unix (macOS and Linux)
### Dependencies
- Python - Get it from [Python's official website.](https://python.org)
- Latest compiler-unix.py
### Run a file
Run the command:
```
python compiler-unix.py <file>
```
and it will print the results, or:
```
python compiler-unix.py
```
and enter the file path when prompted.
