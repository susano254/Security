from DES import DES
from Helper import Helper
from Key import Key

plain_text = "ABCDEF"
key_str = "12345678"

plain_text = Helper.str_to_binary(plain_text)
key_str = Helper.str_to_binary(key_str)

# plain_text = "123456ABCD132536"
# key_str = "AABB09182736CCDD"
# plain_text = Helper.hex_to_binary(plain_text)
# key_str = Helper.hex_to_binary(key_str)

key = Key(key_str)



cipher_text = DES.encrypt(plain_text, key)
print(cipher_text)
plain_text = DES.decrypt(cipher_text, key)
print(plain_text)