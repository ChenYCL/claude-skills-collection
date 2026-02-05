---
name: pdf
description: >
  PDF processing toolkit for reading, creating, merging, splitting, and manipulating PDF files.
  Use when: (1) extracting text/tables from PDFs, (2) merging or splitting PDFs,
  (3) creating new PDFs, (4) filling PDF forms, (5) adding watermarks,
  (6) OCR on scanned documents, (7) encrypting/decrypting PDFs.
  Triggers: "PDF", ".pdf", "merge PDF", "split PDF", "extract text",
  "fill form", "watermark", "OCR", "scan", "combine PDFs".
---

# PDF Processing Toolkit

Comprehensive PDF manipulation for extracting text, merging documents, filling forms, and more.

## Capabilities

- Extract text and tables from PDFs
- Merge multiple PDFs into one
- Split PDFs into separate files
- Rotate, reorder pages
- Add watermarks and annotations
- Fill PDF forms
- Encrypt/decrypt PDFs
- OCR scanned documents
- Extract images

## Python Libraries

```python
# Text extraction
import pdfplumber  # Best for tables
from PyPDF2 import PdfReader, PdfWriter  # Merge, split, rotate

# Creating PDFs
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# OCR (optional)
import pytesseract
from pdf2image import convert_from_path
```

## Common Operations

### Extract Text
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

### Extract Tables
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    page = pdf.pages[0]
    tables = page.extract_tables()
    for table in tables:
        for row in table:
            print(row)
```

### Merge PDFs
```python
from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf")
merger.append("file3.pdf")
merger.write("merged.pdf")
merger.close()
```

### Split PDF
```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("document.pdf")

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as f:
        writer.write(f)
```

### Rotate Pages
```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.rotate(90)  # Rotate 90 degrees clockwise
    writer.add_page(page)

with open("rotated.pdf", "wb") as f:
    writer.write(f)
```

### Create New PDF
```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("new_document.pdf", pagesize=letter)
width, height = letter

# Add text
c.setFont("Helvetica", 12)
c.drawString(72, height - 72, "Hello, World!")

# Add rectangle
c.rect(72, height - 200, 200, 100)

c.save()
```

### Add Watermark
```python
from PyPDF2 import PdfReader, PdfWriter

# Create watermark first with reportlab
reader = PdfReader("document.pdf")
watermark = PdfReader("watermark.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.merge_page(watermark.pages[0])
    writer.add_page(page)

with open("watermarked.pdf", "wb") as f:
    writer.write(f)
```

### OCR Scanned PDF
```python
from pdf2image import convert_from_path
import pytesseract

# Convert PDF pages to images
images = convert_from_path("scanned.pdf")

# OCR each page
full_text = ""
for image in images:
    text = pytesseract.image_to_string(image)
    full_text += text + "\n"

print(full_text)
```

### Encrypt PDF
```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("password123")

with open("encrypted.pdf", "wb") as f:
    writer.write(f)
```

## Workflow Tips

1. **Text extraction** - Use pdfplumber for better accuracy with tables
2. **Large files** - Process page by page to manage memory
3. **Scanned docs** - Use OCR with pytesseract + pdf2image
4. **Form filling** - Use PyPDF2 or pdfrw for AcroForms
5. **Complex layouts** - Consider using reportlab for precise control

## Library Comparison

| Task | Best Library |
|------|--------------|
| Text extraction | pdfplumber |
| Table extraction | pdfplumber, camelot |
| Merge/split | PyPDF2 |
| Create new | reportlab |
| Fill forms | PyPDF2 |
| OCR | pytesseract + pdf2image |
