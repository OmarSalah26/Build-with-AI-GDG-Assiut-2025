# Data Model

## Entities

### `Resume`
Represents the candidate's parsed resume.
- `file_path`: str
- `extracted_text`: str
- `metadata`: dict (optional)

### `JobDescription`
Represents the target job requirements.
- `source_text`: str

### `EvaluationResult`
Represents the structured output from Gemini.
- `score`: int (0-100)
- `strengths`: list[str]
- `weaknesses`: list[str]
- `summary`: str
