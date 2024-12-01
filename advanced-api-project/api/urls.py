from django.urls import path
from .views import BookListView, CreateView, DetailView, UpdateView, DeleteView

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Create a new book
    path('books/create/', CreateView.as_view(), name='book-create'),

    # Retrieve details of a specific book by ID
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),

    # Update a specific book by ID
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'),

    # Delete a specific book by ID
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),
]
