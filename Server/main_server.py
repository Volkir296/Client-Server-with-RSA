import socket
import sys

HOST = "127.0.0.1"          # Объявление адреса сервера. Данный аддрес = localhost
PORT = 8005                 # Объявление порта подключения

class TCPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        with self.socket as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

server = TCPServer(HOST, PORT)
server.start()



