# Author
Farhat Ghani
# Resume-analyser
This is an AI powered resume analyser that would compare a candidate's resume with a job description and providing ATS style matching score, Skills matching percentage, missing skills identification, job suitability recommendation.
# Fetures would including
Upload Resume (PDF), paste Job Description, Extract Resume skills, compare resume with jobrequirements, calculating overall similarity score, identify missing skills additionally genrating recommendation.
##  Project structure
resume-analyser/
|---- app.py
|----utils.py
|----requirements.txt
|----README.md
|----sample_data/
## Technologies used
- Python
- Streamlit
- Scikit-Learn
- PDFMiner
- NLP Techniques
## Installation
Repository clonned with '''bash
- git clone < https://github.com/farhatghani/resume-analyser-ai.git >
- cd resume-analyser
To install dependencies bash
- pip install -r requirements.text
To run the application bash
- streamlit run app.py
# The output will print similarly
overall similarity: 38%
skills Match: 75%
Matched Skills:
Python
SQL
Machine Learning
Missing Skills:
Power BI
Recommendation:
Suitable

## Future Improvements
- AI techniques use to generate suggesionsfor update resume
- AI techniques use to generate cover letter
- AI techniques use to ranking resume
- Additionally, implement OCR support for scanned PDF file
- Furthermore, comparison of maultiple resume

