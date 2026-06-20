import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURATION ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- 2. THE WEBPAGE LAYOUT ---
st.set_page_config(page_title="AI Resume Upgrader", page_icon="🚀", layout="centered")

st.title("🚀 Smart AI Resume Analyzer & Outreach Agent")
st.subheader("Beat the ATS & generate personalized networking emails instantly!")

# Input boxes for the user
job_description = st.text_area("📋 Paste the Job Description here:", height=150)
resume_text = st.text_area("📄 Paste your Resume Text here:", height=200)

# Create two action buttons
col1, col2 = st.columns(2)

with col1:
    analyze_button = st.button("📊 Analyze Match Score")

with col2:
    email_button = st.button("✉️ Generate Cold LinkedIn Message")

# --- 3. THE AI LOGIC ---
model = genai.GenerativeModel('gemini-2.5-flash')

if analyze_button:
    if job_description and resume_text:
        with st.spinner("Analyzing your resume against the job..."):
            prompt = f"""
            You are an expert HR Manager and ATS system. Analyze this resume against the job description.
            
            Job Description: {job_description}
            Resume: {resume_text}
            
            Provide the output in this exact structure:
            1. **ATS Match Score**: Give a percentage (e.g., 75%).
            2. **Missing Keywords & Skills**: List key terms or technologies present in the job description but missing or weak in the resume.
            3. **Actionable Roadmap**: Give 2-3 specific bullet points on how the user can improve this resume for this job.
            """
            response = model.generate_content(prompt)
            st.success("Analysis Complete!")
            st.markdown(response.text)
    else:
        st.warning("Please fill in both the Job Description and Resume boxes!")

if email_button:
    if job_description and resume_text:
        with st.spinner("Crafting a winning networking message..."):
            prompt = f"""
            Based on this candidate's resume and the target job description, write a highly professional, short, and compelling LinkedIn connection request or cold email (under 150 words). 
            It should highlight a strong skill from the resume that matches the job, sound enthusiastic, and ask politely for a short chat.
            
            Job Description: {job_description}
            Resume: {resume_text}
            """
            response = model.generate_content(prompt)
            st.success("Your Custom Outreach Message is Ready!")
            st.code(response.text, language="markdown")
    else:
        st.warning("Please fill in both the Job Description and Resume boxes!")