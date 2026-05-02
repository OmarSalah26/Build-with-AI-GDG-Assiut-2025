import sqlite3
import json
from pathlib import Path
from typing import List, Optional
from datetime import datetime
from gemini_ats_scorer.models import EvaluationResult

DB_PATH = Path("ats_evaluations.db")


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS evaluation_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                resume_filename TEXT NOT NULL,
                job_description_snippet TEXT NOT NULL,
                score INTEGER NOT NULL,
                strengths TEXT NOT NULL,
                weaknesses TEXT NOT NULL,
                summary TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()


def save_evaluation(
    resume_filename: str, job_description: str, result: EvaluationResult
) -> int:
    snippet = job_description[:100] + ("..." if len(job_description) > 100 else "")
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO evaluation_records 
            (resume_filename, job_description_snippet, score, strengths, weaknesses, summary)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (
                resume_filename,
                snippet,
                result.score,
                json.dumps(result.strengths),
                json.dumps(result.weaknesses),
                result.summary,
            ),
        )
        conn.commit()
        return cursor.lastrowid


def get_all_evaluations() -> List[dict]:
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(
            "SELECT * FROM evaluation_records ORDER BY created_at DESC"
        )
        return [dict(row) for row in cursor.fetchall()]
