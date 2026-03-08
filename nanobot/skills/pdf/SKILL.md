---
name: pdf
description: "Read, extract, and manipulate PDF files using Python. Supports text extraction, metadata, merging, splitting, and page operations."
metadata: {"nanobot":{"emoji":"📕","requires":{"bins":["python3"]},"install":[{"id":"pip","kind":"pip","package":"pypdf","bins":["python3"],"label":"Install pypdf (pip)"}]}}
---

# PDF Skill

Use the `pypdf` library (formerly PyPDF2) to work with PDF files.

## Installation

```bash
pip install pypdf
```

## Reading PDFs

### Extract all text from a PDF:

```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")

for page in reader.pages:
    print(page.extract_text())
```

### Extract text from specific pages:

```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")

# First page (0-indexed)
page = reader.pages[0]
print(page.extract_text())

# Multiple pages
for i in range(0, 3):
    print(reader.pages[i].extract_text())
```

### Get document metadata:

```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")

meta = reader.metadata
print(f"Title: {meta.get('/Title')}")
print(f"Author: {meta.get('/Author')}")
print(f"Subject: {meta.get('/Subject')}")
print(f"Creator: {meta.get('/Creator')}")
print(f"Producer: {meta.get('/Producer')}")
print(f"Creation date: {meta.get('/CreationDate')}")
```

### Get page count and info:

```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")

print(f"Number of pages: {len(reader.pages)}")

# Get page dimensions
first_page = reader.pages[0]
print(f"Page size: {first_page.mediabox}")
```

## Manipulating PDFs

### Merge PDFs:

```python
from pypdf import PdfWriter

merger = PdfWriter()

merger.append("file1.pdf")
merger.append("file2.pdf")
merger.append("file3.pdf")

merger.write("merged.pdf")
merger.close()
```

### Split PDF:

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
writer = PdfWriter()

# Extract first 3 pages
for page in reader.pages[:3]:
    writer.add_page(page)

writer.write("split.pdf")
writer.close()
```

### Extract specific pages:

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
writer = PdfWriter()

# Extract pages 5, 10, 15 (0-indexed)
for page_num in [5, 10, 15]:
    writer.add_page(reader.pages[page_num])

writer.write("extracted.pdf")
writer.close()
```

### Copy pages between PDFs:

```python
from pypdf import PdfReader, PdfWriter

src = PdfReader("source.pdf")
dst = PdfWriter()

# Copy all pages from source to destination
for page in src.pages:
    dst.add_page(page)

# Add additional pages
extra = PdfReader("extra.pdf")
for page in extra.pages:
    dst.add_page(page)

dst.write("combined.pdf")
```

## Extracting Images

### Extract images from a page:

```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")
page = reader.pages[0]

for image_file_object in page.images:
    with open(image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)
```

## Creating PDFs

### Create a simple PDF:

```python
from pypdf import PdfWriter

writer = PdfWriter()

# Add a blank page
writer.add_blank_page(width=612, height=792)  # Letter size

writer.write("blank.pdf")
writer.close()
```

Note: For rich PDF creation with text styling, images, and advanced layout, use `reportlab` or `fpdf` libraries instead.

## Advanced

### Rotate pages:

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.rotate(90)  # Rotate 90 degrees clockwise
    writer.add_page(page)

writer.write("rotated.pdf")
```

### Compress PDF:

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# Enable compression
writer.compress_content_streams()

writer.write("compressed.pdf")
```

### Check if PDF is encrypted:

```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")
print(f"Is encrypted: {reader.is_encrypted}")
```
