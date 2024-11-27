from django.http import HttpResponse
from rest_framework.request import Request

from API.models import Document, Module
from API.serializers import DocumentSerializer

from rest_framework.views import APIView, Response

form = """
<html>
<head>
<title>Upload Document</title>
</head>
<body>
<form method="POST" action="/api/documents/"  enctype="multipart/form-data">
<input type="hidden" name="module" value="1">
<input type="file" name="file">
<input type="submit">
</form>
</body>
</html>
"""

class DocumentView(APIView):
    def get(self, request: Request) -> Response:
        print(request.GET)
        if 'add' in request.GET.keys():
            return HttpResponse(form)

        module = request.query_params.get('module', -1)
        documents = Document.objects.filter(module=int(module))
        serialized_documents = DocumentSerializer(documents, many=True)

        return Response({"documents": serialized_documents.data})

    def post(self, request: Request) -> Response:
        module_id = int(request.data.get('module', -1))
        file = request.data.get('file')

        document = DocumentSerializer(data={
            "name": file.name,
            "module": module_id,
            "file": file
        })

        if document.is_valid():
            document.save()
            return Response({"message": "Document created successfully"})
        else:
            return Response({"bruh": "llll"}, status=400)