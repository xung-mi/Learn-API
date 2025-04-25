# import_books.py
import os
import django

# Thiết lập môi trường Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# Import model Book
from book.models import Book

# Thêm dữ liệu vào bảng Book
def import_books():
    books = [
        {"title": "Django for Beginners", "author": "William S. Vincent"},
        {"title": "Python Crash Course", "author": "Eric Matthes"},
        {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart"},
        # Thêm nhiều sách nữa nếu cần
    ]
    
    for book in books:
        Book.objects.create(title=book["title"], author=book["author"])
        print(f"Đã thêm sách: {book['title']}")

if __name__ == "__main__":
    import_books()
