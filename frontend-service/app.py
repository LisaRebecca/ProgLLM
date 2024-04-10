import streamlit as st
import requests

def fetch_courses():
    try:
        response = requests.get("http://172.22.0.1:37894/courses")
        if response.status_code == 200:
            return response.json()  # A list of courses with ids, titles, and descriptions
        else:
            st.error("Failed to fetch courses.")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return []

# Function to fetch course names from the backend
def fetch_course_names():
    try:
        response = requests.get("http://172.22.0.1:37894/courses")
        # Ensure the response status is ok (200)
        if response.status_code == 200:
            courses = response.json()
            # Extract course titles from the response
            course_titles = [course["title"] for course in courses]
            return course_titles
        else:
            st.error("Failed to fetch courses. Please check the backend service.")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return []

def get_course_id_by_title(title):
    courses = fetch_courses()  # Assuming this function returns the full list with IDs and titles
    for course in courses:
        if course["title"] == title:
            return course["courseid"]
    return None


def fetch_flashcards(course_id):
    try:
        response = requests.get(f"http://172.22.0.1:37894/courses/{course_id}/flashcards")
        if response.status_code == 200:
            return response.json()  # Assuming the endpoint returns a list of flashcards
        else:
            st.error("Failed to fetch flashcards.")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return []

# Fetch full course details
courses_details = fetch_courses()

# Generate a list of course titles for the selectbox
course_titles = [course["title"] for course in courses_details]
selected_course_title = st.sidebar.selectbox("Select a Course:", course_titles)

# Get the ID of the selected course
selected_course_id = get_course_id_by_title(selected_course_title)

# Fetch flashcards for the selected course
flashcards = fetch_flashcards(selected_course_id)

# Simple state management to cycle through flashcards
if 'current_flashcard_index' not in st.session_state:
    st.session_state.current_flashcard_index = 0

if flashcards:
    current_flashcard = flashcards[st.session_state.current_flashcard_index]
    question = current_flashcard["question"]
    answer = current_flashcard["answer"]  # This might be used later for validation
    
    st.write(f"Question: {question}")
    user_answer = st.text_input("Your answer:", key="user_answer")
    
    if st.button("Submit"):
        # Here you could validate the user's answer, give feedback, and decide what to do next
        st.write(f"Your answer: {user_answer}")
        # This example simply moves to the next flashcard
        st.session_state.current_flashcard_index = (st.session_state.current_flashcard_index + 1) % len(flashcards)
else:
    st.write("No flashcards available for this course.")

