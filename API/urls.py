from django.urls import path

from .views import DocumentView, ModuleView, QuestionView, GenerateQuestionsView

urlpatterns = [
    path('documents/', DocumentView.as_view()),
    path('modules/', ModuleView.as_view()),
    path('question/', QuestionView.as_view()),

    path('generate/', GenerateQuestionsView.as_view()),
]