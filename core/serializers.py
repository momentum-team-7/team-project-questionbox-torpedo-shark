from rest_framework import serializers, fields
from rest_framework.exceptions import ValidationError
from .models import User, Question, Answer, Profile

class CurrentUserDefault:

    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user


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
    author = UserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'body', 'question', 'author',)


class AnswerWriteableSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Answer
        fields = ('id', 'body', 'question', 'author',)


class QuestionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = ('id', 'title', 'body', 'author', 'tags', 'musicgenre',)
    

class QuestionDetailSerializer(serializers.HyperlinkedModelSerializer):
    replies = AnswerSerializer(read_only=True, many=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'body', 'author', 'tags', 'replies', 'musicgenre',)


class QuestionResponseSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('id', 'body', 'question',)


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'first_name', 'last_name', 'bio', 'location', 'join_year', 'img', 'question',)