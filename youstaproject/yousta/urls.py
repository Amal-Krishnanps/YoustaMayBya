from django.urls import path

from yousta.views import SignupView,SignInView,CategoryCreateView,remove_category\
    ,ClothCreateView,ClothListView,ClothUpdateView,remove_ClothView,ClothVarientCreateView

urlpatterns=[
    path("register/",SignupView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("category/add",CategoryCreateView.as_view(),name="add-category"),
    path("category/<int:pk>/remove",remove_category,name="remove-category"),
    path("cloths/add",ClothCreateView.as_view(),name="cloth-add"),
    path("cloths/all",ClothListView.as_view(),name="cloth-list"),
    path("cloths/<int:pk>/change",ClothUpdateView.as_view(),name="cloth-change"),
    path("cloths/<int:pk>/remove",remove_ClothView,name="cloth-remove"),
    path("cloths/<int:pk>/varient/add",ClothVarientCreateView.as_view(),name="add-varient")

]