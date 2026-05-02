# Data Model

## Entity: EvaluationRecord
Represents a saved result of an ATS scoring evaluation in the SQLite database.

**Fields**:
- `id`: Integer (Primary Key, Auto-increment)
- `resume_filename`: String (Original uploaded filename)
- `job_description_snippet`: String (First 100 characters of the JD for display)
- `score`: Integer (0-100)
- `strengths`: String (JSON encoded list of strengths)
- `weaknesses`: String (JSON encoded list of weaknesses)
- `summary`: Text
- `created_at`: Datetime (Timestamp of evaluation)

**Relationships**:
- None (Standalone entity for a single-user system)

**Validation Rules**:
- `score` must be between 0 and 100.
- `strengths` and `weaknesses` must be valid JSON strings.
