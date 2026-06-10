# imports
import streamlit as st
from utils import clean_text, extract_pdf_text, analyze

st.title("📄 Resume Analyzer AI (ATS System)")
st.write("Upload Resume in (PDF) format and compare with job description")
# Resume Upload
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job Description
job_text = st.text_area("Paste Job Description")

if st.button("Analyze"):

    if resume_file is not None:

        # PDF → text
        resume_text = extract_pdf_text(resume_file)

        # cleanning text
        resume_text = clean_text(resume_text)
        job_text_clean = clean_text(job_text)

        # analysing 
        result = analyze(resume_text, job_text_clean)

        st.markdown("## Results")

        st.metric("Overall Similarity",f"{result['overall_score']}%")
        st.metric("Skills Match", f"{result['skill_score']}%")

        st.markdown("### Matched Skills")
        if result["matched"]:
            st.success("✔".join(result["matched"]))
        else:
            st.warning("No matched skills found")

        st.markdown("### Missing Skills")
        if result["missing"]:
            st.error("✖".join(result["missing"]))
        else:
            st.success("No missing skills")

        st.markdown("### Recommendation")
        rec = result["recommendation"]
        if rec == "Highly Suitable":
            st.success(rec)
        elif rec == "Suitable":
            st.info(rec)
        elif rec == "Moderately Suitable":
            st.warning(rec)
        else:
            st.error(rec)
        st.markdown("### skill Match Progress")
        st.progress(int(result["skill_score"]) / 100)