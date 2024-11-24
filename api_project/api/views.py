from rest_framework import generics
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetching all book records
    serializer_class = BookSerializer  # Using the serializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions 
    (list, create, retrieve, update, destroy) for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer



