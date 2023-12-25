from Helper import Helper
from AES.SBOX import SBOX
from AES.AES import AES

plain_text = "ABCDEF"
key_str = "12345678abcdefgh"

# plain_text = input("Enter plain text: ")
# key_str = input("Enter 8 key characters: ")

plain_text = Helper.str_to_binary(plain_text)
key_str = Helper.str_to_binary(key_str)


B = SBOX.run(Helper.divide_into_blocks(key_str, 8))
matrix = AES.constructMatrix(B)
matrix = AES.shiftRows(matrix)
matrix = AES.mixColumns(matrix)

# cipher_text = DES.encrypt(plain_text, DES_Key(key_str))
# print(cipher_text)
# plain_text = DES.decrypt(cipher_text, DES_Key(key_str))
# print(plain_text)