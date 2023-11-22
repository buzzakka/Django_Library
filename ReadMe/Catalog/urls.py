from django.urls import path, re_path
from . import views



urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^books/$", views.BookListView.as_view(), name="books"),
    path("book/<slug:slug>", views.BookDetailView.as_view(), name="book_detail"),
    re_path(r"^authors/$", views.AuthorListView.as_view(), name="authors"),
    path("author/<slug:slug>", views.AuthorDetailView.as_view(), name="author_detail"),
]