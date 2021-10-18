from random import choice
from string import ascii_uppercase

import pyaes

class MC:
    def __init__(self):
        self.k1 = ''.join(choice(ascii_uppercase) for i in range(16))
        self.k2 = ''.join(choice(ascii_uppercase) for i in range(16))
        self.k = "ANDREEAVINAMADAL"
    def getKKey(self):
        return self.k
    def get_k1_encryption(self):
        new_k = self.k.encode()
        new_k1 = self.k1.encode()
        aes = pyaes.AES(new_k)
        return aes.encrypt(new_k1)
    def get_k2_encryption(self):
        new_k = self.k.encode()
        new_k2 = self.k2.encode()
        aes = pyaes.AES(new_k)
        return aes.encrypt(new_k2)
