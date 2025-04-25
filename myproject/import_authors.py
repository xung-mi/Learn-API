# import_books.py
import os
import django

# Thiết lập môi trường Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()


# Import mô hình Author
from book.models import Author

# Tạo một tác giả mới
author = Author.objects.create(
    name="George R.R. Martin"
)

# Kiểm tra tác giả đã được tạo chưa
print(f"Created author: {author.name}")
