import streamlit as st

from forms.education_details import Education_Details
import meta_data

def personal_details():
    with st.form("Personal_details"):
        meta_data.name=st.text_input("Name")
        meta_data.email=st.text_input("Email Address")
        meta_data.location=st.text_input("Location")
        submit_button=st.form_submit_button("Submit")

        if submit_button:
            st.success("Personal information stored successfully")
            meta_data.state =1
            st.rerun()
           # Education_Details()

