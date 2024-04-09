import openai
import os
import json

openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()

GPT_MODEL = "gpt-3.5-turbo"
GPT_FUNCTION_MODEL = "gpt-3.5-turbo-0125"


def get_summary_from_text(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system", 
                "content": "You are a helpful study assistant who summarizes the main ideas of an input."
                },
            {
                "role": "user", 
                "content": text,
                },
          ],
        model=GPT_MODEL,
        )
    summary = chat_completion.choices[0].message.content
    return summary



tool_extract_question = [
  {
    "type": "function",
    "function": {
      "name": "hand_over_questions",
      "description": "Give the comprehensive questions to the user.",
      "parameters": {
        "type": "object",
        "properties": {
          "question": {
            "type": "string",
            "description": "A question which can be answered using the given text paragraph.",
          },
          "answer": {
              "type": "string", 
              "description": "The answer to the question.",
          },
        },
        "required": ["question", "answer"],
      },
    }
  }
]

def get_question_from_text(text):
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "user", 
                "content": text,
            }
        ],
        tools=tool_extract_question,
        model=GPT_FUNCTION_MODEL,
    )

    function_arguments = chat_completion.choices[0].message.tool_calls[0].function.arguments
    function_arguments = json.loads(function_arguments)

    question = function_arguments['question']
    answer = function_arguments['answer']

    return question, answer