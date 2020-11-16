from rest_framework import viewsets

from pools.serialializers import PoolSerializer, QuestionSerializer, AnswerSerializer
from pools.services.pools import get_active_pools, get_active_question, get_answers_for_active_question


class PoolsView(viewsets.ModelViewSet):
    queryset = get_active_pools()
    serializer_class = PoolSerializer


class QuestionsView(viewsets.ModelViewSet):
    queryset = get_active_question()
    serializer_class = QuestionSerializer


class AnswersView(viewsets.ModelViewSet):
    queryset = get_answers_for_active_question()
    serializer_class = AnswerSerializer
