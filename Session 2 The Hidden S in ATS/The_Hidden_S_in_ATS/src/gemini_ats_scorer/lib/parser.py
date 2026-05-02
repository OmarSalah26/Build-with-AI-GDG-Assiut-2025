import fitz # PyMuPDF
from gemini_ats_scorer.errors import PDFParseError

def parse_pdf(file_path: str) -> str:
    try:
        doc = fitz.open(file_path)
    except Exception as e:
        raise PDFParseError(f"Failed to open PDF {file_path}: {e}")
        
    text = ""
    for page in doc:
        text += page.get_text()
        
    if not text.strip():
        raise PDFParseError(f"No text could be extracted from {file_path}. It might be a scanned image.")
        
    return text.strip()
