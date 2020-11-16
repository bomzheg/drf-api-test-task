from datetime import datetime

from pools.models import Poll, Question, Answer


def get_active_pools():
    now = datetime.utcnow().date()
    # noinspection PyUnresolvedReferences
    return Poll.objects.filter(date_start__lte=now, date_finish__gte=now)


def get_active_question():
    # noinspection PyUnresolvedReferences
    return Question.objects.filter(from_pool__in=get_active_pools())


def get_answers_for_active_question():
    # noinspection PyUnresolvedReferences
    return Answer.objects.filter(for_question__in=get_active_question())
