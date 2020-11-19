from django.db import models

from .plan import Question, QuestionTypes


class Answer(models.Model):
    """Фактический ответ пользователя на вопрос из опроса."""
    for_question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="К вопросу",
        related_name='possible_answers',
    )
    respondent = models.IntegerField
    answer_type = models.CharField(
        choices=QuestionTypes.choices(),
        verbose_name="Тип ответа на вопрос",
        max_length=64,
    )
    answer_text = models.CharField(max_length=512, verbose_name="Текст ответа")
    datetime_answer = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "fact_answers"
        verbose_name = "Фактический ответ"
        verbose_name_plural = "Фактические ответы"

    def __str__(self):
        return f"{self.for_question} - респондент {self.respondent} ответил {self.answer_text}"
