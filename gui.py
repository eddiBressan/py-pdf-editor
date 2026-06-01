import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from pdf_engine import pdf_merger, pdf_extractor



class PdfGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Linux PDF Editor")
        self.root.geometry("450x250")
        self.root.resizable(False,False)

        tk.Label(
            root,
            text="PDF Manipulation Tool",
            font=("Helvetica", 16, "bold"),
            pady=20
        ).pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.merge_btn = tk.Button(
            btn_frame,
            text="Merge PDFs",
            command=self.gui_merge,
            width=20,
            height=2,
            font=("Helvetica", 11)
        )
        self.merge_btn.grid(row=0, column=0, padx=10)

        self.extract_btn = tk.Button(
            btn_frame,
            text="Extract Pages",
            command=self.gui_extract,
            width=20,
            height=2,
            font=("Helvetica", 11)
        )
        self.extract_btn.grid(row=0, column=1, padx=10)

        tk.Label(
            root,
            text="Select an operation to start",
            fg="gray"
        ).pack(side="bottom", pady=15)

    def gui_merge(self):
        files= filedialog.askopenfilenames(
            title="Select PDF files to merge",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if not files:
            return

        output = filedialog.asksaveasfilename(
            title="Save merged PDF as...",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if not output:
            return
        
        try:
            pdf_merger(files,output)
            messagebox.showinfo("Success", f"PDFs merged successfully!\nSaved to: {output}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

        
    def gui_extract(self):
        file = filedialog.askopenfilename(
            title="Select source PDF file",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if not file:
            return
        
        interval = simpledialog.askstring(
            "Page Range",
            "Enter range (ex: 3-10) or single page (ex: 5):"
        )
        if not interval:
            return
        
        output = filedialog.asksaveasfilename(
            title="Save extracted PDF as ...",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if not output:
            return
        
        try:
            pdf_extractor(file, output, interval)
            messagebox.showinfo("Success", f"Pages extracted successfully!\nSaved to: {output}")
        except Exception as e:
            messagebox.showerror("Error", str(e))