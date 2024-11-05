from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using related_name specified in ForeignKey
    return books

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using related_name specified in ManyToManyField
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Accessing OneToOneField through related_name
    return librarian