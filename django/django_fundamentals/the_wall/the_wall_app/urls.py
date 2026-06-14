from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('login',views.login),
    path('register',views.register),
    path('logout',views.logout),
    path('wall',views.wall),
    path('message/create',views.create_message),
    path('comment/create/<int:id>',views.create_comment),
    path('message/delete/<int:id>',views.delete_message),

]