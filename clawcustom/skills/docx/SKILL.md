---
name: docx
description: "Create, read, and edit Microsoft Word .docx files using Python. Supports paragraphs, tables, basic formatting, and text extraction."
metadata: {"nanobot":{"emoji":"📄","requires":{"bins":["python3"]},"install":[{"id":"pip","kind":"pip","package":"python-docx","bins":["python3"],"label":"Install python-docx (pip)"},{"id":"pip2","kind":"pip","package":"docx2txt","bins":["python3"],"label":"Install docx2txt (pip)"}]}}
---

# Docx Skill

Use Python libraries `python-docx` and `docx2txt` to work with .docx files.

## Installation

```bash
pip install python-docx docx2txt
```

## Reading Documents

### Extract all text from a document:

```python
import docx2txt

text = docx2txt.process("document.docx")
print(text)
```

### Read with python-docx (preserves structure):

```python
from docx import Document

doc = Document("document.docx")

# Print all paragraphs
for para in doc.paragraphs:
    print(para.text)

# Print tables
for table in doc.tables:
    for row in table.rows:
        print([cell.text for cell in row.cells])
```

### Get document metadata:

```python
from docx import Document

doc = Document("document.docx")
core_props = doc.core_properties
print(f"Author: {core_props.author}")
print(f"Title: {core_props.title}")
print(f"Created: {core_props.created}")
```

## Creating Documents

### Basic document with paragraphs:

```python
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Add heading
doc.add_heading("Document Title", 0)

# Add paragraph
doc.add_paragraph("This is a paragraph.")

# Add paragraph with styling
para = doc.add_paragraph("Styled text")
para.runs[0].bold = True
para.runs[0].font.size = Pt(14)

doc.save("output.docx")
```

### Add headings at different levels:

```python
doc.add_heading("Heading 1", level=1)
doc.add_heading("Heading 2", level=2)
doc.add_heading("Heading 3", level=3)
```

### Add lists:

```python
# Bullet list
doc.add_paragraph("Item 1", style="List Bullet")
doc.add_paragraph("Item 2", style="List Bullet")

# Numbered list
doc.add_paragraph("Step 1", style="List Number")
doc.add_paragraph("Step 2", style="List Number")
```

## Tables

### Create a table:

```python
from docx import Document

doc = Document()

# Add table with 3 rows, 3 columns
table = doc.add_table(rows=3, cols=3)

# Set header row
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Name"
hdr_cells[1].text = "Age"
hdr_cells[2].text = "City"

# Add data rows
row_cells = table.rows[1].cells
row_cells[0].text = "Alice"
row_cells[1].text = "30"
row_cells[2].text = "NYC"

doc.save("table.docx")
```

### Style a table:

```python
table.style = "Light Grid Accent 1"
```

## Images

### Add an image:

```python
from docx import Document
from docx.shared import Inches

doc = Document()
doc.add_picture("image.png", width=Inches(2))
doc.save("with-image.docx")
```

## Advanced

### Set page margins:

```python
from docx.shared import Inches
from docx.enum.text import WD_PARAGRAPH_ALIGN

section = doc.sections[0]
section.top_margin = Inches(1)
section.bottom_margin = Inches(1)
section.left_margin = Inches(1.25)
section.right_margin = Inches(1.25)
```

### Add page numbers:

Page numbers require a different approach - typically add to footer:
```python
section = doc.sections[0]
footer = section.footer
paragraph = footer.paragraphs[0]
paragraph.text = "Page %s of %s"  # Word will auto-fill
```

### Search and replace text:

```python
from docx import Document

doc = Document("input.docx")

for para in doc.paragraphs:
    if "old_text" in para.text:
        para.text = para.text.replace("old_text", "new_text")

doc.save("output.docx")
```
