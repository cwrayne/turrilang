def parse_turrilang_code(code):
    python_code = ""
    indent_level = 0
    indent = "    "
    control_stack = []

    def increase_indent():
        nonlocal indent_level
        indent_level += 1

    def decrease_indent():
        nonlocal indent_level
        if indent_level > 0:
            indent_level -= 1

    def append_line(line):
        nonlocal python_code
        python_code += f"{indent * indent_level}{line}\n"

    for line in code.splitlines():
        stripped_line = line.strip()

        if stripped_line == 'end':
            while control_stack:
                control_stack.pop()
                decrease_indent()
            continue

        # Handle different constructs
        if stripped_line.startswith("print "):
            append_line(f"print({stripped_line[6:]})")
        elif "=" in stripped_line and "==" not in stripped_line:
            append_line(stripped_line)
        elif stripped_line.startswith("if "):
            condition = stripped_line[3:].rstrip(":")
            append_line(f"if {condition}:")
            increase_indent()
            control_stack.append("if")
        elif stripped_line.startswith("elif "):
            if control_stack and control_stack[-1] == "if":
                control_stack.pop()
                decrease_indent()
            condition = stripped_line[5:].rstrip(":")
            append_line(f"elif {condition}:")
            increase_indent()
            control_stack.append("elif")
        elif stripped_line.startswith("else"):
            if control_stack and control_stack[-1] == "if":
                control_stack.pop()
                decrease_indent()
            append_line("else:")
            increase_indent()
            control_stack.append("else")
        elif stripped_line.startswith("for "):
            rest_of_line = stripped_line[4:].rstrip(":")
            append_line(f"for {rest_of_line}:")
            increase_indent()
            control_stack.append("for")
        elif stripped_line.startswith("while "):
            condition = stripped_line[6:].rstrip(":")
            append_line(f"while {condition}:")
            increase_indent()
            control_stack.append("while")
        elif stripped_line.startswith("print_upper "):
            text = stripped_line[12:].strip("\"'")  # Extract text without quotes
            append_line(f"print({text.upper()!r})")
        elif stripped_line.startswith("double "):
            var = stripped_line[7:].strip()
            append_line(f"{var} *= 2")
        elif stripped_line.startswith("swap "):
            vars = stripped_line[5:].split(",")
            var1, var2 = vars[0].strip(), vars[1].strip()
            append_line(f"{var1}, {var2} = {var2}, {var1}")
        elif stripped_line.startswith("increment "):
            var = stripped_line[10:].strip()
            append_line(f"{var} += 1")
        elif stripped_line.startswith("loop_print "):
            parts = stripped_line[11:].split(" ", 1)
            n, message = parts[0], parts[1].strip("\"'")
            append_line(f"for _ in range({n}):")
            increase_indent()
            append_line(f"print({message!r})")
            decrease_indent()
        elif stripped_line.startswith("func "):
            parts = stripped_line.split()
            func_name = parts[1]
            args = ", ".join(parts[2:]).rstrip(":")
            append_line(f"def {func_name}({args}):")
            increase_indent()
            control_stack.append("func")
        elif stripped_line.startswith("check_even "):
            var = stripped_line[11:].strip()
            append_line(f"if {var} % 2 == 0:")
            increase_indent()
            append_line(f"print(f'{{{var}}} is even')")
            decrease_indent()
        else:
            append_line(stripped_line)

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

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_turrilang_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = "translated_code.py"
    
    parse_and_translate(input_file, output_file)
    execute_translated_code(output_file)