import streamlit as st

land_page = st.Page(
page="pages/landpage.py",
title="Landpage",
icon=":material/account_circle:",
default=True,
)
about_page = st.Page(
page="pages/personal_info.py",
title="About Me",
icon=":material/account_circle:",
)

project_1_page = st.Page(
page="pages/dashboard.py",
title="Dashboard",
icon=":material/bar_chart:",
)
st.logo("logo.png")

pg = st.navigation(pages=[land_page,about_page,project_1_page])

pg.run()