import base64
import hashlib
from Crypto.Cipher import AES
# we will take a key and will generate a key 
class AES256:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
        self.iv = b'\xc6Dv0F\x94\x13\xcdJ@\xf9\xfcI\x18T\x06'


    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padding_length = 16 - (len(data) % 16) 
        data += chr(padding_length) * padding_length
        ciphertext= cipher.encrypt(data.encode())
        return base64.b64encode(self.iv + ciphertext)
    

    def decrypt(self, ciphertext):
        ciphertext=base64.b64decode(ciphertext)
        iv=ciphertext[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext= cipher.decrypt(ciphertext[16:]).decode()
        padding_length=ord(plaintext[-1])
        return plaintext[:-padding_length]


