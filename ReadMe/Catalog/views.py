from django.shortcuts import render
from .models import *
from django.views import generic

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    return render(
        request,
        'catalog/index.html',
        context = {
            'num_books': num_books,
            'num_authors': num_authors
        }
    )


class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/books/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/books/book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/authors/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/authors/author_detail.html'