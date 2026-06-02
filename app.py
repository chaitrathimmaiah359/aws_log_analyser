import streamlit as st

from analyzer.parser import extract_errors
from analyzer.ai_summary import summarize

st.title("AWS Log Analyzer")

uploaded = st.file_uploader(
    "Upload Log File"
)

if uploaded:

    content = uploaded.read().decode()

    errors = extract_errors(content)

    st.subheader("Detected Errors")

    for err in errors:
        st.write(err)

    if st.button("Analyze"):

        summary = summarize(errors)

        st.subheader("AI Analysis")

        st.write(summary)