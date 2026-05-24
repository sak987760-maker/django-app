from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Ternal
import re

User = get_user_model()

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError('パスワードが一致しません')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

def home(request):
    if request.method == "POST":
        text = request.POST.get("text")
        Ternal.objects.create(text=text, user=request.user)
        return redirect('/')
    items = Ternal.objects.filter(user=request.user).order_by('-id')
    for item in items:
        item.text = linkify(item.text)
    return render(request, "test.html", {"items": items})

def save_memo(request):
    if request.method == "POST":
        text = request.POST.get("text")
        Ternal.objects.create(text=text, user=request.user)
        return redirect('/')
    items = Ternal.objects.filter(user=request.user).order_by('-id')
    for item in items:
        item.text = linkify(item.text)
    return render(request, "test.html", {"items": items})

def delete_all(request):
    Ternal.objects.all().delete()
    return redirect('/')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
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
def update_icon(request):
    if request.method == "POST" and request.FILES.get('icon'):
        request.user.icon = request.FILES['icon']
        request.user.save()
    return redirect('/')