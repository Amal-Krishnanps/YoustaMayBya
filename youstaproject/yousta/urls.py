from django.urls import path

from yousta.views import SignupView,SignInView

urlpatterns=[
    path("register/",SignupView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin")

]