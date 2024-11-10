from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library

def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the 'list_books.html' template with the list of books
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'  