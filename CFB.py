import pyaes
IV = "AHJ DHS3465782^$".encode()
encrypted_text = []
decrypted_text = ""
block_cipher_encryption = []

def CFB_encryption(originalText,key):
    global encrypted_text
    global block_cipher_encryption
    key = key.encode()
    aes = pyaes.AES(key)
    for i in range(0,len(originalText),16):
        block = originalText[i:i+16]
        block = block.encode()
        if(i == 0):
            block_cipher_encryption = aes.encrypt(IV)
        else : 
            block_cipher_encryption  = aes.encrypt(block_cipher_encryption)
        if(len(block)<16):
            for j in range(0,16-len(block)):
                block += b'\x00'
        block_cipher_encryption = [x ^ y for (x, y) in zip(block_cipher_encryption,block)]
        encrypted_text += block_cipher_encryption
    return encrypted_text

def CFB_decryption(encryptedText,key):
    global decrypted_text
    global block_cipher_encryption
    key = key.encode()
    aes = pyaes.AES(key)
    for i in range(0,len(encryptedText),16):
        block = encryptedText[i:i+16]
        if(i == 0):
            block_cipher_encryption = aes.encrypt(IV)
        else : 
            block_cipher_encryption = aes.encrypt(encryptedText[i-16:i])
        decrypted_text += bytes([x ^ y for (x, y) in zip(block_cipher_encryption,block)]).decode()
    return decrypted_text