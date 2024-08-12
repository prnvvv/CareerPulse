import streamlit as st

from forms.userinfo_form import personal_details
from forms.education_details import Education_Details
from forms.work_experience import Work_experience
from forms.project_exp import project_exp
from forms.stu_yes_no import stu_YesNo
import meta_data


st.session_state.state_stu = 5


if meta_data.state  ==  0:
    @st.dialog("User details")
    def personal_info():
        personal_details()
    personal_info()

if meta_data.state  ==  1:
    @st.dialog("Education and Technical Skills")
    def Education_info():
        Education_Details()
        st.session_state.state_stu = 0
    Education_info()



if meta_data.state  ==  2:
    @st.dialog("Are you a student:")
    def check_stu():
        stu_YesNo()
    check_stu()
    

if meta_data.state  ==  3:
    @st.dialog("Work experience")
    def work_info():
        Work_experience()
    work_info()

if meta_data.state  ==  4:
    @st.dialog("Project experience")
    def project_info():
        project_exp()
    project_info()

if meta_data.state  ==  5:
    st.switch_page("pages/dashboard.py")