# main.py

def parse_turrilang_code(code):
    # Example: Translate a simple custom language syntax to Python
    python_code = ""
    for line in code.splitlines():
        if line.startswith("print "):
            python_code += f"print({line[6:]})\n"
        # Add more translation rules here
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