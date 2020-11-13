from rest_framework import serializers
from .models import Poll, Question

class PoolSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=256)
    welcome_text = serializers.CharField(max_length=1024)
    final_text = serializers.CharField(max_length=1024)

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question_text = serializers.CharField(max_length=1024)

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

