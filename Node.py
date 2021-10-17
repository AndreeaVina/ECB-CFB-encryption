class Node :
        
    def ask_for_encryption_mode(self,key_manager):
        self.mode = input("Enter desired encryption mode (ECB/CFB) : ")
        while self.mode != "ECB" and self.mode!="CFB":
            print("Try again! ")
            self.mode = input("Enter desired encryption mode (ECB/CFB) : ")
        return self.mode
    def set_K_key(self,k):
        self.k = k
    def set_k1(self,k1):
        self.k1 = k1
    def set_k2(self,k2):
        self.k2 = k2