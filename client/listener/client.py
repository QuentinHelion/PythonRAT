import socket


class Client:
    def __init__(self, host, port=8888):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((host, port))
        except ConnectionRefusedError:
            print("Connection refused")

    def send(self, data):
        try:
            self.sock.sendall(data)
            return True
        except:
            return False

    def listen(self):
        while True:
            data = self.sock.recv(4096)
            if data:
                return print(data)
