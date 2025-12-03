import fitz  # PyMuPDF

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from all pages of a PDF."""
    text = ""
    with fitz.open(file_path) as doc:
        for i, page in enumerate(doc):
            page_text = page.get_text("text")
            text += page_text + "\n"
            print(f"✅ Extracted page {i + 1} ({len(page_text)} chars)")
    return text.strip()
