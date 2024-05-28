curl -X POST http://localhost:37894/courses \
     -H "Content-Type: application/json" \
     -d '{"title": "Deep Learning", "description": "A course about deep learning."}'

# Flashcard 1
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 1, "question": "What is deep learning?", "answer": "Deep learning is a subset of machine learning in artificial intelligence (AI) that has networks capable of learning unsupervised from data that is unstructured or unlabeled."}'

# Flashcard 2
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 1, "question": "Why is deep learning important?", "answer": "Because it is the technology behind many of the advances in AI, including computer vision, natural language processing, and autonomous vehicles."}'

# Flashcard 3
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 1, "question": "What are the key components of deep learning?", "answer": "Neural networks, big data, and algorithms for training the networks."}'

curl -X POST http://localhost:37894/courses \
     -H "Content-Type: application/json" \
     -d '{"title": "Anatomy", "description": "A course about human anatomy."}'

# Flashcard 1
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 2, "question": "What is the largest organ of the human body?", "answer": "The skin."}'

# Flashcard 2
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 2, "question": "Which bone is the longest bone in the human body?", "answer": "The femur."}'

# Flashcard 3
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 2, "question": "What is the main function of the red blood cells?", "answer": "To transport oxygen."}'

# Flashcard 4
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 2, "question": "How many chambers does the human heart have?", "answer": "Four."}'

# Flashcard 5
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 2, "question": "What type of joint is found in the shoulder?", "answer": "Ball and socket joint."}'

curl -X POST http://localhost:37894/courses \
     -H "Content-Type: application/json" \
     -d '{"title": "Electrical Engineering", "description": "A course about electrical engineering fundamentals."}'

# Flashcard 1
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 3, "question": "What is Ohms Law?", "answer": "The current through a conductor between two points is directly proportional to the voltage across the two points."}'

# Flashcard 2
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 3, "question": "What are the three passive electrical elements?", "answer": "Resistor, capacitor, inductor."}'

# Flashcard 3
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 3, "question": "What does AC stand for in electricity?", "answer": "Alternating current."}'

# Flashcard 4
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 3, "question": "What is the function of a transformer?", "answer": "To increase or decrease the voltage of an alternating current."}'

# Flashcard 5
curl -X POST http://localhost:37894/flashcards \
     -H "Content-Type: application/json" \
     -d '{"course_id": 3, "question": "What is a semiconductor?", "answer": "A material that has a conductivity between conductors and insulators."}'
