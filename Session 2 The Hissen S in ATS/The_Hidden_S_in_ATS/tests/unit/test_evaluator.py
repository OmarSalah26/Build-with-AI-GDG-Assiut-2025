import pytest
from gemini_ats_scorer.lib.evaluator import evaluate_resume

def test_evaluate_resume_signature():
    assert callable(evaluate_resume)
