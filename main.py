import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import subprocess

def parse_turrilang_code(code):
    python_code = ""
    indent_level = 0
    indent = "    "

    def increase_indent():
        nonlocal indent_level
        indent_level += 1

    def decrease_indent():
        nonlocal indent_level
        indent_level -= 1

    for line in code.splitlines():
        stripped_line = line.strip()

        if stripped_line.startswith("print "):
            python_code += f"{indent * indent_level}print({stripped_line[6:]})\n"
        elif "=" in stripped_line and "==" not in stripped_line:  # basic variable assignment
            python_code += f"{indent * indent_level}{stripped_line}\n"
        elif stripped_line.startswith("if "):
            condition = stripped_line[3:].rstrip(":")
            python_code += f"{indent * indent_level}if {condition}:\n"
            increase_indent()
        elif stripped_line.startswith("elif "):
            decrease_indent()
            condition = stripped_line[5:].rstrip(":")
            python_code += f"{indent * indent_level}elif {condition}:\n"
            increase_indent()
        elif stripped_line.startswith("else"):
            decrease_indent()
            python_code += f"{indent * indent_level}else:\n"
            increase_indent()
        elif stripped_line.startswith("for "):
            rest_of_line = stripped_line[4:].rstrip(":")
            python_code += f"{indent * indent_level}for {rest_of_line}:\n"
            increase_indent()
        elif stripped_line.startswith("while "):
            condition = stripped_line[6:].rstrip(":")
            python_code += f"{indent * indent_level}while {condition}:\n"
            increase_indent()
        elif stripped_line.startswith("print_upper "):
            text = stripped_line[12:].strip("\"'")  # Extract text without quotes
            python_code += f"{indent * indent_level}print({text.upper()!r})\n"
        elif stripped_line.startswith("double "):
            var = stripped_line[7:].strip()
            python_code += f"{indent * indent_level}{var} *= 2\n"
        elif stripped_line.startswith("swap "):
            vars = stripped_line[5:].split(",")
            var1, var2 = vars[0].strip(), vars[1].strip()
            python_code += f"{indent * indent_level}{var1}, {var2} = {var2}, {var1}\n"
        elif stripped_line.startswith("increment "):
            var = stripped_line[10:].strip()
            python_code += f"{indent * indent_level}{var} += 1\n"
        elif stripped_line.startswith("loop_print "):
            parts = stripped_line[11:].split(" ", 1)
            n, message = parts[0], parts[1].strip("\"'")
            python_code += f"{indent * indent_level}for _ in range({n}):\n"
            increase_indent()
            python_code += f"{indent * indent_level}print({message!r})\n"
            decrease_indent()
        elif stripped_line.startswith("func "):
            parts = stripped_line.split()
            func_name = parts[1]
            args = ", ".join(parts[2:]).rstrip(":")
            python_code += f"{indent * indent_level}def {func_name}({args}):\n"
            increase_indent()
        elif stripped_line == "end_func":
            decrease_indent()
        elif stripped_line.startswith("check_even "):
            var = stripped_line[11:].strip()
            python_code += f"{indent * indent_level}if {var} % 2 == 0:\n"
            increase_indent()
            python_code += f"{indent * indent_level}print({var} + ' is even')\n"
            decrease_indent()
        else:
            if stripped_line.endswith(":"):  # Handle cases where user provided incorrect indent
                increase_indent()
            python_code += f"{indent * indent_level}{stripped_line}\n"

    return python_code

def parse_and_translate(input_file, output_file):
    with open(input_file, 'r') as file:
        turrilang_code = file.read()
    
    python_code = parse_turrilang_code(turrilang_code)
    
    with open(output_file, 'w') as file:
        file.write(python_code)

def execute_translated_code(python_file):
    result = subprocess.run(['python3', python_file], capture_output=True, text=True)
    return result.stdout

def open_file():
    input_file = filedialog.askopenfilename(filetypes=[("Turrilang files", "*.tl"), ("All files", "*.*")])
    if input_file:
        output_file = "translated_code.py"
        parse_and_translate(input_file, output_file)
        output = execute_translated_code(output_file)
        text_area.config(state=tk.NORMAL)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, output)
        text_area.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Turrilang Interpreter")

# Create a ScrolledText widget
text_area = ScrolledText(root, wrap=tk.WORD, width=100, height=30)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a button to open file
open_button = tk.Button(root, text="Open .tl File", command=open_file)
open_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
