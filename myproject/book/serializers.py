from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']  # Chỉ lấy id và name của tác giả

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nối dữ liệu tác giả vào sách

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']  # Các trường muốn trả về trong API

