from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from .models import User, Question, Answer, Profile
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer, QuestionDetailSerializer, QuestionResponseSerializer


# Create your views here.

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_class = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        
    def perform_destroy(self, serializer):
        instance = serializer.delete()


class QuestionResponse(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        question_id = self.kwargs.get('question_id')
        question = get_object_or_404(Question, pk=question_id)
        return Answer.objects.filter(question=question)


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        
    def perform_destroy(self, serializer):
        instance = serializer.delete()