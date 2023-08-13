import os
import sys
from PyPDF2 import PdfReader, PdfWriter

if len(sys.argv) < 2:
    print('Usage: python remove_pdf_metadata.py <pdf_file>')
    sys.exit(1)
    
pdf_path = sys.argv[1]

if not os.path.isfile(pdf_path):
    print('Error: Specified file does not exist')
    sys.exit(1)

if pdf_path.lower().endswith('.pdf'):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)

    with open(pdf_path, 'wb') as f:
        writer.write(f)

    print(f'Metadata removed from {pdf_path}')

else:
    print('Error: Invalid PDF file')