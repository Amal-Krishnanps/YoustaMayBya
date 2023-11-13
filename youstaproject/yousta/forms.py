from django import forms


from yousta.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","phone","address"]
        