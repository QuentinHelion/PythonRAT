from listener.client import Client
from listener.cipher import Cipher
import json


def main():
    listener = Client('127.0.0.1', 8888)
    cipher = Cipher()

    print('Listening on port 8888...')
    while True:
        data = listener.listen()
        data = cipher.decrypt_message(data)
        data = json.loads(data)
        if data is not None:
            print(data)
            # data = None


if __name__ == '__main__':
    main()
