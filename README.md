
# Arithmetic Expression Parse Tree Generator 

This project is a simple compiler tool that takes an arithmetic expression as input, performs lexical and syntax analysis, and generates a visual parse tree. It's a great demonstration of the initial stages of a compiler.

## Features

  * **Lexical Analysis**: Converts the input string into a stream of tokens.
  * **Syntax Analysis**: Builds a parse tree based on a context-free grammar.
  * **Operator Support**: Handles addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
  * **Parentheses**: Correctly interprets expressions within parentheses `( )` to manage precedence.
  * **Visualization**: Uses Graphviz to render the parse tree as a PNG image, which opens automatically.
  * **Error Handling**: Provides user-friendly messages for syntax or lexical errors.

-----

## Project Structure

The project is organized into modular Python scripts for clarity and maintainability.

```
compiler_project/
├── main.py          # Main script to run the program
├── lexer.py         # Handles lexical analysis (tokenizing)
├── syntax_parser.py        # Handles syntax analysis (tree building)
├── visualizer.py    # Handles tree visualization with Graphviz
└── requirements.txt   # Lists project dependencies
```

-----

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1.  **Python 3.6+**: You can download it from [python.org](https://www.python.org/).
2.  **Graphviz**: This is a command-line tool required for rendering the tree image.
      * **Windows**: Download from the [official site](https://graphviz.org/download/). **Important**: Make sure to add Graphviz to your system's PATH during installation.
      * **macOS**: `brew install graphviz`
      * **Linux (Ubuntu/Debian)**: `sudo apt-get install graphviz`

-----

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

**1. Clone the repository (or create the files):**

```bash
git clone <your-repository-url>
cd compiler_project
```

**2. Create and activate a virtual environment:**
This step isolates the project's dependencies from your system's Python installation.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**3. Install the required Python packages:**

```bash
pip install -r requirements.txt
```

-----

## ▶️ How to Run

Once the setup is complete, you can run the main script from your terminal:

```bash
python main.py
```

The program will start and prompt you to enter an arithmetic expression.

-----

## Usage Example

After running the application, you can interact with it as shown below.

**1. Start the program:**

```bash
$ python main.py
 Arithmetic Expression Parse Tree Generator
Enter an expression (e.g., '3 * (4 + 2)') or type 'exit' to quit.
```

**2. Enter an expression:**

```bash
>>> 5 * (10 - 2)
```

**3. See the output:**
The terminal will show the token stream and a success message.

```
Tokens: [{'kind': 'NUMBER', 'value': '5'}, {'kind': 'MULTIPLY', 'value': '*'}, {'kind': 'LPAREN', 'value': '('}, {'kind': 'NUMBER', 'value': '10'}, {'kind': 'MINUS', 'value': '-'}, {'kind': 'NUMBER', 'value': '2'}, {'kind': 'RPAREN', 'value': ')'}]
Successfully generated parse tree at: parse_tree.png
```

An image file named `parse_tree.png` will be created in your project directory and will automatically open for you to view.

**4. Handling errors:**
If you enter an invalid expression, the program will catch it and display an error.

```bash
>>> 5 + * 2
💥 Syntax Error: Unexpected token {'kind': 'MULTIPLY', 'value': '*'}
```

**5. Exit the program:**
To stop the application, simply type `exit` and press Enter.

```bash
>>> exit
```

-----

## File Descriptions

  * `main.py`: The entry point for the application. It handles user input and orchestrates the calls to the lexer, parser, and visualizer.
  * `lexer.py`: Contains the `tokenize` function, which performs lexical analysis using regular expressions to convert the input string into a list of tokens.
  * `parser.py`: Implements a recursive descent parser. It takes the token list and builds an abstract syntax tree based on the defined grammar rules for arithmetic expressions.
  * `visualizer.py`: Uses the `graphviz` library to traverse the generated parse tree and render it into a visually appealing graph, saved as a PNG file.
  * `requirements.txt`: A list of the Python packages required for the project to run.