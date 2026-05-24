from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Ternal
import re

def home(request):
    if request.method == "POST":
        text = request.POST.get("text")
        Ternal.objects.create(text=text)
        return redirect('/')
    items = Ternal.objects.all().order_by('-id')
    for item in items:
        item.text = linkify(item.text)
    return render(request, "test.html", {"items": items})

def save_memo(request):
    if request.method == "POST":
        text = request.POST.get("text")
        Ternal.objects.create(text=text)
        return redirect('/')
    items = Ternal.objects.all().order_by('-id')
    for item in items:
        item.text = linkify(item.text)
    return render(request, "test.html", {"items": items})

def delete_all(request):
    Ternal.objects.all().delete()
    return redirect('/')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('/login/')

def linkify(text):
    return re.sub(r'(https?://[^\s]+)', r'<a href="\1" target="_blank">\1</a>', text)