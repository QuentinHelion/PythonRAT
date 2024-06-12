from time import sleep
from listener.client import Client
import json


def main():
    listener = Client('127.0.0.1', 8888)

    while True:
        data = {
            "message": "Hello World!"
        }
        data = json.dumps(data).encode('utf-8')
        # data = b"Hello World"
        if listener.send(data):
            print("data send")
        else:
            print("error on data send")
            listener = Client('127.0.0.1', 8888)
        sleep(3)


if __name__ == '__main__':
    main()
