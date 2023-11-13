from django.shortcuts import render

from django.views.generic import CreateView,FormView
from yousta.forms import LoginForm, RegistrationForm
from yousta.models import User
from django.urls import reverse_lazy
from django.contrib import messages

class SignupView(CreateView):
    template_name="yousta/register.html"
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("signup")

    def form_valid(self, form):
        messages.success(self.request,"Account Created")
        return super().form_valid(form)    


    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)    
    
class SignInView(FormView):
    template_name="yousta/login.html"
    form_class=LoginForm