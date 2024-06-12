import socket


class Client:
    def __init__(self, host, port=8888):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))

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
            return data
