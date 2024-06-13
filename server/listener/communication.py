import socket


class Communication:
    def __init__(self, port=8888):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port

    def init_listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', self.port))
        sock.listen(5)
        while True:
            conn, addr = sock.accept()
            sock.close()
            return addr

    def listen(self):
        self.sock.listen(5)
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
