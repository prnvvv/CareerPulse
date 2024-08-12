import streamlit as st
import meta_data

def project_exp():
    with st.form("project_exp"):
        meta_data.key_proj=st.text_area("Key Projects Completed (brief description, role, outcomes)")
        meta_data.type_proj=st.text_area("Types of Projects (e.g., design, research, development)")
        submit_button=st.form_submit_button("Submit")
        if submit_button:
            st.success("Personal information stored successfully")
            meta_data.state = 5
            st.rerun()