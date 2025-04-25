from django.urls import path
from . import views  # Đảm bảo rằng bạn đã import views từ app book

urlpatterns = [
    path('', views.get_books, name='book_list'),  # Đường dẫn 'book/' sẽ gọi get_books
    path('top/', views.get_top_books, name='get_top_books'),  # Đường dẫn 'book/top/' sẽ gọi get_top_books
    path('api/authors/', views.get_authors, name='get_authors'),
]
