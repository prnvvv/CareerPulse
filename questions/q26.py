import streamlit as st
import meta_data

def Q26_page():
    with st.form("Q26_page"):
        col1, col2 = st.columns(2)
        with col1:
            yesbut = st.form_submit_button("Yes")
                
        with col2:
            nobut = st.form_submit_button("No")


        if yesbut:
                meta_data.Qstate = 27
                meta_data.QID26 = True
                st.rerun()

        if nobut:
                meta_data.Qstate = 27
                meta_data.QID26 = False
                st.rerun()