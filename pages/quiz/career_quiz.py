import streamlit as st
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
                        meta_data.QID0 = True
                        st.rerun()

                if nobut:
                        meta_data.QID0 = False
                        st.rerun()


        def dataAnal_YesNo():
            with st.form("dataAnal_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                    
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID1 = False
                    st.rerun()

                if nobut:
                    meta_data.QID1 = True
                    st.rerun()

        def readandwrite_YesNo():
            with st.form("readandwrite_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                        
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                        meta_data.QID2 = False
                        st.rerun()

                if nobut:
                        meta_data.QID2 = True
                        st.rerun()

        def techPerson_YesNo():
            with st.form("techPerson_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID3 = 4
                    st.rerun()

                if nobut:
                    meta_data.QID3 = 3
                    st.rerun()

        def nonTech_YesNo():
            with st.form("nonTech_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID4 = False
                    st.rerun()

                if nobut:
                    meta_data.QID4 = True
                    st.rerun() 

        def coding_YesNo():
            with st.form("coding_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID5 = False
                    st.rerun()

                if nobut:
                    meta_data.QID5 = True
                    st.rerun()    

        def mobileApp_YesNo():
            with st.form("mobileApp_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID6 = False
                    st.rerun()

                if nobut:
                    meta_data.QID6 = True
                    st.rerun()   

        def comm_YesNo():
            with st.form("comm_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID7 = False
                    st.rerun()

                if nobut:
                    meta_data.QID7 = True
                    st.rerun()         

        def security_YesNo():
            with st.form("security_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                                
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID8 = False
                    st.rerun()

                if nobut:
                    meta_data.QID8 = True
                    st.rerun()

        def largeData_YesNo():
            with st.form("largeData_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID9 = False
                    st.rerun()

                if nobut:
                    meta_data.QID9 = True
                    st.rerun()

        def statsandDS_YesNo():
            with st.form("statsandDS_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID10 = False
                    st.rerun()

                if nobut:
                    meta_data.QID10 = True
                    st.rerun()

        def English_YesNo():
            with st.form("English_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID11 = False
                    st.rerun()

                if nobut:
                    meta_data.QID11 = True
                    st.rerun()

        def manage_YesNo():
        with st.form("manage_YesNo"):
            col1, col2 = st.columns(2)
            with col1:
                yesbut = st.form_submit_button("Yes")
                        
            with col2:
                nobut = st.form_submit_button("No")



            if yesbut:
                meta_data.QID12 = False
                st.rerun()

            if nobut:
                meta_data.QID12 = True
                st.rerun()

        def blog_YesNo():
        with st.form("blog_YesNo"):
            col1, col2 = st.columns(2)
            with col1:
                yesbut = st.form_submit_button("Yes")
                        
            with col2:
                nobut = st.form_submit_button("No")



            if yesbut:
                meta_data.QID13 = 4
                st.rerun()

            if nobut:
                meta_data.QID13 = 3
                st.rerun()

        def marketing_YesNo():
            with st.form("marketing_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID14 = False
                    st.rerun()

                if nobut:
                    meta_data.QID14 = True
                    st.rerun()

        def MLexpert_YesNo():
            with st.form("MLexpert_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID15 = False
                    st.rerun()

                if nobut:
                    meta_data.QID15 = True
                    st.rerun()

        def connections_YesNo():
            with st.form("connections_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID16 = False
                    st.rerun()

                if nobut:
                    meta_data.QID16 = True
                    st.rerun()
            
        def liveProj_YesNo():
            with st.form("liveProj_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID17 = False
                    st.rerun()

                if nobut:
                    meta_data.QID17 = True
                    st.rerun()

        def CAOsoft_YesNo():
            with st.form("CAOsoft_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID18 = False
                    st.rerun()

                if nobut:
                    meta_data.QID18 = True
                    st.rerun()
                        
        def roboticsProj_YesNo():
            with st.form("roboticsProj_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID19 = 4
                    st.rerun()

                if nobut:
                    meta_data.QID19 = 3
                    st.rerun()
            
        def constructionMat_YesNo():
            with st.form("constructionMat_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID20 = False
                    st.rerun()

                if nobut:
                    meta_data.QID20 = True
                    st.rerun()

        def involvementUrbanProj_YesNo():
            with st.form("involvementUrbanProj_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID21 = False
                    st.rerun()

                if nobut:
                    meta_data.QID21 = True
                    st.rerun()

        def biomechanics_YesNo():
            with st.form("biomechanics_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID22 = False
                    st.rerun()

                if nobut:
                    meta_data.QID22 = True
                    st.rerun()

        def healthcareTech_YesNo():
            with st.form("healthcareTech_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID23 = False
                    st.rerun()

                if nobut:
                    meta_data.QID23 = True
                    st.rerun()
            
        def aircraftDesign_YesNo():
            with st.form("aircraftDesign_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID24 = False
                    st.rerun()

                if nobut:
                    meta_data.QID24 = True
                    st.rerun()

        def flightSimulation_YesNo():
            with st.form("flightSimulation_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID25 = False
                    st.rerun()

                if nobut:
                    meta_data.QID25 = True
                    st.rerun()

        def controlSys_YesNo():
            with st.form("controlSys_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID26 = False
                    st.rerun()

                if nobut:
                    meta_data.QID26 = True
                    st.rerun()

        def PCBDesign_YesNo():
            with st.form("PCBDesign_YesNo"):
                col1, col2 = st.columns(2)
                with col1:
                    yesbut = st.form_submit_button("Yes")
                            
                with col2:
                    nobut = st.form_submit_button("No")



                if yesbut:
                    meta_data.QID27 = False
                    st.rerun()

                if nobut:
                    meta_data.QID27 = True
                    st.rerun()