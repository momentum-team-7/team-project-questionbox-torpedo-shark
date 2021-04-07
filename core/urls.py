from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('user/<int:pk>/destroy', views.UserDestroy.as_view()),
    path('profile-page/<int:pk>/', views.ProfileDetail.as_view()),
    path('profile-page/<int:pk>/update/', views.ProfileUpdate.as_view()),
    path('profile-page/<int:user_id>/questions/', views.ProfileQuestions.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('questions/<int:question_id>/answers/', views.QuestionResponse.as_view()),
    path('answers/<int:pk>/', views.AnswerDetail.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('answers/add/', views.AnswerWrite.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)