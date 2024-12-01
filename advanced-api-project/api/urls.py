from django.urls import path
from .views import BookListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    # List all books or create a new book
    path('books/', BookListView.as_view(), name='book-list-create'),

    # Retrieve details of a specific book by ID
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', CreateView.as_view(), name='book-create'),

    # Update a specific book
    path('books/update/', UpdateView.as_view(), name='book-update'),

    # Delete a specific book
    path('books/delete/', DeleteView.as_view(), name='book-delete'),
]
