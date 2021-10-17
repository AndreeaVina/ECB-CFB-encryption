from MC import MC
from Node import Node
key_manager = MC()
A = Node
B = Node
A.set_K_key(A,key_manager.getKKey())
B.set_K_key(B,key_manager.getKKey())
if(A.ask_for_encryption_mode(A) == 'ECB'):
    A.set_k1(A,key_manager.get_k1_encryption())
    B.set_k1(B,key_manager.get_k1_encryption())
else: 
    A.set_k1(A,key_manager.get_k2_encryption())
    B.set_k1(B,key_manager.get_k2_encryption())