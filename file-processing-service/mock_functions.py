import time

def get_summary_from_text(text):
    summary = f"""I am a mocked summary so that you are not billed during programming.
    This was your original input: 
    {text}"""
    time.sleep(0.5)
    return summary

def get_question_from_text(text):
    question = f"""I am a mocked question so that you are not billed during programming.
    This was your original input: 
    {text}"""
    answer = "Mock answer"
    time.sleep(0.5)
    return question, answer