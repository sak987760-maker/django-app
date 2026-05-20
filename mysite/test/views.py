from django.shortcuts import render, redirect
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

def linkify(text):
    return re.sub(r'(https?://[^\s]+)', r'<a href="\1" target="_blank">\1</a>', text)