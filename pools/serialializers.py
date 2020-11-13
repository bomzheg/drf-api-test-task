from typing import Any, Dict

from rest_framework import serializers
from .models import Poll, Question, Answer


class PoolSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=256)
    welcome_text = serializers.CharField(max_length=1024)
    final_text = serializers.CharField(max_length=1024)

    def create(self, validated_data: Dict[str, Any]):
        return Poll(**validated_data)

    def update(self, instance: Poll, validated_data: Dict[str, Any]):
        instance.name = validated_data.get('name', default="name")
        instance.welcome_text = validated_data.get('welcome_text', default="welcome_text")
        instance.final_text = validated_data.get('final_text', default="final_text")
        return instance


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question_text = serializers.CharField(max_length=1024)

    def create(self, validated_data: Dict[str, Any]):
        return Question(**validated_data)

    def update(self, instance: Question, validated_data: Dict[str, Any]):
        instance.question_text = validated_data.get('question_text', default="question_text")
        return instance


class AnswerSerializer(serializers.Serializer):
    answer_text = serializers.CharField(max_length=256)

    def create(self, validated_data: Dict[str, Any]):
        return Answer(**validated_data)

    def update(self, instance: Answer, validated_data: Dict[str, Any]):
        instance.answer_text = validated_data.get('answer_text', default="answer_text")
        return instance
