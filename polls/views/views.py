from rest_framework import viewsets

from polls.models import Poll
from polls.serialializers import (
    PollSerializer,
    QuestionSerializer,
    AnswerSerializer
)
from polls.services.polls import (
    get_active_polls,
    get_active_question,
    get_answers_for_active_question,
    get_question_of_poll,
)
from polls.views.common import ParentIDMixin


class PollsView(viewsets.ModelViewSet):
    queryset = get_active_polls()
    serializer_class = PollSerializer


class QuestionsView(viewsets.ModelViewSet):
    queryset = get_active_question()
    serializer_class = QuestionSerializer


class AnswersView(viewsets.ModelViewSet):
    queryset = get_answers_for_active_question()
    serializer_class = AnswerSerializer


class PollQuestionsView(viewsets.ModelViewSet, ParentIDMixin):
    serializer_class = QuestionSerializer
    model = Poll
    parent_field = "poll_id"
