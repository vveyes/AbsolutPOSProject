from django.urls import path
from .views import QuestionView, ResultsView

urlpatterns = [
    path('', QuestionView.as_view(), name = 'polls'),
    path('results', ResultsView.as_view(), name = 'results')
]