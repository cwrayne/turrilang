# Turrilang
GPT-4o's attempt at making a programming language using Python
## Basic Setup
### Get Pip with Python
Open PowerShell in the folder and type:
```batch
cd portable-python
./python.exe get-pip.py
```
And then ensure `pip` is installed:
```batch
./python.exe -m ensurepip
```
#### Troubleshooting
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
###