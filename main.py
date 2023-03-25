import os
import secrets
import pyaes

def generateKeyAES():
    random_key = os.urandom(16)
    return random_key

def generateCounterValue():
    iv = secrets.randbits(128)
    return iv
def aesEncryptionCtr(key, iv, file):
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(file)
    return ciphertext
def aesDecryptionCtr(key, iv, ciphertext):
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    plaintext = aes.decrypt(ciphertext)
    return plaintext

if __name__ == '__main__':
    with open('password.txt', 'rb') as file:
        originalFile = file.read()
    secretKey = generateKeyAES()
    nonceForCtr = generateCounterValue()
    print("Your random secret key for AES: " + str(secretKey))
    print("128 bit random counter value:" + str(nonceForCtr))
    ciphertext = aesEncryptionCtr(secretKey, nonceForCtr, originalFile)
    with open('encrypted.txt', 'wb') as file:
        file.write(ciphertext)
    plaintext = aesDecryptionCtr(secretKey, nonceForCtr, ciphertext)
    with open('decrypted.txt', 'wb') as file:
        file.write(plaintext)