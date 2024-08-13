import streamlit as st

st.title("🔍 Find your Interest ")
st.text("The data is taking more time than expected 😔")

custom_css = """
<style>
    .stButton {
        display: grid;
        place-items: center;
    }
    .stButton > button {
        width: 100px;
        height: 50px;
        font-size: 20px;
    }
    .stButton > button:hover {
        background-color: white;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
Button = st.button("Home")


if Button:
    st.switch_page("pages/dashboard.py")
