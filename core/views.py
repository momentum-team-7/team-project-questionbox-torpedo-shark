from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from .models import User, Question, Answer, Profile
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer, QuestionDetailSerializer, QuestionResponseSerializer
from .serializers import AnswerWriteableSerializer, ProfileSerializer, ProfileDetailSerializer


# Create your views here.

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroy(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_destroy(self, serializer):
        instance = serializer.delete()

class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = [IsAuthenticated]


class ProfileUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()


class ProfileQuestions(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(Profile, pk=user_id)
        return Question.objects.filter(author=user.id)


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

    # def get_serializer(self, *args, **kwargs):
    #     # leave this intact
    #     serializer_class = self.get_serializer_class()
    #     kwargs["context"] = self.get_serializer_context()
    #     return serializer_class(*args, **kwargs)

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


class AnswerWrite(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerWriteableSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get_queryset(self):
    #     question_id = self.kwargs.get('question_id')
    #     question = get_object_or_404(Question, pk=question_id)
    #     return Answer.objects.filter(question=question)

    # def perform_create(self, serializer):
    #     question = get_object_or_404(Question, pk=self.kwargs['question_id'])
    #     serializer.save(question=question)
        # serializer.save(author=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(question=self.kwargs.get('question_id'))


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        
    def perform_destroy(self, serializer):
        instance = serializer.delete()