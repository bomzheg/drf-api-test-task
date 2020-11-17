from django.contrib.auth.models import User
from rest_framework import serializers

from polls.models import Poll, Question, PossibleAnswer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        exclude = tuple()
        read_only_fields = ['date_start']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = tuple()


class PossibleAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PossibleAnswer
        exclude = tuple()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'token')