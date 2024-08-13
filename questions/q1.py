import streamlit as st
import meta_data

def Q1_page():
    with st.form("Q1_page"):
        meta_data.key_proj=st.text_area("Enter CGPA: ")
        submit_button=st.form_submit_button("Submit")
        if submit_button:
            st.success("Personal information stored successfully")
            meta_data.state = 1
            st.rerun()