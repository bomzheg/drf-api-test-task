from datetime import datetime

from polls.models import Poll, Question, Answer


def get_active_polls():
    now = datetime.utcnow().date()
    # noinspection PyUnresolvedReferences
    return Poll.objects.filter(date_start__lte=now, date_finish__gte=now)


def get_active_question():
    # noinspection PyUnresolvedReferences
    return Question.objects.filter(from_poll__in=get_active_polls())


def get_answers_for_active_question():
    # noinspection PyUnresolvedReferences
    return Answer.objects.filter(for_question__in=get_active_question())


def get_question_of_poll(poll_id: int):
    # noinspection PyUnresolvedReferences
    return Question.objects.filter(from_poll__id=poll_id)
