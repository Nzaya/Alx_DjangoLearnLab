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

    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

   
]
