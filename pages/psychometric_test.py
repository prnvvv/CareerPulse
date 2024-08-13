import streamlit as st
import pandas as pd

def main():
    st.title("Psychometric Test")

    questions = [
        'In uncertain times, I usually expect the best.',
        'I`m always optimistic about my future.',
        'I generally expect things to go my way.',
        'Overall, I expect more good things to happen to me than bad.',
        'I feel that I am a person of worth, at least on an equal plane with others.',
        'I take a positive attitude toward myself.',
        'I am able to do things as well as most other people.',
        'I feel I have a number of good qualities.',
        'I tend to look on the bright side of things.',
        'I am generally satisfied with myself.',
        'I am confident in my ability to achieve my goals.',
        'I can handle most situations that come my way.',
        'I bounce back quickly after experiencing difficulties.',
        'I can handle stress effectively.',
        'I am aware of my emotions and how they affect my behavior.',
        'I can empathize with others` feelings.',
        'I remain calm under pressure.',
        'I handle stressful situations effectively.',
        'I am highly motivated to achieve my goals.',
        'I persist in the face of challenges.',
        'I communicate effectively with others.',
        'I am good at building and maintaining relationships.',
        'I am satisfied with my life as a whole.',
        'I feel fulfilled in my daily activities.'
    ]

    options = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
    
    # Create a DataFrame to store responses
    if 'responses' not in st.session_state:
        st.session_state.responses = pd.DataFrame(columns=['Question', 'Answer'])

    for i, question in enumerate(questions, 1):
        st.write(f"**Q{i}. {question}**")
        answer = st.radio(f"Select your answer for Q{i}:", options, key=f"q{i}")
        
        # Store the response
        st.session_state.responses = st.session_state.responses._append({
            'Question': question,
            'Answer': answer
        }, ignore_index=True)
        
        st.write("---")

    if st.button("Submit"):
        st.write("Thank you for completing the psychometric test!")
        st.write("Your responses:")
        st.dataframe(st.session_state.responses)

main()