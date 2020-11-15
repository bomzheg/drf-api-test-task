from rest_framework import serializers
from .models import Poll, Question, Answer


class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ("name", "welcome_text", "final_text")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = tuple()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = tuple()
