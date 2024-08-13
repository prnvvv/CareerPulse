import streamlit as st

st.title("ChatBot 🤖")
st.text("Sorry, We are working on the Chat Bot currently 😔")
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
