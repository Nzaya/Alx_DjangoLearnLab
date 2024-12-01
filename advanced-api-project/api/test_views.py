from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create some books to test with
        self.book1 = Book.objects.create(title="Book 1", author="Author 1", publication_year=2020)
        self.book2 = Book.objects.create(title="Book 2", author="Author 2", publication_year=2021)
        
        # Define the URLs for the endpoints
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.book_create_url = reverse('book-create')
        self.book_update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.book_delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    def test_get_books_list(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two books should be returned

    def test_create_book(self):
        # Test with authentication
        self.client.login(username='testuser', password='password123')
        data = {'title': 'Book 3', 'author': 'Author 3', 'publication_year': 2022}
        response = self.client.post(self.book_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Book 3')  # Check that the title is correctly saved

    def test_create_book_without_authentication(self):
        data = {'title': 'Book 3', 'author': 'Author 3', 'publication_year': 2022}
        response = self.client.post(self.book_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Should return Forbidden without authentication

    def test_update_book(self):
        self.client.login(username='testuser', password='password123')
        data = {'title': 'Updated Book 1', 'author': 'Author 1', 'publication_year': 2020}
        response = self.client.put(self.book_update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book 1')  # Ensure the title was updated

    def test_update_book_without_authentication(self):
        data = {'title': 'Updated Book 1', 'author': 'Author 1', 'publication_year': 2020}
        response = self.client.put(self.book_update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Should return Forbidden without authentication

    def test_delete_book(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Book should be deleted
        self.assertEqual(Book.objects.count(), 1)  # One book should remain

    def test_delete_book_without_authentication(self):
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Should return Forbidden without authentication

    def test_book_search(self):
        response = self.client.get(self.book_list_url, {'search': 'Book 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book matches the search term

    def test_book_filter_by_author(self):
        response = self.client.get(self.book_list_url, {'author': 'Author 2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book matches the author

    def test_book_ordering_by_publication_year(self):
        response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)  # The first book should have the earlier publication year

