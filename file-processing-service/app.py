from mock_functions import get_summary_from_text, get_question_from_text

from flask import Flask, request, jsonify
import openai
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/summarize', methods=['POST'])
def summarize_file():
    """
    Endpoint to summarize file content.
    """
    data = request.json
    text = data.get('text')
    
    try:
        logging.info("SUMMARY REQUEST: "+text)
        summary = get_summary_from_text(text)
        return jsonify({"summary": summary}), 200
    except Exception as e:
        print(e)
        logging.error(f"Error generating summary: {str(e)}")
        return jsonify({"error": "Error generating summary"}), 500

@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    """
    Endpoint to generate questions based on file content.
    """
    data = request.json
    text = data.get('text')
    
    try:
        question, answer = get_question_from_text(text)
        return jsonify({"question": question, "answer": answer}), 200
    except Exception as e:
        logging.error(f"Error generating questions: {str(e)}")
        return jsonify({"error": "Error generating questions"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=34567)
