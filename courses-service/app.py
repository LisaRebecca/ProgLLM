from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database connection parameters
DB_HOST = "db"
DB_NAME = "flashcards_db"
DB_USER = "user"
DB_PASS = "password"

def get_db_connection():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    return conn

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    title = data['title']
    description = data.get('description', '')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Courses (Title, Description) VALUES (%s, %s) RETURNING CourseID;",
                (title, description))
    course_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Course created successfully', 'CourseID': course_id}), 201

@app.route('/courses', methods=['GET'])
def get_courses():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM Courses;")
    courses = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(courses), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM Courses WHERE CourseID = %s;", (course_id,))
    course = cur.fetchone()
    cur.close()
    conn.close()

    if course is not None:
        return jsonify(course), 200
    else:
        return jsonify({'message': 'Course not found'}), 404
    
@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # First, check if the course exists in the database
    cur.execute("SELECT * FROM Courses WHERE CourseID = %s;", (course_id,))
    course = cur.fetchone()
    if course is None:
        cur.close()
        conn.close()
        return jsonify(404, description="Course not found")  # Return 404 if the course does not exist

    # If the course exists, proceed to delete it
    cur.execute("DELETE FROM Flashcards WHERE CourseID = %s;", (course_id,))
    cur.execute("DELETE FROM Courses WHERE CourseID = %s;", (course_id,))
    conn.commit()
    
    cur.close()
    conn.close()

    return jsonify({"message": f"Course id={course_id}deleted successfully"}), 200
    
@app.route('/courses/<int:course_id>/flashcards', methods=['GET'])
def get_flashcards_for_course(course_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM Flashcards WHERE CourseID = %s;", (course_id,))
    flashcards = cur.fetchall()
    cur.close()
    conn.close()

    if flashcards:
        return jsonify(flashcards), 200
    else:
        return jsonify({'message': 'No flashcards found for the specified course or course not found'}), 404


@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    course_id = data['course_id']
    question = data['question']
    answer = data['answer']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Flashcards (CourseID, Question, Answer) VALUES (%s, %s, %s) RETURNING FlashcardID;",
                (course_id, question, answer))
    flashcard_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Flashcard created successfully', 'FlashcardID': flashcard_id}), 201

# Add more routes as needed for CRUD operations on flashcards and user progress

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=37894)
