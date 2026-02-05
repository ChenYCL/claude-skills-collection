---
name: xlsx
description: >
  Excel spreadsheet handler for creating, reading, editing, and analyzing .xlsx files.
  Use when: (1) working with spreadsheet files (.xlsx, .xlsm, .csv, .tsv),
  (2) adding columns, computing formulas, formatting, charting,
  (3) cleaning messy tabular data, (4) converting between tabular formats.
  Triggers: "spreadsheet", "excel", ".xlsx", "csv", "add column", "formula",
  "chart", "pivot table", "data cleaning", "tabular data".
---

# Excel Spreadsheet Handler

Comprehensive Microsoft Excel (.xlsx) document creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization.

## Capabilities

- Create new spreadsheets from scratch or data sources
- Read, edit, and fix existing .xlsx, .xlsm, .csv, .tsv files
- Add columns, rows, formulas, and formatting
- Create charts, pivot tables, and data visualizations
- Clean and restructure messy tabular data
- Convert between tabular file formats

## Python Libraries

```python
# Primary: openpyxl for .xlsx
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Fill, Alignment, Border
from openpyxl.chart import BarChart, LineChart, PieChart
from openpyxl.utils.dataframe import dataframe_to_rows

# For data manipulation
import pandas as pd

# For CSV/TSV
import csv
```

## Common Operations

### Create New Workbook
```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"

# Add headers
headers = ["Name", "Value", "Date"]
ws.append(headers)

# Add data
ws.append(["Item A", 100, "2024-01-15"])
ws.append(["Item B", 200, "2024-01-16"])

wb.save("output.xlsx")
```

### Read and Modify
```python
from openpyxl import load_workbook

wb = load_workbook("input.xlsx")
ws = wb.active

# Read cell
value = ws["A1"].value

# Write cell
ws["B2"] = "New Value"

# Add formula
ws["C2"] = "=SUM(A2:B2)"

wb.save("modified.xlsx")
```

### Formatting
```python
from openpyxl.styles import Font, PatternFill, Alignment

# Bold header
ws["A1"].font = Font(bold=True, size=12)

# Fill color
ws["A1"].fill = PatternFill("solid", fgColor="FFFF00")

# Center align
ws["A1"].alignment = Alignment(horizontal="center")

# Column width
ws.column_dimensions["A"].width = 20
```

### Charts
```python
from openpyxl.chart import BarChart, Reference

chart = BarChart()
chart.title = "Sales Data"
data = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=5)
categories = Reference(ws, min_col=1, min_row=2, max_row=5)
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
ws.add_chart(chart, "E2")
```

### Pandas Integration
```python
import pandas as pd

# Read Excel to DataFrame
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Process data
df["Total"] = df["Price"] * df["Quantity"]

# Write back to Excel
df.to_excel("output.xlsx", index=False)
```

## Formula Reference

| Formula | Description | Example |
|---------|-------------|---------|
| SUM | Add values | `=SUM(A1:A10)` |
| AVERAGE | Calculate mean | `=AVERAGE(B1:B10)` |
| COUNT | Count numbers | `=COUNT(A1:A10)` |
| IF | Conditional | `=IF(A1>10,"High","Low")` |
| VLOOKUP | Vertical lookup | `=VLOOKUP(A1,B:C,2,FALSE)` |
| SUMIF | Conditional sum | `=SUMIF(A:A,"Yes",B:B)` |

## Data Cleaning Workflow

1. **Load data** - Read the messy file
2. **Identify issues** - Missing headers, junk rows, wrong types
3. **Clean headers** - Standardize column names
4. **Remove junk** - Delete empty/invalid rows
5. **Fix types** - Convert strings to numbers/dates
6. **Validate** - Check data integrity
7. **Export** - Save clean spreadsheet

## Best Practices

- Always create backups before modifying
- Use named ranges for complex formulas
- Document formulas with comments
- Validate data types before calculations
- Use conditional formatting for data visualization
