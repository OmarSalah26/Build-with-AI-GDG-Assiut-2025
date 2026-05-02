import streamlit as st
import tempfile
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
except ImportError:
    pass

from gemini_ats_scorer.ui.db import init_db, save_evaluation
from gemini_ats_scorer.ui.views import render_history, render_evaluation_result
from gemini_ats_scorer.lib.parser import parse_pdf
from gemini_ats_scorer.lib.evaluator import evaluate_resume
from gemini_ats_scorer.models import Resume, JobDescription
from gemini_ats_scorer.errors import GeminiAtsScorerError


def main():
    st.set_page_config(page_title="Gemini ATS Scorer", page_icon="📄", layout="wide")

    init_db()

    st.title("Gemini ATS Scorer")

    tab1, tab2 = st.tabs(["Evaluate Resume", "History"])

    with tab1:
        st.header("New Evaluation")

        uploaded_file = st.file_uploader("Upload candidate's PDF resume", type="pdf")
        job_description_text = st.text_area("Paste Job Description", height=200)

        if st.button("Evaluate", type="primary"):
            if not uploaded_file:
                st.error("Please upload a PDF resume.")
            elif not job_description_text.strip():
                st.error("Please enter a job description.")
            else:
                with st.spinner("Evaluating..."):
                    try:
                        with tempfile.NamedTemporaryFile(
                            delete=False, suffix=".pdf"
                        ) as tmp:
                            tmp.write(uploaded_file.getvalue())
                            tmp_path = tmp.name

                        try:
                            resume_text = parse_pdf(tmp_path)
                            resume = Resume(
                                file_path=uploaded_file.name, extracted_text=resume_text
                            )
                            jd = JobDescription(source_text=job_description_text)

                            result = evaluate_resume(resume, jd)

                            save_evaluation(
                                uploaded_file.name, job_description_text, result
                            )

                            render_evaluation_result(result)

                        finally:
                            os.unlink(tmp_path)

                    except GeminiAtsScorerError as e:
                        st.error(str(e))
                    except Exception as e:
                        st.error(f"An unexpected error occurred: {e}")

    with tab2:
        render_history()


if __name__ == "__main__":
    main()
