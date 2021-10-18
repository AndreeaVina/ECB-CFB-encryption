from MC import MC
from Node import Node
key_manager = MC()
A = Node()
B = Node()
if(A.ask_for_encryption_mode(key_manager) == 'ECB'):
    A.set_k1(key_manager.get_k1_encryption())
    B.setEncryptionMode(A.sendEncryptionMode())
    B.set_k1(key_manager.get_k1_encryption())
    A.k1_decryption()
    B.k1_decryption()
    A.setOkMessage(B.sendOkMessage("we can start encryption!"),B)
else: 
    A.set_k2(key_manager.get_k2_encryption())
    B.setEncryptionMode(A.sendEncryptionMode())
    B.set_k2(key_manager.get_k2_encryption())
    A.k2_decryption()
    B.k2_decryption()
    A.setOkMessage(B.sendOkMessage("we can start encryption!"),B)