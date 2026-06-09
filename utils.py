import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


SKILLS = [
    "python","pandas","numpy","matplotlib","seaborn","javascript","sql",
    "power bi","machine learning","tableau","excel","mysql","postgresql",
    "mongodb","scikit-learn","tensorflow","random forest","decision tree",
    "neural networks","hadoop","spark","aws","azure","gcp","git","jira"
]


def extract_pdf_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill.lower() in text:
            found.append(skill)
    return found


def match_score(resume_text, job_text):
    docs = [resume_text, job_text]
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(docs)
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(score * 100, 2)


def analyze(resume_text, job_text):
    resume_text = clean_text(resume_text)
    job_text = clean_text(job_text)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched = set(resume_skills) & set(job_skills)
    missing = set(job_skills) - set(resume_skills)

    skill_score = (len(matched) / len(job_skills)) * 100 if job_skills else 0
    overall_score = match_score(resume_text, job_text)

    if skill_score >= 80:
        recommendation = "Highly Suitable"
    elif skill_score >= 60:
        recommendation = "Suitable"
    elif skill_score >= 40:
        recommendation = "Moderately Suitable"
    else:
        recommendation = "Not Suitable"

    return {
        "overall_score": overall_score,
        "skill_score": skill_score,
        "matched": list(matched),
        "missing": list(missing),
        "recommendation": recommendation
    }