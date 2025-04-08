
# Ensure pdfplumber is installed by running `pip install pdfplumber` in your terminal.
import os
from typing import List
import pdfplumber


class PDFFileLoader:
    def __init__(self, path: str):
        self.documents = []
        self.path = path

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path) and self.path.endswith(".pdf"):
            self.load_file()
        else:
            raise ValueError("Provided path is neither a valid directory nor a .pdf file.")

    def load_file(self):
        with pdfplumber.open(self.path) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
            self.documents.append(full_text)

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".pdf"):
                    full_path = os.path.join(root, file)
                    with pdfplumber.open(full_path) as pdf:
                        full_text = ""
                        for page in pdf.pages:
                            text = page.extract_text()
                            if text:
                                full_text += text + "\n"
                        self.documents.append(full_text)

    def load_documents(self):
        self.load()
        return self.documents


# You can reuse the same CharacterTextSplitter class from your original code.

if __name__ == "__main__":
    loader = PDFFileLoader("data/SomePDFFile.pdf")  # or directory path
    loader.load()
    splitter = CharacterTextSplitter()
    chunks = splitter.split_texts(loader.documents)
    print(f"Number of chunks: {len(chunks)}")
    print("Sample chunk 1:\n", chunks[0])
    print("--------")
    print("Sample chunk 2:\n", chunks[1])

