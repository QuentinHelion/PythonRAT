from listener.server import Server
import json

def main():
    listener = Server()
    print('Listening on port 8888...')
    while True:
        data = listener.listen()
        data = json.loads(data.decode('utf-8'))
        if data is not None:
            print(data["message"])
            data = None


if __name__ == '__main__':
    main()
