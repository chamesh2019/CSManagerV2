from API.models import Question
from API.serializers import QuestionSerializer
from rest_framework.views import APIView

from rest_framework.request import Request
from rest_framework.response import Response

class QuestionView(APIView):
    def get(self, request: Request) -> Response:
        questions = Question.objects.all()
        selected_question = questions.order_by('?').first()
        serializer = QuestionSerializer(selected_question)
        return Response(serializer.data)
