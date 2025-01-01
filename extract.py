import nbformat

# Load the notebook
with open("data_zscore.ipynb", "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Extract code cells
code_cells = [cell["source"] for cell in notebook.cells if cell.cell_type == "code"]

# Save to a Python file
with open("extracted_code.py", "w", encoding="utf-8") as f:
    f.write("\n\n".join(code_cells))
