import pytest
import sys
from unittest.mock import patch

def test_app_imports_successfully():
    # Streamlit requires a running context for full AppTest, but we can verify
    # it imports without errors (e.g. syntax errors, missing dependencies).
    with patch("streamlit.set_page_config"):
        import gemini_ats_scorer.ui.app
        assert callable(gemini_ats_scorer.ui.app.main)
