from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("courses/create", views.create_course),
    path("courses/<int:course_id>/delete", views.delete_page),
    path("courses/destroy/<int:course_id>", views.destroy),
]
