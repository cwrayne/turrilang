# main.py

import os
import sys

def parse_turrilang_code(code):
    python_code = ""
    for line in code.splitlines():
        if line.startswith("print "):
            python_code += f"print({line[6:]})\n"
    return python_code

def parse_and_translate(input_file, output_file):
    with open(input_file, 'r') as file:
        turrilang_code = file.read()
    
    python_code = parse_turrilang_code(turrilang_code)
    
    with open(output_file, 'w') as file:
        file.write(python_code)

def execute_translated_code(python_file):
    with open(python_file, 'r') as file:
        exec(file.read())

def resource_path(relative_path):
    """Get the absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    # Path to the bundled example.tl file
    input_file = resource_path("example.tl")

    if not os.path.isfile(input_file):
        print(f"File not found: {input_file}")
        sys.exit(1)
    
    output_file = resource_path("translated_code.py")
    
    parse_and_translate(input_file, output_file)
    execute_translated_code(output_file)