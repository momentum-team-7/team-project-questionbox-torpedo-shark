from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    join_year = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

class Answer(models.Model):
    body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_author')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='replies')
    likes = models.IntegerField(default=0) # new

    def __str__(self):
        return f'{self.body}'


class Question(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    tags = models.CharField(max_length=200)
    likes = models.IntegerField(default=0) # new
    answered = models.BooleanField(default=False) # new

    class Genre(models.TextChoices):
        hiphop = 'Hiphop', _('Hip-hop')
        rap = 'Rap', _('Rap')
        jazz = 'Jazz', _('Jazz')
        techno = 'Techno', _('Techno')
        rb = 'R & B', _('R & B')
        punk = 'Punk', _('Punk')
        rock = 'Rock', _('Rock')
        alternative = 'Alternative', _('Alternative')
        metal = 'Metal', _('Metal')
        country = 'Country', _('Country')
        indie = 'Indie', _('Indie')
        edm = 'EDM', _('EDM')
        bootybass = 'Booty Bass', _('Booty Bass')
        gossip = 'gossip', _('Gossip')
        other = 'Other', _('Other')
    
    musicgenre = models.CharField(choices=Genre.choices, default=Genre.bootybass, max_length=100)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.title} {self.musicgenre}'

