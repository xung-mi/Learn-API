from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer

def get_books(request):
    # Lấy tất cả các cuốn sách
    books = Book.objects.all()
    for book in books:
        print(book.title, book.author)
    return render(request, 'book/book_list.html', {'books': books})

def get_books_by_author(request, author_name):
    # Lấy các cuốn sách của một tác giả cụ thể
    books = Book.objects.filter(author=author_name)
    for book in books:
        print(book.title)
    return HttpResponse(f"Books by {author_name} listed in the terminal")

def get_single_book(request, book_id):
    # Lấy cuốn sách theo ID
    try:
        book = Book.objects.get(id=book_id)
        print(book.title)
    except Book.DoesNotExist:
        return HttpResponse("Book not found")
    return HttpResponse(f"Book: {book.title} by {book.author}")

def get_top_books(request):
    # Lấy 5 cuốn sách đầu tiên
    books = Book.objects.all()[:5]
    for book in books:
        print(book.title)
    return HttpResponse("Top 5 books listed in the terminal")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@api_view(['GET'])
def get_authors(request):
    authors = Author.objects.all()  # Lấy tất cả các tác giả từ database
    serializer = AuthorSerializer(authors, many=True)  # Chuyển đổi sang JSON
    return Response(serializer.data)