from django.urls import path
from . import views

urlpatterns = [
    path("", views.books),
    path("books/create", views.create_book),
    path("books/<int:book_id>", views.book_details),
    path("books/add_author", views.add_author_to_book),
    path("authors", views.authors),
    path("authors/create", views.author_create),
    path("authors/<int:author_id>", views.author_details),
    path("authors/add_book", views.add_book_to_author),
]
