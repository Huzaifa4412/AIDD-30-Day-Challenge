import streamlit as st
from modules.extractor import extract_text
from modules.summarizer import generate_summary
from modules.quiz_mcq import generate_mcq_quiz
from modules.quiz_mixed import generate_mixed_quiz

st.title("Study Notes Summarizer & Quiz Generator")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    
    # Extract text
    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_text(uploaded_file)
    
    if pdf_text:
        st.success("Text extracted successfully!")

        # Generate Summary
        st.header("Summary")
        if st.button("Generate Summary"):
            with st.spinner("Generating summary..."):
                summary = generate_summary(pdf_text)
            st.write(summary)

        # Generate Quiz
        st.header("Quiz Generator")
        quiz_mode = st.radio("Select Quiz Mode:", ("MCQ", "Mixed-Style"))

        if st.button("Generate Quiz"):
            if quiz_mode == "MCQ":
                with st.spinner("Generating MCQ Quiz..."):
                    quiz = generate_mcq_quiz(pdf_text)
                st.write(quiz)
            elif quiz_mode == "Mixed-Style":
                with st.spinner("Generating Mixed-Style Quiz..."):
                    quiz = generate_mixed_quiz(pdf_text)
                st.write(quiz)
    else:
        st.error("Could not extract text from the PDF.")