from django.urls import path
from . import views
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # URL pattern for the function-based view to list all books
    path('books/', views.list_books, name='list_books'),

    # URL pattern for the class-based view to display library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # User authentication URLs
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    path('books/', views.list_books, name='book_list'),  # List all books
    path('books/add/', views.add_book, name='add_book'),  # Add a new book
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),  # Edit an existing book
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),  # Delete a book


   
]
