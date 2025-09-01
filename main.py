# main.py
from lexer import tokenize
from syntax_parser import Parser
from visualizer import visualize_tree

def main():
    print("🚀 Arithmetic Expression Parse Tree Generator")
    print("Enter an expression (e.g., '3 * (4 + 2)') or type 'exit' to quit.")

    while True:
        try:
            expression = input(">>> ")
            if expression.lower() == 'exit':
                break
            
            # 1. Lexical Analysis
            tokens = tokenize(expression)
            print("Tokens:", tokens)
            
            # 2. Syntax Analysis (Parsing)
            parser = Parser(tokens)
            parse_tree = parser.parse()
            
            # 3. Visualization
            if parse_tree:
                visualize_tree(parse_tree)
            else:
                print("Expression is empty.")

        except RuntimeError as e:
            print(f"💥 {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()