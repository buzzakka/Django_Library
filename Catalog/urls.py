from django.urls import path, include
from . import views

app_name = 'catalog'

authors_urls = [
    path('', views.AuthorListView.as_view(), name='authors'),
    path('add_author', views.AddAuthor.as_view(), name='add_author'),
    path('<slug:slug>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('<slug:slug>/edit', views.EditAuthor.as_view(), name='edit_author'),
    path('<slug:slug>/delete', views.DeleteAuthor.as_view(), name='delete_author'),
]

books_urls = [
    path('', views.BookListView.as_view(), name='books'),
    path('add_book', views.AddBook.as_view(), name='add_book'),
    path('add_genre', views.AddGenre.as_view(), name='add_genre'),
    path('<slug:slug>', views.BookDetailView.as_view(), name='book_detail'),
    path('<slug:slug>/edit', views.EditBook.as_view(), name='edit_book'),
    path('<slug:slug>/delete', views.DeleteBook.as_view(), name='delete_book'),
]

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('authors/', include(authors_urls)),
    path('books/', include(books_urls)),
    path('bookshelf/', views.BookshelfDetailView.as_view(), name='bookshelf'),
]
