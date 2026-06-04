from django.db import models
from django.contrib.auth.models import User
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_batsman = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    toss_winner = models.ForeignKey(Team, related_name='toss_winner_matches', on_delete=models.CASCADE)
    toss_decision = models.CharField(max_length=100)
    overs = models.IntegerField()
    target = models.IntegerField(null=True, blank=True)
    winner = models.ForeignKey(Team, related_name='match_winner_matches', on_delete=models.CASCADE, null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name}"
