import socket


class Server:
    def __init__(self, port=8888):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))

    def listen(self):
        self.sock.listen(5)
        while True:
            conn, addr = self.sock.accept()
            data = conn.recv(4096)
            return data

    def stop(self):
        self.sock.close()
        self.sock = None

    def send(self, data):
        self.sock.sendall(data)
        return self.sock.recv(4096)
