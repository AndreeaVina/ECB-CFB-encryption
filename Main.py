from MC import MC
from Node import Node
key_manager = MC()
A = Node
B = Node
if(A.ask_for_encryption_mode(A,key_manager) == 'ECB'):
    A.set_k1(A,key_manager.get_k1_encryption())
    B.setEncryptionMode(B,A.sendEncryptionMode(A))
    B.set_k1(B,key_manager.get_k1_encryption())
    A.k1_decryption()
    B.k1_decryption()
    A.sendOkMessage(B.sendOkMessage("we can start encryption!"))
else: 
    A.set_k2(A,key_manager.get_k2_encryption())
    B.setEncryptionMode(A.sendEncryptionMode(A))
    B.set_k2(B,key_manager.get_k2_encryption())
    A.k2_decryption(A)
    B.k2_decryption()
    B.sendOkMessage()
    A.sendOkMessage(B.sendOkMessage("we can start encryption!"))