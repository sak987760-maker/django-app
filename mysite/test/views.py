from django.shortcuts import render
from .models import Ternal


def home(request):
    return render(request, "test.html")


def save_memo(request):

    if request.method == "POST":
        text = request.POST.get("text")

        Ternal.objects.create(text=text)

    return render(request, "test.html")