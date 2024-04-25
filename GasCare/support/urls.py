from django.contrib import admin
from django.urls import path,include
from support import views

urlpatterns = [
    path('signin/',views.signin, name="signin"),
    path('sign-up/', views.signup, name="signup"),
    path('logout/', views.user_logout, name = "logout"),
    path('',views.home, name="home"),
]
