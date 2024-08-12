import streamlit as st
import meta_data

def Education_Details():
    with st.form("Education_Details"):
        meta_data.degree = st.text_input("Highest Degree Obtained (e.g., B.Tech, M.S.)")
        meta_data.discipline = st.text_input("Engineering Discipline (e.g., Computer Science, Electrical, etc.)")
        meta_data.institutions = st.text_area("Institutions Attended")
        meta_data.certifications = st.text_area("Relevant Certifications (e.g., PE license, PMP)")
        programming_languages = st.text_input("Programming Languages (if applicable, e.g., Python, Java)")

        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            st.success("Personal information stored successfully")
            meta_data.state = 2 
            st.rerun()
