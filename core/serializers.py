from rest_framework import serializers, fields
from .models import User, Question, Answer

class CurrentUserDefault:

    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',)

    
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