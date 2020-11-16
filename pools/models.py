from datetime import datetime
from enum import Enum, auto

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


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
        return self.date_start < datetime.utcnow().date() < self.date_finish


class Question(models.Model):
    """Модель данных вопроса обязательно связана с конкретным опросом."""
    question_text = models.CharField(max_length=1024, verbose_name="Текст вопроса")
    question_type = models.CharField(
        choices=QuestionTypes.choices(),
        default=QuestionTypes.one_choice,
        verbose_name="Тип ответа на вопрос",
        max_length=64,
    )
    from_pool = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="К опросу")

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    """Вариант ответа для вопросов с вариантами ответов."""
    answer_text = models.CharField(max_length=256, verbose_name="Текст ответа")
    for_question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="К вопросу")

    def __str__(self):
        return self.answer_text


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
