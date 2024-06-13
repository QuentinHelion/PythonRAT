from listener.server import Server
from listener.cipher import Cipher
import json


def main():
    listener = Server()
    cipher = Cipher()
    print('Connect on port 8888...')
    while True:
        uinput = input("> ")
        data = json.dumps(
            {
                'message': uinput
            }
        ).encode('utf-8')

        listener.send(cipher.encrypt_message(data))



if __name__ == '__main__':
    main()
