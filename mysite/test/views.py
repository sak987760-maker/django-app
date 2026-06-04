from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Ternal
import re
import json
User = get_user_model()

def save_comment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request.user.comment = data.get('comment')
        request.user.save()
    from django.http import JsonResponse
    return JsonResponse({'status': 'ok'})
class SignupForm(forms.ModelForm):
    username = forms.CharField(
        help_text='150文字以下で入力してください。',
        error_messages={
            'required': 'ユーザーネームを入力してください。',
            'unique': 'このユーザーネームはすでに使われています。',
        }
    )
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'category']  # categoryを追加
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
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == "POST":
        text = request.POST.get("text")
        comment = request.POST.get("comment")
        if comment:
            request.user.comment = comment
            request.user.save()
        if text:
            obj = Ternal.objects.create(text=text, user=request.user)
            print(f"saved: {obj.id}, text: {text}")  # 追加
        return redirect('/')
    items = Ternal.objects.filter(user=request.user).order_by('-id')
    print(f"home items count: {items.count()}")  # 追加
    for item in items:
        item.text = linkify(item.text)
    return render(request, "test.html", {"items": items})
def save_memo(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('/login/')
        text = request.POST.get("text")
        obj = Ternal.objects.create(text=text, user=request.user)
        print(f"saved: id={obj.id}, user_id={obj.user_id}, text={text}")
        return redirect('/')
def delete_all(request):
    Ternal.objects.all().delete()
    return redirect('/')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST.get("name", "")  # getに変更
            user = form.save()
            user.name = name
            user.save()
            if request.FILES.get('header'):
                user.header = request.FILES['header']
                user.save()
            if request.FILES.get('icon'):
                user.icon = request.FILES['icon']
                user.save()
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
from django.db.models import Max
def home_page(request):
    from .models import Ternal
    users_with_posts = Ternal.objects.values('user').order_by('-id').distinct()
    user_ids = [t['user'] for t in users_with_posts]
    users = User.objects.filter(id__in=user_ids)
    return render(request, "home.html", {"users": users})
def user_page(request, user_id):
    page_user = User.objects.get(id=user_id)
    items = Ternal.objects.filter(user=page_user).order_by('-id')
    print(f"user_id: {user_id}, items count: {items.count()}")  # 追加
    for item in items:
        item.text = linkify(item.text)
    return render(request, "test.html", {"items": items, "page_user": page_user})