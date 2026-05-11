import requests
import re
import random
from django.shortcuts import render

def home(request):
    
    return render(request, "test.html", {"msg":""})
