'''import streamlit as st
import meta_data
def Career_quiz():
    with st.form("Career Quiz"):
        degree = st.text_input("Highest Degree Obtained (e.g., B.Tech, M.S.)")
        cgpa = st.text_input("CGPA: The individual's CGPA (Cumulative Grade Point Average).")
        def webDev_YesNo():
            with st.form("webDev_YesNo"):
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


        def dataAnal_YesNo():
            with st.form("dataAnal_YesNo"):
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

    def techPerson_YesNo():
        with st.form("techPerson_YesNo"):
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

    def techPerson_YesNo():
        with st.form("techPerson_YesNo"):
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
                st.rerun()'''

