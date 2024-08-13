import streamlit as st
import meta_data

def Q14_page():
    with st.form("Q14_page"):
        col1, col2 = st.columns(2)
        with col1:
            yesbut = st.form_submit_button("Yes")
                
        with col2:
            nobut = st.form_submit_button("No")


        if yesbut:
                meta_data.Qstate = 15
                meta_data.QID14 = True
                st.rerun()

        if nobut:
                meta_data.Qstate = 15
                meta_data.QID14 = False
                st.rerun()