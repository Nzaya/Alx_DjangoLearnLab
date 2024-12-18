from django.urls import include, path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Creating a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('books/', BookList.as_view(), name='book-list'),  # Maps '/books/' to the BookList view

    # Include the router URLs for the BookViewSet
    path('', include(router.urls)),  # Includes all routes registered with the router
]
