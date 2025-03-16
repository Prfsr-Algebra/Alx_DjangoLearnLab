"""
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
from rest_framework.filters import SearchFilter

class BookListView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'author__name']

from rest_framework.filters import OrderingFilter

class BookListView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['title', 'publication_year']
"""
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book  # Replace with your model

class CreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'published_date']  # Replace with actual fields
    template_name = 'book_form.html'  # Ensure you have this template
    success_url = reverse_lazy('book_list')  # Change if needed

class UpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class DeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'  # Ensure you have this template
    success_url = reverse_lazy('book_list')

