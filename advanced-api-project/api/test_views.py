from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", publication_year=2022, author=self.author)
        self.user = User.objects.create_user(username='testuser', password='password')
    
    def test_book_list(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_create_book_unauthenticated(self):
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post('/books/', data)
        self.assertEqual(response.status_code, 403)
    
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post('/books/', data)
        self.assertEqual(response.status_code, 201)

