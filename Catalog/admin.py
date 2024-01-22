from django.contrib import admin
from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'date_of_death', )
    ordering = ('last_name', 'first_name', )
    search_fields = ('last_name', 'first_name', )

    @admin.display(description='Автор', ordering='last_name')
    def full_name(self, author: Author):
        return f'{author.last_name} {author.first_name}'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('genre', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', )
    search_fields = ('title', 'author__last_name', )


@admin.register(Bookshelf)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('user', )
