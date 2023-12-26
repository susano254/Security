from AES.SBOX import SBOX
from Helper import Helper

class Key:

	RC = [
		0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
		0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
		0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
		0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
	]

	def __init__(self, key):
		self.expanded_key = []
		word_groups = []
		words = Helper.divide_into_blocks(key, 8)
		for i in range(0, len(words), 4):
			group = [int(word, 2) for word in words[i:i+4]]
			word_groups.append(group)

		words = word_groups

		self.expanded_key.append(words)
		
		for i in range(1, 11):
			self.expanded_key.append([0] * 4)  # Initialize sublist for each round
			self.expand_round_key(i)

	def expand_round_key(self, i):
		prev_row_key = self.expanded_key[i-1][0]
		g_value = self.g(self.expanded_key[i-1][-1], i)
		self.expanded_key[i][0] = [prev_row_key[i] ^ g_value[i] for i in range(4)]
		for j in range(1, 4):
			prev_column_key = self.expanded_key[i][j-1]
			prev_row_key = self.expanded_key[i-1][j]
			self.expanded_key[i][j] = [prev_column_key[i] ^ prev_row_key[i] for i in range(4)]



	def g(self, word, i):
		# divide the word into 4 bytes
		bytes = word

		# rotate by one byte
		bytes =  bytes[1:] + bytes[:1]
		# sub word using s box for each byte
		bytes = [SBOX.run_one_block(byte) for byte in bytes]
		bytes[0] ^= self.RC[i]
		return bytes

	def extract_key_i_grid(self, i):
		words = self.expanded_key[i]
		
		matrix = [
			[words[0][0], words[1][0], words[2][0], words[3][0]],
			[words[0][1], words[1][1], words[2][1], words[3][1]],
			[words[0][2], words[1][2], words[2][2], words[3][2]],
			[words[0][3], words[1][3], words[2][3], words[3][3]]
		]           
		return matrix
              
	             
	def printData(self):
		for i in range(len(self.expanded_key)):
			print("key grid ",i, ": ", self.extract_key_i_grid(i))