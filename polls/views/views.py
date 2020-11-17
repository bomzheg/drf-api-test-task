from rest_framework import viewsets

from polls.models import Poll
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


class QuestionsView(viewsets.ModelViewSet):
    queryset = get_active_question()
    serializer_class = QuestionSerializer


class PossibleAnswersView(viewsets.ModelViewSet):
    queryset = get_possible_answers_for_active_question()
    serializer_class = PossibleAnswerSerializer


class PollQuestionsView(viewsets.ModelViewSet, ParentIDMixin):
    serializer_class = QuestionSerializer
    model = Poll
    parent_field = "poll_id"
