from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer, AuthorSerializer

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

@api_view(['POST'])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_author(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['PUT'])
def update_author(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AuthorSerializer(author, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_author(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    author.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['PUT'])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)