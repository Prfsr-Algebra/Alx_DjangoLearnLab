from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    response = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(response, content_type="text/plain")

