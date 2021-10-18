import pyaes

def ECB_encryption(originalText,key):
    key = key.encode()
    aes = pyaes.AES(key)
    encrypted_text = []
    for i in range(0,len(originalText),16):
        block = originalText[i:i+16]
        block = block.encode()
        if(len(block)<16):
            for j in range(0,16-len(block)):
                block += b'\x00'
        encrypted_text +=  aes.encrypt(block)
    return encrypted_text

def ECB_decryption(encryptedText,key):
    decrypted_text = ''
    key = key.encode()
    aes = pyaes.AES(key)
    for i in range(0,len(encryptedText),16):
        block = encryptedText[i:i+16]
        decrypted_text +=  bytes(aes.decrypt(block)).decode()
    return decrypted_text
    