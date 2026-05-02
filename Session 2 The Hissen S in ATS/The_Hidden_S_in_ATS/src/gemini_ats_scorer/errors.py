class GeminiAtsScorerError(Exception):
    """Base exception for gemini_ats_scorer"""
    pass

class PDFParseError(GeminiAtsScorerError):
    """Raised when there is an issue parsing the PDF (e.g., scanned or unreadable)"""
    pass

class EvaluatorError(GeminiAtsScorerError):
    """Raised when there is an issue with the Gemini evaluation API"""
    pass
