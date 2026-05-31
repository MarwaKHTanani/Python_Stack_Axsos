from django.urls import path
from . import views
from blogs.views import index

urlpatterns = [
    path('', index),
    path('register', views.register),
    path('login', views.login),
    path('users/new', views.register),
    path('users', views.users),
]