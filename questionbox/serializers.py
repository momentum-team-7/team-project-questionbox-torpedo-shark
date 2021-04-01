from rest_framework import serializers, fields
from .models import User, Question, Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)

    
class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'body', 'question',)


class QuestionSerializer(serializers.ModelSerializer):
    replies = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'body', 'author', 'tags', 'replies',)

    # def create(self, validated_data):
    #     questions_data = validated_data.pop('questionsanswer')
    #     question = Question.objects.create(**validated_data)
    #     for question_data in questions_data:
    #         Question.objects.create(author=question, **question_data)
    #     return question