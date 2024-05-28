from database_requests import fetch_courses
from streamlit_card import card

import streamlit as st

st.set_page_config(page_title='👩🏼‍🏫 Home - AI Tutor')

def example(id):
    card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
        key=str(id),
        styles={
        "card": {
            "width": "200px",
            "height": "200px",
            "border-radius": "10px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            }
        }
)

st.title('Welcome to the FAU AI Tutor! 👩🏼‍🏫🧠')
st.divider()

with st.container(border=True):
    if st.button("Add a new Course", key="add_contents", type="primary"):
        st.switch_page("pages/file_upload.py")    

courses_details = fetch_courses()

for course in courses_details:
    with st.container(border=True):
        st.title(course["title"])
        st.write(course["description"])
        if st.button("Start interactive Session →", key=str(course)):
            st.session_state.selected_course_id = course["courseid"]
            st.switch_page("pages/study.py")

