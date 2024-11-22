import json
import os
from typing import List, Dict, Union
import google.generativeai as genai
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from API.models import Document, History, Question, Module
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

prompt = """
Create 2 detailed multiple-choice questions (MCQs) from the above content. Ensure that every small detail is addressed, including minor facts, nuanced concepts, and specific terminology.

Instructions:
    - Cover all aspects of the content, leaving no detail unexplored.
    - For each question:
        Write the question clearly.
        Provide four answer options: one correct answer and three plausible distractors.
        Include an explanation for the correct answer, clarifying why it's correct and why the distractors are incorrect.
    - Question difficulty should be high, covering the following levels:
        Basic fact recall.
        Conceptual understanding.
        Application and critical thinking based on the content.
        Analysis and evaluation of the content.
    - options must be in the form of 1, 2, 3, 4. 

Return the result as a JSON object structured as follows:
[{
    "question": "QUESTION_TEXT",
    "options": ["OPTION_1", "OPTION_2", "OPTION_3", "OPTION_4"],
    "answer": "CORRECT_OPTION_INDEX",
    "explanation": "EXPLANATION"
}, ...
]
"""

def generate_questions(content: str, document: Document) -> List[Dict[str, Union[str, List[str], int]]]:
    """
    Generate a set of multiple-choice questions from the given content.

    Args:
    content (str): The content from which to generate questions.

    Returns:
    List[Dict[str, Union[str, List[str], int]]]: A list of dictionaries, each containing a question, options, answer, and explanation.
    """

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash-8b')

    history = ""

    if History.objects.filter(document=document).exists():
        history_instance = History.objects.get(document=document)
        history = history_instance.history

    prompt_with_data = f"""
    --------------------------------------------
    {content}
    --------------------------------------------
    Previously generated questions:
    {history}
    --------------------------------------------
    {prompt}
    --------------------------------------------
    """

    print("prompt token count: ", model.count_tokens(prompt))
    print("history: ", history)

    print("prompt token count: ", model.count_tokens(prompt_with_data))

    result = model.generate_content(prompt_with_data)

    response = result.text
    response = response.replace('```json\n', "")
    response = response.replace('```', "")
    response = response.replace('\n', "")

    json_response = eval(response)

    if history == "":
        history = json.dumps(json_response, indent=None).replace('\n', "")[1:-1]
    else:
        history += json.dumps(json_response, indent=None).replace('\n', "")[1:-1]

    if History.objects.filter(document=document).exists():
        history_instance = History.objects.get(document=document)
        history_instance.history = json.dumps(history)
        history_instance.save()
    else:
        history_instance = History(
            document=document,
            history=history
        )
        history_instance.save()


    return json_response

class GenerateQuestionsView(APIView):
    def get(self, request: Request) -> Response:
        module_id = int(request.data.get('module', -1))
        document_id = int(request.data.get('module', -1))

        if module_id == -1:
            document = Document.objects.all().order_by('?').first()
        else:
            if document_id == -1:
                document = Document.objects.filter(module=module_id).order_by('?').first()
            else:
                document = Document.objects.get(id=document_id)

        content = document.file.read()

        questions = generate_questions(content, document)

        for question in questions:
            question_instance = Question(
                question_text=question['question'],
                options=question['options'],
                correct_option=question['answer'],
                module=document.module,
                document=document,
                explanation=question['explanation']
            )
            question_instance.save()

        return Response({"questions": questions})
