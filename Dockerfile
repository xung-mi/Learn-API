# Dockerfile
FROM python:3.11-slim

# Cài thêm dependencies để build mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work dir
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Cài đặt pip packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code
COPY ./src /app

# Cổng mặc định
EXPOSE 8000

# Lệnh mặc định khi chạy container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
