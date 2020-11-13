from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название опроса")
    welcome_text = models.CharField(max_length=1024, verbose_name="Приветственное сообщение в начале опроса")
    final_text = models.CharField(max_length=1024, verbose_name="Сообщение о завершении опроса")

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=1024, verbose_name="Текст вопроса")
    from_pool = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="К опросу")

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    answer_text = models.CharField(max_length=256, verbose_name="Текст ответа")
    for_question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="К вопросу")

    def __str__(self):
        return self.answer_text
