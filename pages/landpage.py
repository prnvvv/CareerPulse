import streamlit as st

st.markdown("<h1 style='text-align: center; color: white;'>Welcome to CareerPulse</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white; font-family:roboto; '>Empowering Your Journey.</h2>", unsafe_allow_html=True)

st.image("getstarted.jpg")

st.markdown(
    """
    <style>
    .stButton > button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a button
if st.button("Get Started!"):
    st.write("Button clicked!")
    st.switch_page("pages/personal_info.py")