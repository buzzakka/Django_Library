from django import forms
from .models import Book, Author, Genre


class AddBookForm(forms.Form):
    title = forms.CharField(
        max_length=250,
        label="Название",
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )

    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        label="Автор",
        empty_label="Автор не выбран"
    )

    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        label="Жанр",
        empty_label="Жанр не выбран"
    )

    about = forms.CharField(
        widget=forms.Textarea(),
        label="Описание книги",
        required=False
    )

    link_to_file = forms.FileField(
        label="Файл книги ",
        required=False
    )

    image = forms.ImageField(
        label="Изображение",
        required=False
    )


class AddAuthorForm(forms.Form):
    first_name = forms.CharField(
        max_length=250,
        label="Имя",
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )

    last_name = forms.CharField(
        max_length=250,
        label="Фамилия",
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )

    date_of_birth = forms.DateField(
        label="Дата рождения"
    )

    date_of_death = forms.DateField(
        required=False,
        label="Дата смерти"
    )

    about = forms.CharField(
        widget=forms.Textarea(),
        label="Об авторе",
        required=False
    )

    image = forms.ImageField(
        label="Изображение",
        required=False
    )


class AddGenreForm(forms.Form):
    genre = forms.CharField(
        max_length=250,
        label="Жанр",
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
