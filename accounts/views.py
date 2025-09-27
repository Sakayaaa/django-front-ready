from django.shortcuts import render, redirect
from .models import UserProfile, Experience, Education
from .forms import AddEducationForm, AddExperienceForm
from django.contrib.auth.decorators import login_required


@login_required
def addeducation(request):
    if request.method == 'POST':
        form = AddEducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user.userprofile
            education.save()
            return redirect('dashboard')

    form = AddEducationForm()
    return render(request, 'accounts/addeducation.html', {'form': form})


@login_required
def addexperience(request):
    if request.method == 'POST':
        form = AddExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user.userprofile
            experience.save()
            return redirect('dashboard')

    form = AddExperienceForm()
    return render(request, 'accounts/addexperience.html', {'form': form})


def createprofile(request):
    return render(request, 'accounts/createprofile.html', {})


def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})


def login(request):
    return render(request, 'accounts/login.html', {})


def profile(request, id):
    user_profile = UserProfile.objects.get(id=id)
    return render(request, 'accounts/profile.html', {'user_profile': user_profile})


def profiles(request):
    return render(request, 'accounts/profiles.html', {})


def register(request):
    return render(request, 'accounts/register.html', {})


