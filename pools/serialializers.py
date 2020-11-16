from rest_framework import serializers
from pools.models import Poll, Question, Answer


class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        exclude = tuple()


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = tuple()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = tuple()
