from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.contrib.auth import get_user_model

from ReadMe.settings import MEDIA_ROOT

from slugify import slugify


def author_media_path(instance, filename):
    new_filename = f"{instance.slug}.{filename.split('.')[-1]}"
    return f'authors/{instance.slug}/{new_filename}'


class Author(models.Model):
    first_name = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Фамилия'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        db_index=True)
    date_of_birth = models.DateField(
        verbose_name='Дата рождения'
    )
    date_of_death = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата смерти'
    )
    about = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        default="",
        verbose_name='Об авторе'
    )
    image = models.ImageField(
        upload_to=author_media_path,
        null=True,
        blank=True,
        verbose_name='Изображение'
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.first_name} {self.last_name}")
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Genre(models.Model):
    genre = models.CharField(
        max_length=200,
        db_index=True,
        unique=True,
        verbose_name='Жанр'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        db_index=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genre)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["genre"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.genre


def book_directory_path(instance, filename):
    new_filename = f"{instance.slug}.{filename.split('.')[-1]}"
    return f'books/{instance.slug}/{new_filename}'


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        db_index=True,
        verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        db_index=True,
        default=slugify(f"{title}")
    )
    author = models.ForeignKey(
        Author,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Автор'
    )
    genre = models. ManyToManyField(
        Genre,
        verbose_name='Жанр'
    )
    about = models.TextField(
        max_length=1000,
        verbose_name='Описание книги'
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5)],
        default=0,
        verbose_name='Рейтинг'
    )
    link_to_file = models.FileField(
        upload_to=book_directory_path,
        null=True,
        blank=True,
        verbose_name='Путь до файла'
    )
    image = models.ImageField(
        upload_to=book_directory_path,
        null=True,
        blank=True,
        verbose_name='Изображение'
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

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


class Bookshelf(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    book = models.ManyToManyField(
        Book,
        verbose_name='Книга'
    )

    class Meta:
        ordering = ["user"]
        verbose_name = "Книжная полка"
        verbose_name_plural = "Книжная полки"

    def __str__(self):
        return f'Книжная полка пользователя {self.user}'