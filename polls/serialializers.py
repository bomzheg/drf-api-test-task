from django.contrib.auth.models import User
from rest_framework import serializers

from polls.models import Poll, Question, PossibleAnswer


class PollSerializer(serializers.ModelSerializer):
    questions = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="question-detail")

    class Meta:
        model = Poll
        fields = ("questions", "name", "date_start", "date_finish",
                  "description", "welcome_text", "final_text")


class QuestionSerializer(serializers.ModelSerializer):
    possible_answers = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="possibleanswer-detail")

    class Meta:
        model = Question
        fields = ("possible_answers", "question_text", "question_type", )
        depth = 1


class PossibleAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PossibleAnswer
        exclude = tuple()
        depth = 1


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'token')
