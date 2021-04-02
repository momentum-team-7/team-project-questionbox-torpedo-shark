from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Answer(models.Model):
    body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_author')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f'{self.body}'


class Question(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    tags = models.CharField(max_length=200)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.title}'