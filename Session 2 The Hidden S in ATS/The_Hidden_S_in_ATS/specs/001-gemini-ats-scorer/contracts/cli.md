# CLI Contract

## Command
`gemini-ats-scorer evaluate`

## Arguments
- `--resume` (required): Path to the candidate's PDF resume.
- `--job` (required): Path to the job description text file.
- `--format` (optional): Output format (`text` or `json`). Default: `text`.

## Example Usage
```bash
gemini-ats-scorer evaluate --resume ./candidate.pdf --job ./job_description.txt --format json
```

## Standard Streams
- `stdout`: Structured evaluation result (JSON or formatted text).
- `stderr`: Parsing errors, API timeouts, or validation errors (e.g., "Error: Resume PDF is scanned and contains no text").
