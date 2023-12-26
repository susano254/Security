from AES.AES import AES
from Helper import Helper
import binascii

plain_text = "ABCDEFGHABCDEFGH"
key_str = "12345678abcdefgh"



cipher = AES.encrypt(plain_text, key_str)
print(cipher)
plain_text = AES.decrypt(cipher, key_str)
print(plain_text)
