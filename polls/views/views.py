from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from polls.models import Poll, Question
from polls.serialializers import (
    PollSerializer,
    QuestionSerializer,
    PossibleAnswerSerializer
)
from polls.services.polls import (
    get_active_polls,
    get_active_question,
    get_possible_answers_for_active_question,
    get_question_of_poll,
)
from polls.views.common import ParentIDMixin


class PollsView(viewsets.ModelViewSet):
    queryset = get_active_polls()
    serializer_class = PollSerializer
    pagination_class = LimitOffsetPagination


class QuestionsView(viewsets.ModelViewSet):
    queryset = get_active_question()
    serializer_class = QuestionSerializer
    pagination_class = LimitOffsetPagination


class PossibleAnswersView(viewsets.ModelViewSet):
    queryset = get_possible_answers_for_active_question()
    serializer_class = PossibleAnswerSerializer
    pagination_class = LimitOffsetPagination


class PollQuestionsView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self, *args, **kwargs):
        pool_id = self.kwargs.get("pool_id")
        queryset = Question.objects.filter(from_poll_id=pool_id)
        return queryset


class QuestionerView:
    pass
