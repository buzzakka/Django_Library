from typing import Any
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import *
from .forms import AddBookForm, AddAuthorForm, AddGenreForm

class Index(TemplateView):
    template_name = 'catalog/index.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title_name'] = "Главная страница"
        return context


class BookListView(ListView):
    model = Book
    template_name = 'catalog/books/book_list.html'
    paginate_by = 5
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title_name'] = "Все книги"
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/books/book_detail.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title_name'] = context['book'].title
        return context


class AuthorListView(ListView):
    model = Author
    template_name = 'catalog/authors/author_list.html'
    paginate_by = 5
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title_name'] = "Все авторы"
        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'catalog/authors/author_detail.html'
    paginate_by = 5
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title_name'] = f"{context['author'].first_name} {context['author'].last_name}"
        
        books = context['author'].book_set.all()
        paginator = Paginator(books, self.paginate_by)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        
        return context


class AddAuthor(PermissionRequiredMixin, CreateView):
    form_class = AddAuthorForm
    template_name = 'catalog/authors/add_author.html'
    permission_required = 'Catalog.add_author'
    
    extra_context = {
        'title_name': 'Добавить автора'
    }
    

class AddBook(PermissionRequiredMixin, CreateView):
    form_class = AddBookForm
    template_name = 'catalog/books/add_book.html'
    permission_required = 'Catalog.add_book'
    
    extra_context = {
        'title_name': 'Добавить книгу'
    }


class AddGenre(PermissionRequiredMixin, CreateView):
    form_class = AddGenreForm
    template_name = 'catalog/books/add_genre.html'
    success_url = reverse_lazy('add_genre')
    permission_required = 'Catalog.add_genre'
    
    extra_context = {
        'title_name': 'Добавить жанр'
    }


class EditAuthor(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'about', 'image',]
    template_name = 'catalog/authors/edit_author.html'
    permission_required = 'Catalog.change_author'
    
    extra_context = {
        'title_name': 'Редактировать автора'
    }


class EditBook(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'genre', 'about', 'link_to_file', 'image',]
    template_name = 'catalog/books/edit_book.html'
    permission_required = 'Catalog.change_book'
    
    extra_context = {
        'title_name': 'Редактировать книгу'
    }


class DeleteAuthor(PermissionRequiredMixin, DeleteView):
    model = Author
    template_name = 'catalog/authors/author_confirm_delete.html'
    permission_required = 'Catalog.delete_author'
    success_url = reverse_lazy('authors')


class DeleteBook(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'catalog/books/book_confirm_delete.html'
    success_url = reverse_lazy('books')
    permission_required = 'Catalog.delete_book'