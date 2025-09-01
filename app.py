# app.py
import streamlit as st
from lexer import tokenize
from syntax_parser import Parser # Use the renamed file
from visualizer import visualize_tree

# --- App Layout ---
st.set_page_config(page_title="Parse Tree Generator", layout="wide")
st.title("🌳 Arithmetic Expression Parse Tree Generator")
st.write("Enter an arithmetic expression to generate its tokens and visualize the parse tree.")

# --- User Input ---
expression = st.text_input(
    "Enter your expression:", 
    value="3 * (4 + 2)",
    placeholder="e.g., 5 * (10 - 2)"
)

# --- Generate Button and Output ---
if st.button("Generate Parse Tree", type="primary"):
    if not expression:
        st.warning("Please enter an expression.")
    else:
        try:
            # --- Analysis Pipeline ---
            st.subheader("1. Lexical Analysis (Tokens)")
            tokens = tokenize(expression)
            st.json(tokens) # Display tokens in a nicely formatted box

            st.subheader("2. Syntax Analysis (Parse Tree)")
            parser = Parser(tokens)
            parse_tree = parser.parse()
            
            # --- Visualization ---
            image_path = visualize_tree(parse_tree, filename="output/parse_tree")
            
            if image_path:
                st.image(image_path, caption="Generated Parse Tree")
            else:
                st.error("Could not generate the parse tree image.")

        except RuntimeError as e:
            st.error(f"💥 Error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")