# imports
import streamlit as st
from utils import clean_text, extract_pdf_text, analyze

st.title("📄 Resume Analyzer AI (ATS System)")
st.write("Upload Resume in (PDF) format and compare with job description")
# Resume Upload
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job Description
job_text = st.text_area("Paste Job Description")

# Analyse Button
if st.button("Analyze Resume"):

    if resume_file is not None:

        # PDF → text
        resume_text = extract_pdf_text(resume_file)

        # cleanning text
        resume_text = clean_text(resume_text)
        job_text_clean = clean_text(job_text)

        # analysing 
        result = analyze(resume_text, job_text_clean)

        st.write("## Results")

        st.write(f"Overall Similarity: {result['overall_score']}%")
        st.write(f"Skills Match: {result['skill_score']}%")

        st.write("### Matched Skills")
        for s in result["matched"]:
            st.write("✔", s)

        st.write("### Missing Skills")
        for s in result["missing"]:
            st.write("✖", s)

        st.write("### Recommendation")
        st.success(result["recommendation"])

    else:
        st.error("Please upload a resume in PDF format and enter job description")