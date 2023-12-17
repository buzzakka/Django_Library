from rest_framework import generics
from .serializer import BookSerializer

from Catalog.models import Book
from .permissions import IsStaff


class BookApiList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStaff,]


class BookApiUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_required = 'Catalog.delete_book'
    permission_classes = [IsStaff,]
