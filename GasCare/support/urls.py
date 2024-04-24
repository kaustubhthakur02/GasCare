from django.contrib import admin
from django.urls import path,include
from support import views

urlpatterns = [
    path('',views.signin, name="signin"),
    path('sign-up/', views.signup, name="signup"),
    path('home/',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
]
