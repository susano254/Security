from Helper import Helper

class Key:
	PC_1 = [57, 49, 41, 33, 25, 17, 9,
			1, 58, 50, 42, 34, 26, 18,
			10, 2, 59, 51, 43, 35, 27,
			19, 11, 3, 60, 52, 44, 36,
			63, 55, 47, 39, 31, 23, 15,
			7, 62, 54, 46, 38, 30, 22,
			14, 6, 61, 53, 45, 37, 29,
			21, 13, 5, 28, 20, 12, 4]

	PC_2 = [14, 17, 11, 24, 1, 5,
			3, 28, 15, 6, 21, 10,
			23, 19, 12, 4, 26, 8,
			16, 7, 27, 20, 13, 2,
			41, 52, 31, 37, 47, 55,
			30, 40, 51, 45, 33, 48,
			44, 49, 39, 56, 34, 53,
			46, 42, 50, 36, 29, 32]

	shift_table = [1, 1, 2, 2,
				2, 2, 2, 2,
				1, 2, 2, 2,
				2, 2, 2, 1]

	def __init__(self, key):
		self.keyList = []
		self.init_key = key

		self.key = Helper.permute(self.init_key, self.PC_1, 56)
		self.Ci = self.key[:28]
		self.Di = self.key[28:]

		for i in range(16):
			self.Ci = Helper.rotate_left(self.Ci, self.shift_table[i])
			self.Di = Helper.rotate_left(self.Di, self.shift_table[i])

			self.key = self.Ci + self.Di

			self.keyList.append(Helper.permute(self.key, self.PC_2, 48))