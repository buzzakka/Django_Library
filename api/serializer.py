from rest_framework import serializers
from Catalog.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'about')
