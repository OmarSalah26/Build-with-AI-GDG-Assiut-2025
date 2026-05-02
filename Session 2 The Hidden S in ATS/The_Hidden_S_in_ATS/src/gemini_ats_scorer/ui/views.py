import streamlit as st
import pandas as pd
import json
from gemini_ats_scorer.ui import db


def render_history():
    st.subheader("Evaluation History")
    records = db.get_all_evaluations()

    if not records:
        st.info("No evaluations yet.")
        return

    display_records = []
    for r in records:
        display_records.append(
            {
                "ID": r["id"],
                "Resume": r["resume_filename"],
                "JD Snippet": r["job_description_snippet"],
                "Score": r["score"],
                "Date": r["created_at"],
            }
        )

    df = pd.DataFrame(display_records)
    st.dataframe(df, hide_index=True, use_container_width=True)

    st.write("### View Details")
    selected_id = st.selectbox(
        "Select ID to view details", options=[r["id"] for r in records]
    )
    if selected_id:
        record = next(r for r in records if r["id"] == selected_id)
        st.write(f"**Score:** {record['score']}/100")
        st.write("**Summary:**")
        st.write(record["summary"])

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Strengths:**")
            for s in json.loads(record["strengths"]):
                st.write(f"- {s}")
        with col2:
            st.write("**Weaknesses:**")
            for w in json.loads(record["weaknesses"]):
                st.write(f"- {w}")


def render_evaluation_result(result):
    st.success(f"Score: {result.score}/100")
    st.write("### Summary")
    st.write(result.summary)

    col1, col2 = st.columns(2)
    with col1:
        st.write("### Strengths")
        for s in result.strengths:
            st.write(f"- {s}")
    with col2:
        st.write("### Weaknesses")
        for w in result.weaknesses:
            st.write(f"- {w}")
