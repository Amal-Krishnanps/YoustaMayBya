from django.shortcuts import render

from django.views.generic import CreateView
from yousta.forms import RegistrationForm
from yousta.models import User
from django.urls import reverse_lazy

class SignupView(CreateView):
    template_name="yousta/register.html"
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("signup")

