from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL pattern for the function-based view to list all books
    path('books/', views.list_books, name='list_books'),

    # URL pattern for the class-based view to display library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # User authentication URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

   
]
