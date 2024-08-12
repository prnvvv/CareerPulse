import streamlit as st
import meta_data

def stu_YesNo():
    with st.form("stu_YesNo"):
        col1, col2 = st.columns(2)
        with col1:
            yesbut = st.form_submit_button("Yes")
                
        with col2:
            nobut = st.form_submit_button("No")



        if yesbut:
                meta_data.state = 4
                st.rerun()

        if nobut:
                meta_data.state = 3
                st.rerun()