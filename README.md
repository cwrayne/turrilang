# TurriLang
GPT-4o's attempt at making a programming language using Python
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