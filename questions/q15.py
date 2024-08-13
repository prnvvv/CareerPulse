import streamlit as st
import meta_data

def Q15_page():
    with st.form("Q15_page"):
        col1, col2 = st.columns(2)
        with col1:
            yesbut = st.form_submit_button("Yes")
                
        with col2:
            nobut = st.form_submit_button("No")


        if yesbut:
                meta_data.Qstate = 16
                meta_data.QID15 = True
                st.rerun()

        if nobut:
                meta_data.Qstate = 16
                meta_data.QID15 = False
                st.rerun()