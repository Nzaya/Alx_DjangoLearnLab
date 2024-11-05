# Delete the book
book.delete()

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(all_books)  # Expected output: <QuerySet []>
