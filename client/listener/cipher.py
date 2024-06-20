from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad


class Cipher:
    def __init__(self, key, iv, charset='utf-8'):
        if len(key) not in [16, 24, 32]:
            raise ValueError("Key must be 16, 24, or 32 bytes long")
        if len(iv) != 16:
            raise ValueError("IV must be 16 bytes long")
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC
        self.charset = charset

    def encrypt_message(self, message):
        cipher = AES.new(self.key, self.mode, self.iv)
        padded = pad(message, AES.block_size)
        return cipher.encrypt(padded)

    def decrypt_message(self, message):
        cipher = AES.new(self.key, self.mode, self.iv)
        decrypted = cipher.decrypt(message)
        unpadded = unpad(decrypted, AES.block_size)
        return unpadded.decode(self.charset)