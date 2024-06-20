import socket


class Communication:
    def __init__(self, host, port=8888):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.conn = None

    def init_send(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.sendall(data)
        sock.close()

    def init_listen(self):
        self.sock.bind(('127.0.0.1', self.port))
        self.sock.listen()
        self.conn, addr = self.sock.accept()

    def send(self, data):
        try:
            self.sock.sendall(data)
            return True
        except:
            return False

    def listen(self):
        while True:
            data = self.conn.recv(4096)
            if data:
                return {
                    "data": data,
                    "conn": self.conn
                }
