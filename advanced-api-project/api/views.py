from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# Filter class to handle filtering of books based on title, author, and publication_year
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search for titles
    author = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search for author names
    publication_year = filters.NumberFilter()  # Exact match for publication year

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


# List view with filtering, searching, and ordering capabilities
class BookListView(generics.ListAPIView):
    """
    Handles retrieving a list of all books.
    Accessible to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No restrictions on accessing the list

    # Add filter, search, and ordering capabilities
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # Exactly this line
    filterset_class = BookFilter
    search_fields = ['title', 'author']  # Fields that can be searched
    ordering_fields = ['title', 'publication_year']  # Fields that can be used for ordering
    ordering = ['title']  # Default ordering


# Create view for adding a new book with authentication
class CreateView(generics.CreateAPIView):
    """
    Handles creating a new book.
    Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom logic before saving the serializer during book creation.
        """
        serializer.save()


# Retrieve a single book view with no restrictions on accessing the book details
class DetailView(generics.RetrieveAPIView):
    """
    Handles retrieving a single book by its ID.
    Accessible to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # No restrictions on retrieving a single book


# Update view for updating an existing book, restricted to authenticated users
class UpdateView(generics.UpdateAPIView):
    """
    Handles updating an existing book.
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete view for deleting an existing book, restricted to authenticated users
class DeleteView(generics.DestroyAPIView):
    """
    Handles deleting an existing book.
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]