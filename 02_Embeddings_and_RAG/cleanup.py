import nbformat

# === CHANGE THIS to your notebook's path ===
notebook_path = "/Users/ashurveer/Projects/MP_AI/AIE6/02_Embeddings_and_RAG/Pythonic_RAG_Assignment.ipynb"

# Load the notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove broken widgets metadata
if "widgets" in nb.metadata:
    print("Removing corrupted 'widgets' metadata...")
    del nb.metadata["widgets"]
else:
    print("No 'widgets' metadata found – nothing to fix.")

# Save the fixed notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook fixed! You can now open it in Jupyter without error.")
