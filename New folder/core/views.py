from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Match


# =======================
# Static Pages
# =======================

def home(request):
    return render(request, 'core/home.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    return render(request, 'core/contact.html')


# =======================
# Auth Views
# =======================

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Please enter all required information.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            # Use Django's create_user to hash the password
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Signup successful! Please login.")
            return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check credentials using Django's system
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Start session
            return redirect('match_setup')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)  # Clear session
    messages.success(request, "You have been logged out.")
    return redirect('home')


# =======================
# Match Views
# =======================

@login_required
def match_setup_view(request):
    return render(request, 'match_setup.html')


@login_required
def match_history(request):
    matches = Match.objects.filter(user=request.user)
    return render(request, 'match_history.html', {'matches': matches})


@login_required
def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id, user=request.user)
    return render(request, 'match_detail.html', {'match': match})


@login_required
def delete_match(request, match_id):
    match = get_object_or_404(Match, id=match_id, user=request.user)
    if request.method == "POST":
        match.delete()
        messages.success(request, "Match deleted successfully.")
        return redirect('match_history')
    return render(request, 'confirm_delete.html', {'match': match})


@login_required
def save_match(request):
    if request.method == 'POST':
        Match.objects.create(
            user=request.user,
            team1=request.POST['team1'],
            team2=request.POST['team2'],
            toss_winner=request.POST['toss_winner'],
            decision=request.POST['decision'],
            result=request.POST['result'],
            overs=request.POST['overs'],
            wickets=request.POST['wickets'],
            runs=request.POST['runs'],
            target=request.POST['target']
        )
        messages.success(request, "Match saved successfully.")
        return redirect('match_history')

    return redirect('match_setup')
