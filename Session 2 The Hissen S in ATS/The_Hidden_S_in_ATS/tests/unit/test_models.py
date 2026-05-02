import pytest
from pydantic import ValidationError
from gemini_ats_scorer.models import Resume, JobDescription, EvaluationResult

def test_evaluation_result_validation():
    result = EvaluationResult(
        score=85,
        strengths=["Python", "AWS"],
        weaknesses=["GCP"],
        summary="Good candidate"
    )
    assert result.score == 85
    
    with pytest.raises(ValidationError):
        EvaluationResult(score=150, strengths=[], weaknesses=[], summary="")
