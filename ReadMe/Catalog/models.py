from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse

from ReadMe.settings import MEDIA_ROOT


def author_media_path(instance, filename):
    return f'authors/{instance.id}/{filename}'


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=False)
    date_of_death = models.DateField(blank=True, null=True)
    about = models.TextField(max_length=1000, blank=True, null=True, default="")
    image = models.ImageField(upload_to=author_media_path, null=True, blank=True)        
    
    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    


class Genre(models.Model):
    genre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.genre


def book_directory_path(instance, filename):
    return f'books/{instance.id}/{filename}'


def book_image_directory_path(instance, filename):
    return f'books/{instance.id}/{filename}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    genre = models.ManyToManyField(Genre)
    about = models.TextField(max_length=1000)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=0)
    link_to_file = models.FileField(upload_to=book_directory_path, null=True, blank=True)
    image = models.ImageField(upload_to=book_directory_path, null=True, blank=True)
    
    def display_genre(self):
        return ', '.join([genre.genre for genre in self.genre.all()[:3]])
    display_genre.short_description = 'Genre'
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["title", "author"]
    