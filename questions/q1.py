import streamlit as st
import meta_data

def Q1_page():
    with st.form("Q1_page"):
        meta_data.QID1 = st.text_area("Enter CGPA: ")
        submit_button=st.form_submit_button("Submit")
        if submit_button:
            st.success("Personal information stored successfully")
            meta_data.Qstate = 2
            st.rerun()