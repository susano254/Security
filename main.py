from AES.AES import AES
from Helper import Helper
from RSA.RSA import RSA

plain_text = "ABCDEFGHABCDEFGH IJK"
key_str = "12345678abcdefgh"

encryptor = RSA()
cipher = encryptor.encoder(plain_text)
print(cipher)
plain_text = encryptor.decoder(cipher)
print(plain_text)


cipher = AES.encrypt(plain_text, key_str)
print(cipher)
plain_text = AES.decrypt(cipher, key_str)
print(plain_text)
