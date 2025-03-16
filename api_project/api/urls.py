from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
from .views import CustomAuthToken

urlpatterns += [
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]

