from django import forms
from django.core.exceptions import ValidationError

from .models import Book, Author, Genre


class AddBookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label="Автор не выбран"
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'about', 'link_to_file', 'image']
        error_messages = {
            'title': {
                'unique': 'Такая книга уже существует'
            }
        }


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth',
                  'date_of_death', 'about', 'image',]

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if (Author.objects.filter(first_name=first_name, last_name=last_name)):
            raise ValidationError("Такой автор уже существует")

        return cleaned_data


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre',]
        error_messages = {
            'genre': {
                'unique': 'Такой жанр уже существует'
            }
        }
