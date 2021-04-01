from rest_framework import serializers
from .models import User, Question, Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)

    
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'body',)


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True) 

    class Meta:
        model = Question
        fields = ('id', 'title', 'body', 'author', 'tag', 'answers',)

