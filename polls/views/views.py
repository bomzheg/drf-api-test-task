from loguru import logger
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from polls.models import Poll, Question, PossibleAnswer
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


class PollQuestionsView(ParentIDMixin, viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    model = Question

    def get_filter_key(self):
        return {"from_poll_id": self.kwargs.get("poll_id")}


class QuestionPossibleAnswersView(ParentIDMixin, viewsets.ModelViewSet):
    serializer_class = PossibleAnswerSerializer
    model = PossibleAnswer

    def get_filter_key(self):
        return {"for_question": self.kwargs.get("question_id")}


class QuestionerView:
    pass
