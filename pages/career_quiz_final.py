import streamlit as st
from questions.career_quiz import Career_quiz
import meta_data

meta_data.gpa=st.text_input("Enter the cgpa")
if meta_data.Qstate  ==  0:
    @st.dialog("CGPA")
    def ():
        personal_details()
    personal_info()