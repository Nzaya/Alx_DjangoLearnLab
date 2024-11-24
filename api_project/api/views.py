from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieving all Book objects
    serializer_class = BookSerializer  # Using the BookSerializer for formatting


