import socket


class Communication:
    def __init__(self, port=8888):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port

    def init_listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', self.port))
        sock.listen()
        while True:
            conn, addr = sock.accept()
            data = conn.recv(4096)
            sock.close()
            if data:
                return {
                    "data": data,
                    "addr": addr
                }

    def listen(self):
        while True:
            conn, addr = self.sock.accept()
            return conn.recv(4096)

    def connect(self, ip):
        self.sock.connect((ip, self.port))

    def stop(self):
        self.sock.close()
        self.sock = None

    def send(self, data):
        self.sock.sendall(data)

    def prompt(self, data):
        self.sock.sendall(data)
        result = self.sock.recv(4096)
        return result
