from rest_framework import viewsets

from .models import Poll, Question, Answer
from .serialializers import PoolSerializer, QuestionSerializer, AnswerSerializer


class PoolsView(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PoolSerializer


class QuestionsView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswersView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
