import xmlrpc.client

# Kết nối đến server RPC
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Gọi hàm `add` từ xa
result = proxy.add(5, 7)
print(f"Kết quả từ server: {result}")
