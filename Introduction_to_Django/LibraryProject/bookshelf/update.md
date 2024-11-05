# Update the title and save changes
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(updated_book)  # Expected output: Nineteen Eighty-Four by George Orwell (1949)
