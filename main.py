from DES.DES import DES
from Helper import Helper
from DES.DES_Key import DES_Key

# plain_text = "123456ABCD132536"
# key_str = "AABB09182736CCDD"
# plain_text = Helper.hex_to_binary(plain_text)
# key_str = Helper.hex_to_binary(key_str)


# plain_text = "ABCDEF"
# key_str = "12345678"


plain_text = input("Enter plain text: ")
key_str = input("Enter 8 key characters: ")

plain_text = Helper.str_to_binary(plain_text)
key_str = Helper.str_to_binary(key_str)


cipher_text = DES.encrypt(plain_text, DES_Key(key_str))
print(cipher_text)
plain_text = DES.decrypt(cipher_text, DES_Key(key_str))
print(plain_text)