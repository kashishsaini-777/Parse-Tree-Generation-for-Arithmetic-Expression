
# 🌳 Arithmetic Expression Parse Tree Generator 🌳

This project provides a **web-based tool**, built with **Streamlit**, to generate a **visual parse tree** from an arithmetic expression.  
It serves as a great interactive demonstration of the initial stages of a **compiler**, including **lexical analysis** and **syntax analysis**.

---

## ✨ Features
- **Interactive Web UI**: Simple and clean interface built with Streamlit.  
- **Lexical Analysis**: Converts the input string into a stream of tokens, displayed neatly.  
- **Syntax Analysis**: Builds a parse tree based on a context-free grammar.  
- **Operator Support**: Handles addition `+`, subtraction `-`, multiplication `*`, and division `/`.  
- **Parentheses Handling**: Correctly interprets `( )` for operator precedence.  
- **Instant Visualization**: Uses Graphviz to render and display the parse tree.  
- **Error Handling**: User-friendly error messages for syntax or lexical issues.  
- **Deployable**: Ready to run locally or on **Streamlit Community Cloud** for free.  

---

## 📂 Project Structure
```bash
compiler_project/
├── app.py            # The Streamlit web application script
├── lexer.py          # Handles lexical analysis (tokenizing)
├── syntax_parser.py  # Handles syntax analysis (tree building)
├── visualizer.py     # Handles tree visualization with Graphviz
├── requirements.txt  # Lists Python dependencies
└── packages.txt      # Lists system-level dependencies for Streamlit Cloud
````

---

## 🛠️ Prerequisites

Ensure the following are installed on your system:

* **Python 3.7+** → [Download here](https://www.python.org/downloads/)
* **Graphviz** (required for rendering parse trees)

  * **Windows**: [Download here](https://graphviz.org/download/) → Add Graphviz to PATH during installation
  * **macOS**:

    ```bash
    brew install graphviz
    ```
  * **Linux (Ubuntu/Debian)**:

    ```bash
    sudo apt-get install graphviz
    ```

---

## ⚙️ Setup and Installation

1. **Clone the repository** (or create the files manually):

   ```bash
   git clone <your-repository-url>
   cd compiler_project
   ```

2. **Create and activate a virtual environment**:

   ```bash
   # Create the virtual environment
   python -m venv venv

   # Activate it
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create an output directory** (for generated images):

   ```bash
   mkdir output
   ```

---

## ▶️ Run Locally

Start the Streamlit app with:

```bash
streamlit run app.py
```

Your browser will open automatically with the running application.

---

## 🚀 Deploy on Streamlit Community Cloud

1. **Push to GitHub**
   Ensure your repository includes `requirements.txt` and `packages.txt`.

2. **Deploy**

   * Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in.
   * Click **New app** → Select your GitHub repo.
   * Set **Main file path** to `app.py`.
   * Click **Deploy!**

Streamlit will automatically install system packages from **packages.txt** and Python packages from **requirements.txt**, then launch your app.

---

## 📄 File Descriptions

* **app.py** → Entry point of the Streamlit app (UI + integration).
* **lexer.py** → Implements lexical analysis (tokenization).
* **syntax\_parser.py** → Recursive descent parser to build the parse tree.
* **visualizer.py** → Renders the parse tree using Graphviz.
* **requirements.txt** → Python dependencies (e.g., `streamlit`, `graphviz`).
* **packages.txt** → System-level dependencies (`graphviz`) for deployment.

---

## 🌟 Example

Input:

```
(3 + 5) * 2 - 8 / 4
```

Generated Parse Tree:
*(Rendered instantly in the app)*

---

💡 This project is perfect for **learning compiler basics**, **teaching parsing concepts**, or just visualizing how arithmetic expressions are processed!

