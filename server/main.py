from listener.server import Server
import json


def main():
    listener = Server()
    print('Listening on port 8888...')
    while True:
        uinput = input("> ")
        data = json.dumps(
            {
                'message': uinput
            }
        ).encode('utf-8')

        listener.send(data)


if __name__ == '__main__':
    main()
