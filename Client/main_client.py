import socket
import sys

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_message(self, message):
        self.socket.sendall(message.encode())
    
    def receive_message(self):
        data = self.socket.recv(1024)
        return data.decode()
    
    def close(self):
        if self.socket:
            self.socket.close()

HOST = '127.0.0.1'
PORT = 8005

client = TCPClient(HOST, PORT)
client.connect()
client.send_message("Hello свинина")
data = client.receive_message()
print(f"Received {data!r}")
client.close        
        