from django.urls import path
from . import views

urlpatterns = [
    # Book URLs
    path('books/', views.get_books, name='book-list'),
    path('books/create/', views.create_book, name='book-create'),
    path('books/<int:pk>/', views.get_book, name='book-detail'),
    path('books/<int:pk>/update/', views.update_book, name='book-update'),
    path('books/<int:pk>/delete/', views.delete_book, name='book-delete'),
    
    # Author URLs
    path('authors/', views.get_authors, name='author-list'),
    path('authors/create/', views.create_author, name='author-create'),
    path('authors/<int:pk>/', views.get_author, name='author-detail'),
    path('authors/<int:pk>/update/', views.update_author, name='author-update'),
    path('authors/<int:pk>/delete/', views.delete_author, name='author-delete'),
]
