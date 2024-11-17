# Retrieve and display all Book instances
book = Book.objects.get(id=book.id)
print(book)  # Expected output: 1984 by George Orwell (1949)
