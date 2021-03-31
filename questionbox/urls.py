from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from questionbox import views

urlpatterns = [
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('questions/<int:pk>/answers/', views.AnswerList.as_view()),
    # path('answers/<int:pk>/', views.AnswerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)