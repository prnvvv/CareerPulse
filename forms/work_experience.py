import streamlit as st
import meta_data

def Work_experience():
    with st.form("Work_experience"):
        meta_data.cur_job=st.text_input("Current job title")
        meta_data.years_exp=st.text_input("Years of experience")
        submit_button=st.form_submit_button("Submit")
        if submit_button:
            st.success("Personal information stored successfully")
            meta_data.state = 4
            st.rerun()
