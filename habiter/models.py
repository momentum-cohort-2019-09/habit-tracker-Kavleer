from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    def ___str___(self): 
        return self.username


class Habit(models.Model):
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, blank=False, null=True, related_name='habits')
    title = models.CharField(max_length=100, blank=True, null=True)
    target = models.TextField(blank=True, null=True)
    measure = models.TextField(blank=True, null=True)
    post_date = models.DateField(default=timezone.now)
    is_reached = models.BooleanField(default=False)
    observer = models.ManyToManyField(to='User', related_name="watched_habits", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    habit = models.ForeignKey(
        to=Habit, on_delete=models.CASCADE, blank=True, null=True, related_name='responses')
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, blank=True, null=True, related_name='comments')
    body = models.TextField(blank=True, null=True)
    post_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.title