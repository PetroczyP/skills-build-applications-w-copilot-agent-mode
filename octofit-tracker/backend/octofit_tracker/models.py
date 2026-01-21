from bson import ObjectId
from djongo import models
from django.utils import timezone


class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"


class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    motto = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "teams"

    def __str__(self) -> str:
        return self.name


class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    calories = models.IntegerField()
    performed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "activities"

    def __str__(self) -> str:
        return f"{self.user_email} - {self.activity_type}"


class LeaderboardEntry(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    team = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    rank = models.IntegerField(default=1)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "leaderboard"

    def __str__(self) -> str:
        return f"{self.team} ({self.rank})"


class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    target_muscle = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "workouts"

    def __str__(self) -> str:
        return self.title
