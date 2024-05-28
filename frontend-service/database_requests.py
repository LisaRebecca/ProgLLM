import requests
import streamlit as st

def fetch_courses():
    try:
        response = requests.get("http://127.0.0.1:37894/courses")
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
        response = requests.get("http://127.0.0.1:37894/courses")
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
        response = requests.get(f"http://127.0.0.1:37894/courses/{course_id}/flashcards")
        if response.status_code == 200:
            return response.json()  # Assuming the endpoint returns a list of flashcards
        else:
            st.error("Failed to fetch flashcards.")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return []