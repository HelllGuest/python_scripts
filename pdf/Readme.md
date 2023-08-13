# Remove PDF Metadata 

This is a simple Python script to remove metadata from PDF files using PyPDF2.

## Usage

To use the script:

```bash
python remove_pdf_metadata.py <input_pdf>  
```

This will overwrite the input PDF file with a new copy that has all metadata removed.

The input PDF file path should be specified as the first argument. 

Example:

```bash
python remove_pdf_metadata.py report.pdf
```

This will create a new report.pdf file without any metadata.

## Requirements

- Python 3
- PyPDF2 

Install PyPDF2:

```bash
pip install PyPDF2
```

## How it Works

The script uses PyPDF2 to read the input PDF and write a new copy without metadata:

- PdfReader opens the PDF and reads pages
- PdfWriter creates a new PDF file 
- Pages are copied from the reader to the writer
- The new PDF is written to the same file path

This strips all metadata fields including title, author, creator, producer, subject etc. while preserving all page content and formatting.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it as you wish.