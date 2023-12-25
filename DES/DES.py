from Helper import Helper
from DES.DES_Key import DES_Key
from DES.SBOX import SBOX
import copy

class DES:
	initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
							60, 52, 44, 36, 28, 20, 12, 4,
							62, 54, 46, 38, 30, 22, 14, 6,
							64, 56, 48, 40, 32, 24, 16, 8,
							57, 49, 41, 33, 25, 17, 9, 1,
							59, 51, 43, 35, 27, 19, 11, 3,
							61, 53, 45, 37, 29, 21, 13, 5,
							63, 55, 47, 39, 31, 23, 15, 7]
	
	f_expansion = [32, 1, 2, 3, 4, 5, 4, 5,
					6, 7, 8, 9, 8, 9, 10, 11,
					12, 13, 12, 13, 14, 15, 16, 17,
					16, 17, 18, 19, 20, 21, 20, 21,
					22, 23, 24, 25, 24, 25, 26, 27,
					28, 29, 28, 29, 30, 31, 32, 1]
	
	f_permutation = [16,  7, 20, 21,
					29, 12, 28, 17,
					1, 15, 23, 26,
					5, 18, 31, 10,
					2,  8, 24, 14,
					32, 27,  3,  9,
					19, 13, 30,  6,
					22, 11,  4, 25]
	
	final_permutation = [40, 8, 48, 16, 56, 24, 64, 32,
						39, 7, 47, 15, 55, 23, 63, 31,
						38, 6, 46, 14, 54, 22, 62, 30,
						37, 5, 45, 13, 53, 21, 61, 29,
						36, 4, 44, 12, 52, 20, 60, 28,
						35, 3, 43, 11, 51, 19, 59, 27,
						34, 2, 42, 10, 50, 18, 58, 26,
						33, 1, 41, 9, 49, 17, 57, 25]

	@staticmethod
	def f_function(right_half, key_i):
		#1: expand right_half from 32-bit to 48bit using expansion_d
		right_expanded = Helper.permute(right_half, DES.f_expansion, 48)
		#2: xor the epansion with key_i
		result = Helper.xor(right_expanded, key_i)

		result_blocks = Helper.divide_into_blocks(result, 6)

		result = SBOX.run(result_blocks)

		result = Helper.permute(result, DES.f_permutation, 32)
		
		return result
	

	@staticmethod
	def encrypt(plain_text_str, key, hexa=True):
		plain_text_blocks = Helper.divide_into_blocks(plain_text_str, 64)
		result_str = ""
		for plain_text in plain_text_blocks:
			while len(plain_text) < 64:
				plain_text += "11111111"
			#1: initial permuation on plain text
			plain_text = Helper.permute(plain_text, DES.initial_permutation, 64)
			left_half = plain_text[:32]
			right_half = plain_text[32:]
			for i in range(16):
				#2: temp = f_function result xor with left_half
				temp = DES.f_function(right_half, key.keyList[i])
				temp = Helper.xor(left_half, temp)

				left_half = right_half
				right_half = temp
				print(Helper.binary_to_hex(left_half), " ", Helper.binary_to_hex(right_half), " ", Helper.binary_to_hex(key.keyList[i], fill=12))

			#5: result = final permutation(L16, R16)
			result = right_half + left_half
			result = Helper.permute(result, DES.final_permutation, 64)

			results = Helper.divide_into_blocks(result, 8)

			if hexa:
				result = ""
				for c in results:
					result += hex(int(c, 2))[2:].zfill(2)
			else:
				result = ""
				for c in results:
					result += chr(int(c, 2))
			
			result_str += result

		#6: return result
		return result_str
 
	@staticmethod
	def decrypt(cipher_text, key):
		key2 = copy.deepcopy(key)
		key2.keyList.reverse()
		cipher_text = Helper.hex_to_binary(cipher_text)
		result = DES.encrypt(cipher_text, key2, False)
		# remove the special char that you added
		result = result.replace(chr(255), '')
		return result
