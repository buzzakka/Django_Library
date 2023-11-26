from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from .forms import AddBookForm, AddAuthorForm, AddGenreForm

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
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/books/book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/authors/author_list.html'
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/authors/author_detail.html'


def AddAuthor(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # try:
                
            # except
    else:
        form = AddAuthorForm()

    return render(request, 'catalog/authors/add_author.html', {'form': form})


def AddBook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # try:
                
            # except
    else:
        form = AddBookForm()

    return render(request, 'catalog/books/add_book.html', {'form': form})


def AddGenre(request):
    if request.method == 'POST':
        form = AddGenreForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Genre.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, "Ошибка добавления объекта")
    else:
        form = AddGenreForm()

    return render(request, 'catalog/books/add_genre.html', {'form': form})