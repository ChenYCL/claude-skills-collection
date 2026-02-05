---
name: canvas-design
description: >
  Create beautiful visual art and designs in .png and .pdf formats using Python graphics libraries.
  Use when: (1) creating posters, flyers, or promotional materials, (2) designing graphics,
  (3) creating visual art or illustrations, (4) generating static visual content.
  Triggers: "poster", "design", "create art", "visual", "graphic design",
  "flyer", "banner", "illustration", "infographic".
---

# Canvas Design

Create beautiful visual art in .png and .pdf formats using Python graphics libraries.

## Capabilities

- Create posters, flyers, and promotional materials
- Design graphics with shapes, text, and images
- Generate infographics and data visualizations
- Create original visual designs
- Export to PNG, PDF, SVG formats

## Python Libraries

```python
# Primary graphics
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import cairo  # For vector graphics

# For complex layouts
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

# For data visualizations
import matplotlib.pyplot as plt
import seaborn as sns
```

## Common Operations

### Create Canvas with PIL
```python
from PIL import Image, ImageDraw, ImageFont

# Create canvas
width, height = 1920, 1080
img = Image.new("RGB", (width, height), color="#FFFFFF")
draw = ImageDraw.Draw(img)

# Add rectangle
draw.rectangle([50, 50, 500, 300], fill="#3498DB", outline="#2980B9")

# Add text
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
draw.text((100, 100), "Hello World", font=font, fill="#FFFFFF")

# Save
img.save("design.png")
```

### Gradient Background
```python
from PIL import Image

def create_gradient(width, height, color1, color2):
    img = Image.new("RGB", (width, height))
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * y / height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / height)
        for x in range(width):
            img.putpixel((x, y), (r, g, b))
    return img

# Usage
gradient = create_gradient(1920, 1080, (52, 152, 219), (155, 89, 182))
gradient.save("gradient.png")
```

### Add Shapes
```python
from PIL import Image, ImageDraw

img = Image.new("RGB", (800, 600), "#FFFFFF")
draw = ImageDraw.Draw(img)

# Rectangle
draw.rectangle([50, 50, 200, 150], fill="#E74C3C")

# Rounded rectangle
draw.rounded_rectangle([250, 50, 400, 150], radius=20, fill="#3498DB")

# Circle
draw.ellipse([450, 50, 550, 150], fill="#2ECC71")

# Line
draw.line([50, 200, 550, 200], fill="#333333", width=3)

# Polygon
draw.polygon([(300, 250), (350, 350), (250, 350)], fill="#F39C12")

img.save("shapes.png")
```

### Typography
```python
from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (800, 400), "#1A1A2E")
draw = ImageDraw.Draw(img)

# Load fonts (system fonts)
title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Title
draw.text((50, 50), "Design Title", font=title_font, fill="#EAEAEA")

# Subtitle
draw.text((50, 140), "Creating beautiful visuals with Python", font=body_font, fill="#A0A0A0")

img.save("typography.png")
```

### Cairo Vector Graphics
```python
import cairo

# Create surface
width, height = 800, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Background
ctx.set_source_rgb(0.1, 0.1, 0.15)
ctx.paint()

# Draw circle
ctx.set_source_rgb(0.9, 0.3, 0.3)
ctx.arc(400, 300, 100, 0, 2 * 3.14159)
ctx.fill()

# Draw text
ctx.set_source_rgb(1, 1, 1)
ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(48)
ctx.move_to(300, 320)
ctx.show_text("Hello")

# Save
surface.write_to_png("vector.png")
```

### Create PDF Poster
```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

c = canvas.Canvas("poster.pdf", pagesize=A4)
width, height = A4

# Background
c.setFillColor(HexColor("#1A1A2E"))
c.rect(0, 0, width, height, fill=1)

# Title
c.setFillColor(HexColor("#FFFFFF"))
c.setFont("Helvetica-Bold", 36)
c.drawCentredString(width/2, height - 100, "Event Poster")

# Content
c.setFont("Helvetica", 18)
c.drawCentredString(width/2, height - 200, "Join us for an amazing event")

c.save()
```

## Design Principles

### Color Harmony
| Scheme | Description |
|--------|-------------|
| Complementary | Opposite colors on wheel |
| Analogous | Adjacent colors |
| Triadic | Three equally spaced |
| Split-complementary | One + two adjacent to complement |

### Typography Rules
1. **Hierarchy** - Size difference for importance
2. **Contrast** - Light text on dark, dark on light
3. **Spacing** - Adequate line height (1.5x font size)
4. **Limit fonts** - Max 2-3 font families
5. **Readability** - 16px+ for body text

### Layout Principles
1. **Rule of thirds** - Place key elements at intersections
2. **White space** - Don't overcrowd
3. **Alignment** - Consistent edges
4. **Proximity** - Group related elements
5. **Balance** - Visual weight distribution

## Color Palettes

### Modern Tech
```python
colors = {
    "primary": "#6C5CE7",
    "secondary": "#00CEC9",
    "accent": "#FD79A8",
    "dark": "#2D3436",
    "light": "#DFE6E9"
}
```

### Corporate
```python
colors = {
    "primary": "#2C3E50",
    "secondary": "#3498DB",
    "accent": "#E74C3C",
    "dark": "#1A252F",
    "light": "#ECF0F1"
}
```

### Nature
```python
colors = {
    "primary": "#27AE60",
    "secondary": "#2ECC71",
    "accent": "#F39C12",
    "dark": "#1E3A2F",
    "light": "#E8F6F3"
}
```

## Best Practices

1. **Start with wireframe** - Plan layout first
2. **Use grid** - Align elements consistently
3. **Consistent colors** - Define palette upfront
4. **High resolution** - Design at 2x for retina
5. **Test at size** - View at actual dimensions
6. **Accessibility** - Ensure contrast ratios (WCAG)
