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


st.button("🔍 Interest - How to follow your passion")
st.button("📝 Psychometric quiz")
st.button("🧠 Career Quiz")
st.button("📄 Job Application")
st.button("💬 Chat bot")



