from rest_framework import generics
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetching all book records
    serializer_class = BookSerializer  # Using the serializer



