from django.contrib import admin
from .models import User, Profile,Question, Answer
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)