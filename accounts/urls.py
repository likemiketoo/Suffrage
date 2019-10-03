# accounts/urls.py
from django.urls import path
from . import views

# accounts/
urlpatterns = [
    path('register', views.registration_view, name='register'),
]