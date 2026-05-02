import pytest
from gemini_ats_scorer.lib.parser import parse_pdf
from gemini_ats_scorer.errors import PDFParseError

def test_parse_pdf_raises_error_for_invalid_file():
    with pytest.raises(PDFParseError):
        parse_pdf("nonexistent_file.pdf")
