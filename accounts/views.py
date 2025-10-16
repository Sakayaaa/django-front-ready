import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Experience, Education
from .forms import AddEducationForm, AddExperienceForm, UserProfileForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.urls import reverse


@login_required
def add_education(request):
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
def edit_education(request, id):
    education = get_object_or_404(
        Education, id=id, user=request.user.userprofile)

    if request.method == "POST":
        form = AddEducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = AddEducationForm(instance=education)
    return render(request, 'accounts/addeducation.html', {'form': form})


@login_required
def delete_education(request, id):
    education = get_object_or_404(
        Education, id=id, user=request.user.userprofile)

    if request.method == "POST":
        education.delete()
        return redirect('dashboard')
    return redirect('dashboard')


@login_required
def add_experience(request):
    if request.method == 'POST':
        form = AddExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user.userprofile
            experience.save()
            return redirect('dashboard')

    form = AddExperienceForm()
    return render(request, 'accounts/addexperience.html', {'form': form})


@login_required
def edit_experience(request, id):
    experience = get_object_or_404(
        Experience, id=id, user=request.user.userprofile)

    if request.method == "POST":
        form = AddExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = AddExperienceForm(instance=experience)
    return render(request, 'accounts/addexperience.html', {'form': form})


@login_required
def delete_experience(request, id):
    experience = get_object_or_404(
        Experience, id=id, user=request.user.userprofile)

    if request.method == "POST":
        experience.delete()
        return redirect("dashboard")
    return redirect("dashboard")


@login_required
def create_profile(request):
    user = request.user
    try:
        user_profile = user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile', id=profile.id)
    form = UserProfileForm(instance=user_profile)
    return render(request, 'accounts/createprofile.html', {'form': form})


@login_required
def dashboard(request):
    userprofile = request.user.userprofile
    experience_list = userprofile.experience_set.all().order_by('-id')
    education_list = userprofile.education_set.all().order_by('-id')
    return render(request, 'accounts/dashboard.html', {
        'userprofile': userprofile,
        'experience_list': experience_list,
        'education_list': education_list
    })


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)

        if user:
            django_login(request, user)
            try:
                _ = user.userprofile
                return redirect('dashboard')
            except UserProfile.DoesNotExist:
                return redirect('create_profile')
        else:
            return render(request, 'accounts/login.html', {'error': 'error'})
    return render(request, 'accounts/login.html', {})


def logout(request):
    django_logout(request)
    return redirect('login')


@login_required
def profile(request, id):
    user_profile = UserProfile.objects.get(id=id)
    skills_list = user_profile.skills.split(',') if user_profile.skills else []
    experience_list = user_profile.experience_set.all()
    education_list = user_profile.education_set.all()
    github_repos = []

    if user_profile.github_username:
        try:
            url = f"https://api.github.com/users/{user_profile.github_username}/repos?sort=updated&per_page=5"
            response = requests.get(url)
            if response.status_code == 200:
                github_repos = response.json()
        except Exception as e:
            print("GitHub API error:", e)

    return render(request, 'accounts/profile.html', {
        'user_profile': user_profile,
        'skills_list': skills_list,
        'experience_list': experience_list,
        'education_list': education_list,
        'github_repos': github_repos,
    })


@login_required
def profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'accounts/profiles.html', {'profiles': profiles})


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            return (redirect('create_profile'))

    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def delete_account(request):
    user = request.user
    if request.method == "POST":
        django_logout(request)
        user.delete()
        return redirect('index')
    return redirect('dashboard')
