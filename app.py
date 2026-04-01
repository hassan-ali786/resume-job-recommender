import streamlit as st
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from predict import predict_resume
from utils import extract_text_from_pdf, extract_skills

st.set_page_config(page_title="Resume AI Premium", layout="wide")
st.markdown("<h1 style='text-align:center'>Resume Screening & Job Recommender</h1>", unsafe_allow_html=True)

file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if file:
    text = extract_text_from_pdf(file)
    role, confidence = predict_resume(text)
    skills = extract_skills(text)

    st.markdown(f"**Predicted Role:** {role}")
    st.progress(int(confidence*100))
    st.markdown(f"**Detected Skills:** {', '.join(skills) if skills else 'None'}")

    st.markdown("**Recommended Jobs:**")
    if role=="Data Science":
        jobs = ["Data Analyst","ML Engineer","Business Analyst"]
    elif role=="Web Designing":
        jobs = ["Frontend Developer","UI/UX Designer","React Developer"]
    elif role=="HR":
        jobs = ["HR Manager","Recruiter"]
    else:
        jobs = ["General Role"]
    
    for job in jobs:
        match = len([s for s in skills if s.lower() in job.lower()])*50
        st.markdown(f"- {job} (Match Score: {match}%)")