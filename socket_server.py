import socket
from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")
db = client.chat
collection = db.messages

def start_server():
    HOST = ""
    PORT = 9000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("TCP Socket server running...")

    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024).decode()
        if data:
            name, message, timestamp = data.split("::")
            collection.insert_one({
                "name": name,
                "message": message,
                "timestamp": timestamp
            })
            print(f"[{timestamp}] {name}: {message}")
        client_socket.close()

if __name__ == "__main__":
    start_server()
