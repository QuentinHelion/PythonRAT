import socket


class Server:
    def __init__(self, port=8888):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', port))

    def listen(self):
        self.sock.listen(5)
        while True:
            conn, addr = self.sock.accept()
            return conn.recv(4096)

    def stop(self):
        self.sock.close()
        self.sock = None

    def send(self, data):
        try:
            self.sock.sendall(data)
            return True
        except:
            return False
