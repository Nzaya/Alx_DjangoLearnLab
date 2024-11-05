"# Introduction to Django" 

# Create a Book instance

### Command
```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  # Expected output: 1984 by George Orwell (1949)

# Retrieve and display all Book instances
book = Book.objects.get(id=book.id)
print(book)  # Expected output: 1984 by George Orwell (1949)


# UPDATE THE TITLE AND SAVE THE CHANGES
book.title = "Nineteen Eighty-Four"
book.save()
## Verify the update
updated_book = Book.objects.get(id=book.id)
print(updated_book)  # Expected output: Nineteen Eighty-Four by George Orwell (1949)

# DELETE THE BOOK
book.delete()
# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(all_books)  # Expected output: <QuerySet []>

