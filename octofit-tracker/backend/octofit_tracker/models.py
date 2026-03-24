from django.db import models
from djongo import models as djongo_models
from django.contrib.auth.models import AbstractUser
from bson import ObjectId

class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    email = models.EmailField(unique=True)
    team = djongo_models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()    # in km

class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
