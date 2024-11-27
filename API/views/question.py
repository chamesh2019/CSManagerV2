import json

from API.models import Question, Document, Module
from API.serializers import QuestionSerializer
from rest_framework.views import APIView

from rest_framework.request import Request
from rest_framework.response import Response

class QuestionView(APIView):
    def get(self, request: Request) -> Response:
        module = int(request.query_params.get('module', -1))
        document = int(request.query_params.get('document', -1))
        difficulty = request.query_params.get("difficulty", "Easy")


        questions = Question.objects.all()
        if module == -1:
            selected_question = questions.order_by('?').first()

        else:
            if document == -1:
                selected_question = questions.filter(module=Module.objects.get(id=module)).order_by('?').first()

            else:
                selected_question = questions.filter(
                    module=Module.objects.get(id=module),
                    document=Document.objects.get(id=Document)
                ).order_by('?').first()

        serializer = QuestionSerializer(selected_question)
        question = {
            "question": serializer.data["question_text"],
            "answer" : serializer.data['correct_option'],
            "options": eval(serializer.data['options']),
            "explanation": serializer.data['explanation']
        }
        return Response(question)
