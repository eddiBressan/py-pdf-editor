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