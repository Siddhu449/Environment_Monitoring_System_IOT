from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Match

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MatchSetupForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team1', 'team2', 'toss_winner', 'toss_decision', 'overs']
