from rest_framework.request import Request

from API.models import Module
from API.serializers import ModuleSerializer
from rest_framework.views import APIView

from rest_framework.response import Response

class ModuleView(APIView):
    def get(self, request: Request) -> Response:
        modules = Module.objects.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response({"modules" : serializer.data})

    def post(self, request):
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)