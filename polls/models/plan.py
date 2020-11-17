from datetime import datetime
from enum import Enum, auto

from django.db import models


class QuestionTypes(Enum):
    """
    Тип вопроса, который может быть задан пользователю, может быть:
    * one_choice - выбор одного варианта ответа
    * multiple_choice - выбор нескольких вариантов ответа
    * free_text - свободный ответ (ввод простого текста)
    """
    one_choice = auto()
    multiple_choice = auto()
    free_text = auto()

    @classmethod
    def choices(cls):
        return [(key.name, key.name) for key in cls]


class Poll(models.Model):
    """Модель данных опроса."""
    name = models.CharField(max_length=256, verbose_name="Название опроса")
    date_start = models.DateField(verbose_name="Дата начала")
    date_finish = models.DateField(verbose_name="Дата завершения")
    description = models.CharField(max_length=1024, verbose_name="Описание")
    welcome_text = models.CharField(
        max_length=1024, verbose_name="Приветственное сообщение в начале опроса", default="")
    final_text = models.CharField(max_length=1024, verbose_name="Сообщение о завершении опроса", default="")

    def __str__(self):
        return self.name

    @property
    def is_active(self):
        # noinspection PyTypeChecker
        return self.date_start <= datetime.utcnow().date() <= self.date_finish


class Question(models.Model):
    """Модель данных вопроса обязательно связана с конкретным опросом."""
    question_text = models.CharField(max_length=1024, verbose_name="Текст вопроса")
    question_type = models.CharField(
        choices=QuestionTypes.choices(),
        default=QuestionTypes.one_choice,
        verbose_name="Тип ответа на вопрос",
        max_length=64,
    )
    from_poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        verbose_name="К опросу",
        related_name='questions',
    )

    def __str__(self):
        return self.question_text


class PossibleAnswer(models.Model):
    """Вариант ответа для вопросов с вариантами ответов."""
    answer_text = models.CharField(max_length=256, verbose_name="Текст ответа")
    for_question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="К вопросу",
        related_name='possible_answers',
    )

    def __str__(self):
        return self.answer_text
