# Quickstart: ATS Web UI

1. Ensure the core library and UI dependencies are installed:
   ```bash
   pip install -e .[ui]
   ```
   *(Note: The `[ui]` extra will include `streamlit`)*

2. Set your Google Gemini API key:
   ```bash
   export GEMINI_API_KEY="your-api-key"
   ```

3. Start the Web UI server:
   ```bash
   streamlit run src/gemini_ats_scorer/ui/app.py
   ```

4. Open your browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`).
5. Upload a PDF resume, paste a job description, and click **Evaluate**.
