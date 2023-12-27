import random
import math

class RSA:

	def  __init__(self):
		self.primes = []

		self.public_key = None
		self.private_key = None
		self.n = None

		self.sieveOfEratosthenes()
		self.generateKeys()


	def sieveOfEratosthenes(self, size = 1000):
		primesOrNot = [False, False] + [True] * (size - 2)

		# starting from 2 
		for i in range(2, size):
			for j in range(i ** 2, size, i):
				primesOrNot[j] = False

		# fill the found prime number in a new array
		for i in range(size):
			if primesOrNot[i]:
				self.primes.append(i)


	def choosePrime(self):
		i = random.randint(0, len(self.primes) - 1)
		prime = self.primes[i]
		self.primes.remove(prime)
		return prime


	def choose_e(self, phi_n):
		e = 2
		while True:
			if math.gcd(e, phi_n) == 1:
				return e
			e += 1


	def calculate_d(self, phi_n, e):
		d = 2
		while True:
			if (d * e) % phi_n == 1:
				return d
			d += 1


	def generateKeys(self):
		p = self.choosePrime() 
		q = self.choosePrime() 

		self.n = p * q
		phi_n = (p - 1) * (q - 1)


		self.public_key = self.choose_e(phi_n)


		self.private_key = self.calculate_d(phi_n, self.public_key)


	# To encrypt the given number
	def encrypt(self, message):
		e = self.public_key

		# X^e mod n 
		encrypted_text = 1
		while e > 0:
			encrypted_text *= message
			encrypted_text %= self.n
			e -= 1

		return encrypted_text


	# To decrypt the given number
	def decrypt(self, encrypted_text):
		d = self.private_key

		# y^d mod n 
		decrypted = 1
		while d > 0:
			decrypted *= encrypted_text
			decrypted %= self.n
			d -= 1

		return decrypted


	def encoder(self, message):
		encoded = []
		for letter in message:
			decimal_val = ord(letter)
			cipher_letter = self.encrypt(decimal_val)
			encoded.append(cipher_letter)
		return encoded


	def decoder(self, cipher):
		stream = ''

		for cipher_letter in cipher:
			decimal_val = self.decrypt(cipher_letter)
			stream += chr(decimal_val)
		return stream 
