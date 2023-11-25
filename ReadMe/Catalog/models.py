from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse

from ReadMe.settings import MEDIA_ROOT

from slugify import slugify


def author_media_path(instance, filename):
    return f'authors/{instance.id}/{filename}'


class Author(models.Model):
    first_name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=200, db_index=True, verbose_name='Фамилия')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, default=slugify(f"{first_name} {last_name}"))
    date_of_birth = models.DateField(blank=False, verbose_name='Дата рождения')
    date_of_death = models.DateField(blank=True, null=True, verbose_name='Дата смерти')
    about = models.TextField(max_length=1000, blank=True, null=True, default="", verbose_name='Об авторе')
    image = models.ImageField(upload_to=author_media_path, null=True, blank=True, verbose_name='Изображение')        
    
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    


class Genre(models.Model):
    genre = models.CharField(max_length=200, db_index=True, verbose_name='Жанр')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, default=slugify(f'{genre}'))
    
    class Meta:
        ordering = ["genre"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
    
    def __str__(self):
        return self.genre


def book_directory_path(instance, filename):
    return f'books/{instance.id}/{filename}'


def book_image_directory_path(instance, filename):
    return f'books/{instance.id}/{filename}'


class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, default=slugify(f"{title}"))
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, verbose_name='Автор')
    genre = models. ManyToManyField(Genre, verbose_name='Жанр')
    about = models.TextField(max_length=1000, verbose_name='Описание книги')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=0, verbose_name='Рейтинг')
    link_to_file = models.FileField(upload_to=book_directory_path, null=True, blank=True, verbose_name='Путь до файла')
    image = models.ImageField(upload_to=book_directory_path, null=True, blank=True, verbose_name='Изображение')
    
    def display_genre(self):
        return ', '.join([genre.genre for genre in self.genre.all()[:3]])
    display_genre.short_description = 'Genre'
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["title", "author"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
    