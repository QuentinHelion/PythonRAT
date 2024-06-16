from time import sleep

from listener.communication import Communication
from listener.cipher import Cipher
from tools.env import EnvReader
import json


def main():
    env = EnvReader()
    listener = Communication(
        host=env.get('SERVER_ADDR').encode('utf-8'),
        port=int(env.get('SERVER_PORT'))
    )
    cipher = Cipher(
        key=env.get("CRYPTO_KEY").encode('utf-8'),
        iv=env.get("CRYPTO_IV").encode('utf-8')
    )

    listener.init_send(json.dumps({
        "type": "init",
        "commands": "setup done"
    }).encode('utf-8'))

    sleep(2)

    listener.init_listen()

    print('Listening on port 8888...')
    while True:
        listen = listener.listen()
        conn = listen["conn"]
        data = cipher.decrypt_message(listen["data"])
        data = json.loads(data)
        if data is not None:
            print(data)
            response = json.dumps({
                'command': 'download',
                'params': "params"
            }).encode('utf-8')

            # response = cipher.encrypt_message(f"Commands received: {data['command']}")
            conn.sendall(cipher.encrypt_message(response))
            # if data["commands"] == "download":

            # data = None


if __name__ == '__main__':
    main()
