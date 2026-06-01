import sys
import argparse
# Importiamo le funzioni logiche per la CLI
from pdf_engine import pdf_merger, pdf_extractor

def run_cli():
    parser = argparse.ArgumentParser(
        description="CLI pdf manipulation tool."
    )

    subparsers = parser.add_subparsers(dest="command", required=True, help="Sub-commands available!")
    #merge command configuration
    merge_parser = subparsers.add_parser("merge", help="Merge multiple files into one")
    merge_parser.add_argument("-i", "--input", nargs="+", required=True, help="List of PDF files to merge")
    merge_parser.add_argument("-o", "--output", required=True, help="Path for the output merged PDF")
    #extract command configuration
    extract_parser = subparsers.add_parser("extract", help="Extract a page range or single page from a PDF")
    extract_parser.add_argument("-i", "--input", required=True, help="Source PDF file")
    extract_parser.add_argument("-o", "--output", required=True, help="Path for the output extracted PDF")
    extract_parser.add_argument("-r", "--range", required=True, help="Interval (ex: 3-10) or single page (ex: 5)")

    args = parser.parse_args()

    try:
        if args.command == "merge":
            pdf_merger(args.input, args.output)
            print(f"Success! PDFs merged into: {args.output}")

        elif args.command == "extract":
            pdf_extractor(args.input, args.output, args.range)
            print(f"Success! Pages extracted into: {args.output}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_cli()
    else:
        import tkinter as tk
        from gui import PdfGui
        
        root = tk.Tk()
        app = PdfGui(root)
        root.mainloop()