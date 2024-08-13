import streamlit as st

import meta_data

# Inject the CSS into the Streamlit app
st.title("Hello "+meta_data.name+" ! 👋")



custom_css = """
<style>
    .stButton {
        display: grid;
        place-items: center;
    }
    .stButton > button {
        width: 400px;
        height: 50px;
        font-size: 20px;
    }
    .stButton > button:hover {
        background-color: white;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.markdown(custom_css, unsafe_allow_html=True)


Interest_button = st.button("🔍 Find your Interest ")
st.button("📝 Psychometric quiz")
st.button("🧠 Career Quiz")
st.button("📄 Job Application")
chat_button = st.button("💬 Chat bot")

if chat_button:
    st.switch_page("pages/chatbot.py")

if Interest_button:
    st.switch_page("pages/Interest.py")



