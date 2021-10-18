import pyaes

class Node :
    def __init__(self):
         self.k = "ANDREEAVINAMADAL"
    #ask the user to choose between ECB encryption and CFB encryption
    def ask_for_encryption_mode(self,key_manager):
        self.mode = input("Enter desired encryption mode (ECB/CFB) : ")
        while self.mode != "ECB" and self.mode!="CFB":
            print("Try again! ")
            self.mode = input("Enter desired encryption mode (ECB/CFB) : ")
        return self.mode
    #send the encryption mode to node B
    def sendEncryptionMode(self):
        return self.mode
    #setter for encryption mode for node B
    def setEncryptionMode(self,mode):
        self.mode = mode
    #setters for K1, K2, K recived from the key manager
    def set_K_key(self,k):
        self.k = k
    def set_k1(self,k1):
        self.k1 = k1
    def set_k2(self,k2):
        self.k2 = k2
    #decryption for Key k1 with k key
    def k1_decryption(self):
        new_k = self.k.encode()
        aes = pyaes.AES(new_k)
        self.k1 = bytes(aes.decrypt(self.k1)).decode()
    #decryption for Key k2 with k key
    def k2_decryption(self):
        new_k = self.k.encode()
        aes = pyaes.AES(new_k)
        self.k2 = bytes(aes.decrypt(self.k2)).decode()
    

    def sendOkMessage(message):
        return message
    def setOkMessage(self,message):
        self.message = message
