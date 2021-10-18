import pyaes
from CFB import CFB_decryption, CFB_encryption
from ECB import ECB_decryption, ECB_encryption

class Node :
    def __init__(self):
        self.k = "ANDREEAVINAMADAL"
        self.ciphertext = []
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
    
    def getCriptoText(self,cipherText):
        self.ciphertext += cipherText

    def startDecryptionECB(self):
        initialMessage = ECB_decryption(self.ciphertext,self.k1)
        print(initialMessage)
    
    def startDecryptionCFB(self):
        initialMessage = CFB_decryption(self.ciphertext,self.k2)
        print(initialMessage)

    def sendOkMessage(self,message):
        return message

    def setOkMessage(self,message,B):
        self.message = message
        if(self.message == "we can start encryption!"):
            if(self.mode=="ECB"):
                f = open("file.txt", "r")
                originalText = f.read()
                self.ciphertext = ECB_encryption(originalText,self.k1)
                for i in range(0,len(self.ciphertext),16):
                    B.getCriptoText(self.ciphertext[i:i+16])
                B.startDecryptionECB()
            else:
                f = open("file.txt", "r")
                originalText = f.read()
                self.ciphertext = CFB_encryption(originalText,self.k2)
                for i in range(0,len(self.ciphertext),16):
                    B.getCriptoText(self.ciphertext[i:i+16])
                B.startDecryptionCFB()
