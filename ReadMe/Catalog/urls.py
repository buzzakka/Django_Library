from django.urls import path, re_path
from . import views



urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    re_path(r"^authors/$", views.AuthorListView.as_view(), name="authors"),
    path("authors/add_author", views.AddAuthor.as_view(), name="add_author"),
    path("author/<slug:slug>", views.AuthorDetailView.as_view(), name="author_detail"),
    path("author/<slug:slug>/edit", views.EditAuthor.as_view(), name="edit_author"),
    path("author/<slug:slug>/delete", views.DeleteAuthor.as_view(), name="delete_author"),

    re_path(r"^books/$", views.BookListView.as_view(), name="books"),
    path("books/add_book", views.AddBook.as_view(), name="add_book"),
    path("books/add_genre", views.AddGenre.as_view(), name="add_genre"),
    path("book/<slug:slug>", views.BookDetailView.as_view(), name="book_detail"),
    path("book/<slug:slug>/edit", views.EditBook.as_view(), name="edit_book"),
    path("book/<slug:slug>/delete", views.DeleteBook.as_view(), name="delete_book"),
    
    path("bookshelf/", views.BookshelfDetailView.as_view(), name="bookshelf"),
    
    
]