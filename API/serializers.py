from .models import Document, Module, Question, Identifier
from rest_framework.serializers import ModelSerializer

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class IdentifierSerializer(ModelSerializer):
    class Meta:
        model = Identifier
        fields = '__all__'