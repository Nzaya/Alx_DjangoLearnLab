from django.shortcuts import redirect, render
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# List all books
def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the 'list_books.html' template with the list of books
    return render(request, 'list_books.html', {'books': books})

# Library detail view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)  # Ensure authenticate is imported
            login(request, user)
            # return redirect('home')  # Redirect to a home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect('home')  # Redirect to a home page after login
    else:
        form = AuthenticationForm()
    return render(request,'relationship_app/login.html', {'form': form})

# Logout View (Using Django's built-in LogoutView)
# This will automatically log the user out and redirect them to the login page
class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirect to login after logging out

# Function to check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view (Only accessible by Admin)
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin Dashboard.")

# Librarian view (Only accessible by Librarians)
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian Dashboard.")

# Member view (Only accessible by Members)
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome to the Member Dashboard.")
