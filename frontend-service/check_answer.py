import openai
import os
import json

openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()

GPT_MODEL = "gpt-3.5-turbo"
GPT_FUNCTION_MODEL = "gpt-3.5-turbo-0125"

tool_grade_answer = [
  {
    "type": "function",
    "function": {
      "name": "grade_answers",
      "description": "Grading student's answers.",
      "parameters": {
        "type": "object",
        "properties": {
          "feedback": {
            "type": "string",
            "description": "Feedback on the student's answer.",
          },
          "grade": {
                "type": "string",
                "description": "The ID of the state",
                "enum": ["Incorrect.","Neutral.","Correct."], 
          },
        },
        "required": ["grade"],
      },
    }
  }
]

def grade_answer(question, reference_answer, user_answer):
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "assistant", 
                "content": question,
            },
            {
                "role": "user", 
                "content": user_answer,
            },
            {
                "role": "assistant", 
                "content": "Reference answer: "+reference_answer,
            }
        ],
        tools=tool_grade_answer,
        model=GPT_FUNCTION_MODEL,
    )

    function_arguments = chat_completion.choices[0].message.tool_calls[0].function.arguments
    function_arguments = json.loads(function_arguments)

    grade = function_arguments['grade']
    try:
        feedback = function_arguments['feedback']
        return grade, feedback
    except Exception:
        return grade
    

if __name__=='__main__':
    #print(grade_answer(question="When was the moon landing?", reference_answer="1969", user_answer="1975"))
    print(grade_answer(question="Who wrote Hamlet?", reference_answer="William Shakespeare", user_answer="Shakespeare"))