class Helper:

	@staticmethod
	def xor(left, right):

		if len(left) != len(right):
			raise Exception("both parameters must be of same length")

		result = ""
		for i in range(len(left)):
			if left[i] == right[i]:
				result += '0'
			else:
				result += '1'
		return result

	@staticmethod
	def rotate_left(binary, n):
		# just to make sure n is less than bin length
		n = n % len(binary)

		return binary[n:] + binary[:n]

	@staticmethod
	def str_to_binary(str):
		binary_list = []

		for char in str:
			binary_list.append(bin(ord(char))[2:].zfill(8))
         
		return ''.join(binary_list)
	
	@staticmethod
	def decimal_to_binary(decimal, fill=8):
		return bin(decimal)[2:].zfill(fill)

	@staticmethod
	def decimals_to_binary(decimals, fill=8):
		for i, decimal in enumerate(decimals):
			decimals[i] = Helper.decimal_to_binary(decimal)

		return decimals

	@staticmethod
	def binaries_to_decimals(binaries):
		decimals = []
		for binary in binaries:
			decimals.append(int(binary, 2))

		return decimals

	@staticmethod
	def hex_to_binary(hex_string):
		binary_string = ''.join(format(int(hex_char, 16), '04b') for hex_char in hex_string)
		return binary_string
	
	@staticmethod
	def binary_to_hex(binary_string, fill=None):
		if fill is not None:
			hex_representation = hex(int(binary_string, 2))[2:].zfill(fill)
		else:
			hex_representation = hex(int(binary_string, 2))[2:]
		return hex_representation



	@staticmethod
	def permute(data, permute_table, n):
		permutation = ""
		for i in range(0, n):
			permutation = permutation + data[permute_table[i] - 1]
		return permutation


	@staticmethod
	def divide_into_blocks(binary_str, block_size):
		# check if the length is divisible by the block size
		if len(binary_str) % block_size != 0:
			# calculate the number of bits needed for padding
			padding_bits = (block_size - len(binary_str) % block_size) % block_size

			# pad the binary string with 1s
			binary_str = binary_str + '1' * padding_bits

		blocks = [binary_str[i:i+block_size] for i in range(0, len(binary_str), block_size)]

		return blocks

	@staticmethod
	def join_bytes_to_word(bytes):
		# Assuming bytes[0] is the least significant byte
		word = 0
		for i in range(4):
			word |= bytes[i] << (i * 8)
		return word


