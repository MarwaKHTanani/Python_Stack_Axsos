from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirect_to_shows),
    path("shows", views.shows),
    path("shows/new", views.new_show),
    path("shows/create", views.create_show),
    path("shows/<int:show_id>", views.details_show),
    path("shows/<int:show_id>/edit", views.edit_show),
    path("shows/<int:show_id>/destroy", views.delete_show),
    path("shows/<int:show_id>/update", views.update_show),
]
