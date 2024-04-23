from django.contrib import admin
from django.urls import path,include
from support import views

urlpatterns = [
    path('',views.signin, name="signin"),
    path('sign-up/', views.signup, name="signup"),
]
