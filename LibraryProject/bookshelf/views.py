from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# View to list all books (with 'can_view' permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View to add a new book (with 'can_create' permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new book to the database
            return redirect('book_list')  # Redirect to the book list page
    else:
        form = BookForm()

    return render(request, 'bookshelf/book_form.html', {'form': form})

# View to edit an existing book (with 'can_edit' permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Fetch the book by its ID

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # Prepopulate form with book data
        if form.is_valid():
            form.save()  # Save the changes to the book
            return redirect('book_list')  # Redirect to the book list page
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/book_form.html', {'form': form, 'book': book})

# View to delete a book (with 'can_delete' permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Fetch the book to delete
    book.delete()  # Delete the book from the database
    return redirect('book_list')  # Redirect to the book list page



