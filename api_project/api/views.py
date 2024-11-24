from rest_framework.generics import ListAPIView
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetching all book records
    serializer_class = BookSerializer  # Using the serializer



