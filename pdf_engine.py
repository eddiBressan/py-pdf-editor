#!/usr/bin/env python3
import os, sys
from pypdf import PdfReader, PdfWriter
from pathlib import Path




def input_file_validation(input_path):
    path = Path(input_path)

    if not path.exists():
        raise FileNotFoundError(f"Error: File '{path}' not exists.")
    if not path.is_file():
        raise IsADirectoryError(f"Error: '{path}' it's a folder, not a file.")
    if path.suffix.lower() != '.pdf':
        raise ValueError(f"Error: File '{path}' it's not a PDF.")
    
    return path


def output_path_validation(output_path):
    path = Path(output_path)

    destination_folder = path.parent
    if not destination_folder.exists():
        raise FileNotFoundError(f"Error: Destination folder {destination_folder} doesn't exists.")

    return path


def pdf_merger(input_file_list, output_path):
    output_path_validation(output_path)

    resolved_output = Path(output_path).resolve()
    if resolved_output in [Path(f).resolve() for f in input_file_list]:
        raise ValueError("Error: Output file cannot be one of the input files!")

    for file in input_file_list:
        input_file_validation(file)

    writer = PdfWriter()
    for file in input_file_list:
        writer.append(file)

    with open(output_path, "wb") as f:
        writer.write(f)


def pdf_extractor(input_file, output_path, interval):
    input_file_validation(input_file)
    output_path_validation(output_path)

    if Path(input_file).resolve() == Path(output_path).resolve():
        raise ValueError("Error: Input file and Output file cannot be the same file!")

    reader = PdfReader(input_file)
    total_pages = len(reader.pages)

    try:
        interval = interval.replace(" ", "")
        if "-" in interval:
            input_inf = int(interval.split("-")[0])
            input_sup = int(interval.split("-")[1])
        else:
            input_inf = int(interval)
            input_sup = int(interval)
    except ValueError:
        raise ValueError("Format not valid! Use 'start-end' notation (ex: 3-10) or a single number (ex: 10).")
    
    inf = input_inf - 1
    sup = input_sup
    
    if inf < 0 or sup < 0 or inf >= sup or inf >= total_pages or sup > total_pages:
        raise ValueError(f"Interval not valid for a document of {total_pages} pages!")
    
    writer = PdfWriter()

    for page in range(inf,sup):
        tmp = reader.pages[page]
        writer.add_page(tmp)
    
    with open(output_path, "wb") as f:
        writer.write(f)



