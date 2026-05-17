from django.shortcuts import render
from .models import Ternal


from django.shortcuts import render
from .models import Ternal


def home(request):
    if request.method == "POST":
        text = request.POST.get("text")
        Ternal.objects.create(text=text)
    
    items = Ternal.objects.all()
    return render(request, "test.html", {"items": items})


def save_memo(request):
    if request.method == "POST":
        text = request.POST.get("text")
        Ternal.objects.create(text=text)
    
    items = Ternal.objects.all()
    return render(request, "test.html", {"items": items})