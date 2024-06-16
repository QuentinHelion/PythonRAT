import socket


class Communication:
    def __init__(self, host, port=8888):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def init_send(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.sendall(data)
        sock.close()

    def init_listen(self):
        self.sock.bind(('', self.port))

    def send(self, data):
        try:
            self.sock.sendall(data)
            return True
        except:
            return False

    def listen(self):
        self.sock.listen(5)
        while True:
            conn, addr = self.sock.accept()
            data = conn.recv(4096)

            if data:
                return {
                    "data": data,
                    "conn": conn
                }
