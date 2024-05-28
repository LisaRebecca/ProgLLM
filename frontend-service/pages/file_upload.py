import streamlit as st
import requests
from langchain.text_splitter import CharacterTextSplitter
import concurrent

ready_to_study=False
course_created=False

def send_request(text_chunk):
    url = "http://localhost:34567/generate-questions"
    headers = {"Content-Type": "application/json"}
    data = {"text": text_chunk}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()  # Assuming the API returns JSON
    else:
        return "Error: API request failed."

def generate_questions(uploaded_file):
    documents = [uploaded_file.read().decode()]
    # Split documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=0, separator=".")
    documents = text_splitter.create_documents(documents)
    # Use ThreadPoolExecutor to send requests in parallel
    questions = []

    count_documents = len(documents)
    i=0
    progress_bar = st.progress(0, "Generating questions for you ...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Map send_request function to each text chunk
        future_to_text = {executor.submit(send_request, doc.page_content): doc.page_content for doc in documents}
        for future in concurrent.futures.as_completed(future_to_text):
            text_chunk = future_to_text[future]
            try:
                response_data = future.result()
                questions.append(future.result())
                #st.write(f"Questions for text chunk '{text_chunk[:50]}...': {response_data}")
                progress_bar.progress(i/count_documents,"Generating questions for you ...")
                i=i+1
            except Exception as exc:
                st.write(f"Generated exception for '{text_chunk[:50]}...': {exc}")
        progress_bar.empty()
    return questions

def add_questions_to_course(question, answer, course_id):
# Here you would typically make an API call to your backend to create the course
        # This is a placeholder for the API call
        url = "http://127.0.0.1:37894/flashcards"  # Update with your actual API endpoint
        payload = {
            "course_id": course_id,
            "question": question,
            "answer": answer
        }
        headers = {"Content-Type": "application/json"}
        
        # Making a POST request to the backend
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200 or response.status_code == 201:
            # Assuming your API returns the created course details or a success message
            created_card = response.json()
            
        else:
            st.error("Failed to create the card.")

# Page title
st.set_page_config(page_title='📚 Add a new Study Material')
st.title('📕 Add a new Course')

# Input fields for course name and description
course_name = st.text_input("Course Name", placeholder="Enter the course name here", disabled=course_created)
course_description = st.text_area("Course Description", placeholder="Enter the course description here", height=150, disabled=course_created)

create = st.button("Create", disabled=course_created)

if create:
    if not course_name or not course_description:
        st.error("Please fill in both the course name and description.")
    else:
        # Here you would typically make an API call to your backend to create the course
        # This is a placeholder for the API call
        url = "http://127.0.0.1:37894/courses"  # Update with your actual API endpoint
        payload = {
            "title": course_name,
            "description": course_description
        }
        headers = {"Content-Type": "application/json"}
        
        # Making a POST request to the backend
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200 or response.status_code == 201:
            # Assuming your API returns the created course details or a success message
            
            st.success("Course created successfully!")
            created_course = response.json()
            st.session_state.created_course_id = created_course["CourseID"]
            course_created=True
            
        else:
            st.error("Failed to create the course.")

st.divider()

st.title('📑 Add Content to Course')

# File upload
uploaded_file = st.file_uploader('Please upload a file', type='txt', disabled=not create)
# Query text

if st.button("Generate Study Set with AI 🪄", key="generate", type="primary", disabled=not uploaded_file):
    study_set = generate_questions(uploaded_file)
    st.success(f"Successfully generated {len(study_set)} questions for you.")
    progress_bar = st.progress(0, "Saving questions to your library ...")
    i = 0
    for qa in study_set:
        try:
            add_questions_to_course(qa["question"], qa["answer"], st.session_state.created_course_id)
            
        except Exception as e:
            print(e)
        progress_bar.progress(i/len(study_set), "Saving questions to your library ...")
        i=i+1
    st.success(f"Successfully added questions to your library.")
    progress_bar.empty()
    ready_to_study=True


if st.button("📖 Start interactive Session", key="start_session", disabled=not ready_to_study):
        st.session_state.selected_course_id = st.session_state.created_course_id
        st.switch_page("pages/study.py")
