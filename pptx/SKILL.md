---
name: pptx
description: >
  PowerPoint presentation handler for creating, reading, and editing .pptx files.
  Use when: (1) creating slide decks or presentations, (2) reading/extracting from .pptx,
  (3) editing existing presentations, (4) working with templates, layouts, speaker notes.
  Triggers: "PowerPoint", "presentation", ".pptx", "slides", "slide deck",
  "pitch deck", "slideshow", "deck", "speaker notes".
---

# PowerPoint Presentation Handler

Create, read, and edit Microsoft PowerPoint (.pptx) presentations with python-pptx.

## Capabilities

- Create new presentations from scratch
- Read and extract text from existing .pptx files
- Edit, modify, and update presentations
- Work with templates, layouts, and masters
- Add images, charts, tables, and shapes
- Manage speaker notes and comments
- Combine or split slide files

## Python Library

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RgbColor
from pptx.enum.shapes import MSO_SHAPE
```

## Common Operations

### Create New Presentation
```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()

# Add title slide
slide_layout = prs.slide_layouts[0]  # Title Slide
slide = prs.slides.add_slide(slide_layout)

title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "My Presentation"
subtitle.text = "Subtitle goes here"

prs.save("presentation.pptx")
```

### Add Content Slide
```python
# Title and Content layout
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)

title = slide.shapes.title
title.text = "Slide Title"

# Add bullet points
body = slide.placeholders[1]
tf = body.text_frame
tf.text = "First bullet point"

p = tf.add_paragraph()
p.text = "Second bullet point"
p.level = 0

p = tf.add_paragraph()
p.text = "Sub-bullet"
p.level = 1
```

### Add Image
```python
from pptx.util import Inches

slide_layout = prs.slide_layouts[5]  # Blank
slide = prs.slides.add_slide(slide_layout)

# Add image
left = Inches(1)
top = Inches(1)
width = Inches(4)
slide.shapes.add_picture("image.png", left, top, width=width)
```

### Add Table
```python
from pptx.util import Inches

rows, cols = 3, 4
left = Inches(1)
top = Inches(2)
width = Inches(8)
height = Inches(2)

table = slide.shapes.add_table(rows, cols, left, top, width, height).table

# Set header row
table.cell(0, 0).text = "Header 1"
table.cell(0, 1).text = "Header 2"

# Add data
table.cell(1, 0).text = "Data 1"
table.cell(1, 1).text = "Data 2"
```

### Add Shape
```python
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches

left = Inches(1)
top = Inches(1)
width = Inches(2)
height = Inches(1)

shape = slide.shapes.add_shape(
    MSO_SHAPE.ROUNDED_RECTANGLE,
    left, top, width, height
)
shape.text = "Click here"
```

### Format Text
```python
from pptx.util import Pt
from pptx.dml.color import RgbColor

paragraph = shape.text_frame.paragraphs[0]
run = paragraph.runs[0]

run.font.name = "Arial"
run.font.size = Pt(24)
run.font.bold = True
run.font.color.rgb = RgbColor(0x00, 0x66, 0xCC)
```

### Add Speaker Notes
```python
notes_slide = slide.notes_slide
notes_tf = notes_slide.notes_text_frame
notes_tf.text = "Remember to mention the key points here."
```

### Read Existing Presentation
```python
prs = Presentation("existing.pptx")

for slide in prs.slides:
    for shape in slide.shapes:
        if hasattr(shape, "text"):
            print(shape.text)
```

### Extract Text
```python
def extract_text(pptx_path):
    prs = Presentation(pptx_path)
    text_content = []

    for slide_num, slide in enumerate(prs.slides, 1):
        slide_text = f"--- Slide {slide_num} ---\n"
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                slide_text += shape.text + "\n"
        text_content.append(slide_text)

    return "\n".join(text_content)
```

## Slide Layouts

| Index | Name | Description |
|-------|------|-------------|
| 0 | Title Slide | Title and subtitle |
| 1 | Title and Content | Title with bullet points |
| 2 | Section Header | Section divider |
| 3 | Two Content | Two columns |
| 4 | Comparison | Side-by-side comparison |
| 5 | Title Only | Just title, blank content |
| 6 | Blank | Completely blank |

## Design Tips

1. **Consistency** - Use the same fonts and colors throughout
2. **White space** - Don't overcrowd slides
3. **Images** - High resolution, properly positioned
4. **Fonts** - Max 2 font families, readable sizes (24pt+ for body)
5. **Colors** - High contrast, limited palette
6. **Bullet points** - Max 6 per slide, short phrases

## Best Practices

- Start with a template for consistent styling
- Use master slides for global changes
- Keep text minimal, use visuals
- Add speaker notes for context
- Test on different screen sizes
