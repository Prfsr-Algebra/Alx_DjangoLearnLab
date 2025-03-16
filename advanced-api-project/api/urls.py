from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
from django.urls import path
from .views import CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/create/', CreateView.as_view(), name='create_book'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='update_book'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='delete_book'),
]

