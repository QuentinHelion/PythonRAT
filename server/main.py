from listener.communication import Communication
from listener.cipher import Cipher
from tools.env import EnvReader
from commands.help import help
import json


def main():
    env = EnvReader()

    listener = Communication(
        port=int(env.get("SERVER_PORT"))
    )

    while True:
        client_init = listener.init_listen()
        print(client_init)
        if client_init is not None:
            client_addr = client_init[0]
            break
        else:
            print(client_init)

    listener.connect(client_addr)

    cipher = Cipher(
        key=env.get("CRYPTO_KEY").encode('utf-8'),
        iv=env.get("CRYPTO_IV").encode('utf-8')
    )
    while True:
        uinput = input("> ")

        if uinput == "help":
            help()
        else:
            data = json.dumps(
                {
                    'message': uinput
                }
            ).encode('utf-8')

            listener.send(cipher.encrypt_message(data))


if __name__ == '__main__':
    main()
