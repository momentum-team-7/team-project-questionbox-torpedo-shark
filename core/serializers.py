from rest_framework import serializers, fields
from .models import User, Profile, Question, Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'first_name', 'last_name', 'bio', 'location', 'join_year', 'img',)

    
class AnswerSerializer(serializers.ModelSerializer):
    question_body = serializers.ReadOnlyField(source='question.body')

    class Meta:
        model = Answer
        fields = ('id', 'body', 'question_body',)


class QuestionSerializer(serializers.ModelSerializer):
    replies = AnswerSerializer(read_only=True, many=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'body', 'author', 'tags', 'replies', 'musicgenre',)

class QuestionResponseSerializer(serializers.ModelSerializer):
    replies = AnswerSerializer(read_only=True, many=True)
    # author = ProfileSerializer(read_only=True)


    class Meta:
        model = Answer
        fields = ('id', 'body', 'replies',)