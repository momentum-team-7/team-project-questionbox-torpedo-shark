from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('questions/<int:question_id>/answers/', views.QuestionResponse.as_view()),
    path('answers/<int:pk>/', views.AnswerDetail.as_view()),
    path('answers/', views.AnswerList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)