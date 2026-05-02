import pytest
import sqlite3
import json
from gemini_ats_scorer.ui import db
from gemini_ats_scorer.models import EvaluationResult

@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_path = tmp_path / "test_ats.db"
    monkeypatch.setattr(db, "DB_PATH", db_path)
    db.init_db()
    return db_path

def test_init_db_creates_table(test_db):
    conn = sqlite3.connect(test_db)
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='evaluation_records'")
    assert cursor.fetchone() is not None

def test_save_and_get_evaluations(test_db):
    result = EvaluationResult(
        score=95,
        strengths=["Python", "SQL"],
        weaknesses=["Java"],
        summary="Great candidate"
    )
    
    db.save_evaluation("test_resume.pdf", "We need a Python dev", result)
    
    records = db.get_all_evaluations()
    assert len(records) == 1
    assert records[0]["resume_filename"] == "test_resume.pdf"
    assert records[0]["score"] == 95
    assert json.loads(records[0]["strengths"]) == ["Python", "SQL"]
