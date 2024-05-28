from database_requests import fetch_course_names, fetch_courses, fetch_flashcards, get_course_id_by_title
from check_answer import grade_answer

import streamlit as st
import random
import time
import requests

# Assuming fetch_flashcards and get_course_id_by_title are defined as previously discussed
courses_details = fetch_courses()
course_titles = [course["title"] for course in courses_details]
#selected_course_title = st.sidebar.selectbox("Select a Course:", course_titles)
#selected_course_id = get_course_id_by_title(selected_course_title)

flashcards = fetch_flashcards(st.session_state.selected_course_id)

# Streamed response emulator for flashcard questions
def response_generator(question):
    for word in question.split():
        yield word + " "
        time.sleep(0.05)

st.title("💬 AI Study Session")

# Initialize chat history and current flashcard index
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "current_flashcard_index" not in st.session_state:
    st.session_state.current_flashcard_index = 0

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user", avatar="🙋🏻").write(message["content"])
    if message["role"] == "tutor":
        st.chat_message("user", avatar="👩🏼‍🏫").write(message["content"])
    if message["role"] == "question":
        st.chat_message("user", avatar="❓").write(message["content"])

# Get the current flashcard
print("index="+str(st.session_state.current_flashcard_index))
current_flashcard = flashcards[st.session_state.current_flashcard_index]
question = current_flashcard["question"]

# Streamed question from the assistant
with st.chat_message("question", avatar="❓"):
    st.text(question)

# Accept user input
user_answer = st.chat_input("Your answer:")
if user_answer:
    st.session_state.messages.append({"role": "question", "content": question})
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_answer})

    result = grade_answer(question=question, reference_answer=current_flashcard["answer"], user_answer=user_answer)

    try:
        grade, feedback = result
        st.session_state.messages.append({"role": "tutor", "content": grade+"\n\n"+feedback+"\n\nReference answer: "+current_flashcard["answer"]})
    except Exception:
        grade = result
        st.session_state.messages.append({"role": "tutor", "content": grade})
    
    # Move to the next flashcard
    st.session_state.current_flashcard_index = (st.session_state.current_flashcard_index + 1) % len(flashcards)

    # Clear the input
    st.experimental_rerun()
