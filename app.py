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
project_2_page = st.Page(
page="pages/career_quiz_final.py",
title="career_quiz",
icon=":material/bar_chart:",
)
project_3_page = st.Page(
page="pages/psychometric_test.py",
title="psychometric_test",
icon=":material/bar_chart:",
)
chatbot_page = st.Page(
page="pages/chatbot.py",
title="chatbot",
icon=":material/bar_chart:",
)
Interest_page = st.Page(
page="pages/Interest.py",
title="Interest",
icon=":material/bar_chart:",
)

st.logo("logo.png")

pg = st.navigation(pages=[land_page,about_page,project_1_page,project_2_page,project_3_page,chatbot_page,Interest_page])

pg.run()