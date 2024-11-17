from django.contrib import admin
from .models import Book

# Define custom admin configuration for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') # Display fields in list view
    list_filter = ('publication_year',)  # Display fields in list view
    search_fields = ('title', 'author') # Enable search by title and author

# Register the Book model with custom admin options
admin.site.register(Book, BookAdmin)
