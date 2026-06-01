# py-pdf-editor

A minimal, lightweight, and native Linux Python utility designed to handle two essential PDF tasks—merging and splitting—without bringing in bloated dependencies or heavy web-based interfaces.

The project features a fully modular design, separating the core processing engine from the user interfaces. This allows you to use it seamlessly from the terminal as a native Linux utility or launch a clean desktop GUI when you prefer a point-and-click approach.

## 🛠️ Project Structure

Instead of a chaotic "single-file" setup, the project is split into three components with separate responsibilities, making it easy to experiment with, extend, or refactor:

* `pdf_engine.py`: The core engine. It handles the actual file manipulation (powered by `pypdf`) and integrates a set of preventive path validations.
* `gui.py`: A lightweight, distraction-free desktop interface built with native Tkinter.
* `main.py`: The orchestrator. It parses CLI arguments to trigger the terminal interface; if no arguments are provided, it dynamically imports and fires up the GUI.

## ✨ Technical Highlights (Safety First)

Even though it is a lightweight tool, robustness was a priority during development:
* **Anti-Data-Loss:** If you attempt to extract pages and accidentally set the output path to the exact same name as the input file, the engine intercepts the conflict and aborts *before* opening the write stream, saving your original file from being wiped to 0 bytes.
* **Resilient Interval Parsing:** The page range string is automatically stripped of whitespaces (e.g., `" 3 - 10 "` becomes `"3-10"`), gracefully digesting both standard notations and single-page isolation.
* **Preventive Validation:** It verifies file existence, checks write permissions on the destination folder, and validates the actual PDF page length before launching any page-copying loops.

## 🚀 Quick Start

### 1. Clone and Setup Environment
No messy global installations. Let's set up an isolated virtual environment:

```bash
git clone https://github.com/eddiBressan/py-pdf-editor.git
cd py-pdf-editor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run it Immediately 
Launch the Graphical Interface (GUI):
```bash
python main.py
```
Extract a page range via CLI (e.g., pages 3 to 10):
```bash
python main.py extract -i source.pdf -o output.pdf -r 3-10
```
Merge multiple PDFs via CLI:
```bash
python main.py merge -i file1.pdf file2.pdf file3.pdf -o merged.pdf
```

## How to Make py-pdf-editor Globally Available

This guide explains how to configure `py-pdf-editor` so you can run it from any directory on your Linux system without manually activating the virtual environment or navigating to the project folder.

---

### 🚀 Automated Setup (Single Command)

To automate the entire process (creating the launcher script, giving it execution permissions, and moving it to your system's PATH), open your terminal, move to your project root folder, and run this single command block:

```bash
# 1. Define the absolute path of your project dynamically
PROJECT_PATH=$(pwd)

# 2. Create the wrapper script with proper environment routing
cat << EOF > py-pdf-editor
#!/bin/bash
# Executes main.py using the virtual environment's Python interpreter automatically
${PROJECT_PATH}/venv/bin/python ${PROJECT_PATH}/main.py "\$@"
EOF

# 3. Make the wrapper script executable
chmod +x py-pdf-editor

# 4. Move it to the local system binary folder
sudo mv py-pdf-editor /usr/local/bin/
```

### Global Usage Examples
Now you can close your terminal, open a new one in any folder (e.g., your Downloads or Documents directory), and use the tool directly.

#### 1. Launching the GUI
If you want to use the graphical window, simply type the command without any arguments:
```bash
py-pdf-editor
```


#### 2. Extracting Pages via CLI
To extract an interval of pages (e.g., pages 3 to 10) from a PDF located in your current directory:
```bash
py-pdf-editor extract -i document.pdf -o extracted.pdf -r 3-10
```

#### 3. Mergins PDFs via CLI
To merge multiple PDF files in sequence into a single output file:
```bash
py-pdf-editor merge -i part1.pdf part2.pdf part3.pdf -o final_merged.pdf
```
