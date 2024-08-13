import streamlit as st
import meta_data

def Q24_page():
    with st.form("Q24_page"):
        col1, col2 = st.columns(2)
        with col1:
            yesbut = st.form_submit_button("Yes")
                
        with col2:
            nobut = st.form_submit_button("No")


        if yesbut:
                meta_data.Qstate = 25
                meta_data.QID24 = True
                st.rerun()

        if nobut:
                meta_data.Qstate = 25
                meta_data.QID24 = False
                st.rerun()