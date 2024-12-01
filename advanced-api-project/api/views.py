from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    """
    Handles retrieving a list of all books and creating a new book.
    Accessible to all users, but only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        """
        Custom logic before saving the serializer during book creation.
        """
        # Example: Automatically assign the logged-in user as the book's author (if applicable)
        serializer.save()

    def get_queryset(self):
        """
        Filter the queryset based on the `author` query parameter.
        """
        queryset = super().get_queryset()
        author_name = self.request.query_params.get('author')  # Get the author name from the query parameters
        if author_name:
            queryset = queryset.filter(author__name=author_name)  # Filter books by author name
        return queryset


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, or deleting a specific book by ID.
    Only authenticated users can update or delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
