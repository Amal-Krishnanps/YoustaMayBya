from django.urls import path

from yousta.views import SignupView

urlpatterns=[
    path("register/",SignupView.as_view,name="signup"),

]