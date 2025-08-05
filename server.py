import socket
import os
from datetime import datetime

def handle_request(request):
    if request.startswith("POST"):
        headers, body = request.split("\r\n\r\n", 1)
        name, message = [x.split("=")[1] for x in body.split("&")]
        send_to_socket_server(name, message)
        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nMessage sent!"

    with open("index.html", "r") as f:
        html = f.read()
    return f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{html}"

def send_to_socket_server(name, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("socket_server", 9000))
    timestamp = datetime.now().isoformat()
    data = f"{name}::{message}::{timestamp}"
    s.send(data.encode())
    s.close()

def start_server():
    HOST = ""
    PORT = 8080
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Web server running on http://localhost:8080")

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024).decode()
        response = handle_request(request)
        client_socket.sendall(response.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
