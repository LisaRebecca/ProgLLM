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
