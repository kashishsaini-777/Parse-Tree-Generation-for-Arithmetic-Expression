🌳 Arithmetic Expression Parse Tree Generator 🌳
This project provides a web-based tool, built with Streamlit, to generate a visual parse tree from an arithmetic expression. It serves as a great interactive demonstration of the initial stages of a compiler, including lexical and syntax analysis.

✨ Features
Interactive Web UI: A simple and clean web interface built with Streamlit.

Lexical Analysis: Converts the input string into a stream of tokens, displayed in a clean format.

Syntax Analysis: Builds a parse tree based on a context-free grammar.

Operator Support: Handles addition (+), subtraction (-), multiplication (*), and division (/).

Parentheses: Correctly interprets expressions within parentheses ( ) to manage operator precedence.

Instant Visualization: Uses Graphviz to render the parse tree and displays it directly in the web app.

Error Handling: Provides user-friendly error messages for syntax or lexical mistakes.

Deployable: Ready to be deployed for free on Streamlit Community Cloud.

📂 Project Structure
The project is organized into modular Python scripts for clarity and maintainability.

compiler_project/
├── app.py           # The Streamlit web application script
├── lexer.py         # Handles lexical analysis (tokenizing)
├── syntax_parser.py # Handles syntax analysis (tree building)
├── visualizer.py    # Handles tree visualization with Graphviz
├── requirements.txt   # Lists Python dependencies for pip
└── packages.txt     # Lists system-level dependencies for Streamlit Cloud

Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.7+: You can download it from python.org.

Graphviz: This is the underlying engine required for rendering the tree image.

Windows: Download from the official site. Important: Make sure to add Graphviz to your system's PATH during installation.

macOS: brew install graphviz

Linux (Ubuntu/Debian): sudo apt-get install graphviz

⚙️ Setup and Installation
Follow these steps to get the project running on your local machine.

1. Clone the repository (or create the files):

git clone <your-repository-url>
cd compiler_project

2. Create and activate a virtual environment:
This step isolates the project's dependencies from your system's Python installation.

# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install the required Python packages:

pip install -r requirements.txt

4. Create an output directory:
The application needs a directory to temporarily store the generated images.

mkdir output

▶️ How to Run Locally
Once the setup is complete, run the Streamlit app from your terminal:

streamlit run app.py

Your default web browser will automatically open a new tab with the running application.

🚀 How to Deploy
You can deploy this application for free using Streamlit Community Cloud.

1. Push to GitHub:
Make sure your entire project, including requirements.txt and packages.txt, is pushed to a public GitHub repository.

2. Deploy on Streamlit Cloud:

Go to share.streamlit.io and sign in with your GitHub account.

Click "New app" and select your repository.

Ensure the "Main file path" is set to app.py.

Click "Deploy!".

Streamlit will automatically install the system packages from packages.txt and the Python packages from requirements.txt and launch your app.

📄 File Descriptions
app.py: The main entry point for the Streamlit web application. It defines the UI and orchestrates the calls to the other modules.

lexer.py: Contains the tokenize function, which performs lexical analysis.

syntax_parser.py: Implements a recursive descent parser to build the parse tree from tokens. (Formerly parser.py).

visualizer.py: Uses the graphviz library to render the parse tree into a PNG file and returns the file path.

requirements.txt: A list of the Python packages (e.g., streamlit, graphviz) required for the project.

packages.txt: A list of system-level dependencies (graphviz) needed by the Streamlit Cloud deployment environment.