from django import forms
from .models import User

class UserIconForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['icon']