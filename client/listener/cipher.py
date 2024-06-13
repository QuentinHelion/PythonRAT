from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

class Cipher:
    def __init__(self, key, iv, charset='utf-8'):
        self.cipher = AES.new(key, AES.MODE_CBC, iv)
        self.charset = charset

    def encrypt_message(self, message):
        padded = pad(message, AES.block_size)
        return self.cipher.encrypt(padded)

    def decrypt_message(self, message):
        decrypted = self.cipher.decrypt(message)
        unpadded = unpad(decrypted, AES.block_size)
        return unpadded.decode(self.charset)
