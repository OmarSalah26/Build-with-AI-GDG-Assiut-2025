# Quickstart

## Setup
1. Clone the repository and navigate to the project root.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Google Gemini API key:
   ```bash
   export GEMINI_API_KEY="your-api-key"
   ```

## Usage
Evaluate a resume against a job description:
```bash
python -m gemini_ats_scorer evaluate --resume path/to/resume.pdf --job path/to/job.txt
```
