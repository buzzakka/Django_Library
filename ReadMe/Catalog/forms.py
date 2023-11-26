from django import forms
from .models import Book, Author, Genre


class AddBookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Автор не выбран", label="Автор")
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'about', 'link_to_file', 'image']


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'about', 'image',]


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre',]