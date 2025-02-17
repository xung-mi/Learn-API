from xmlrpc.server import SimpleXMLRPCServer

# Hàm cần gọi từ xa
def add(x, y):
    return x + y

# Khởi tạo server RPC
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server đang chạy trên cổng 8000...")

# Đăng ký hàm để client có thể gọi
server.register_function(add, "add")

# Chạy server
server.serve_forever()
