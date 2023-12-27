import random
import math

class RSA:
	primes = []

	public_key = None
	private_key = None
	n = None


	@staticmethod
	def sieveOfEratosthenes(size = 1000):
		primesOrNot = [False, False] + [True] * (size - 2)

		# starting from 2 
		for i in range(2, size):
			for j in range(i ** 2, size, i):
				primesOrNot[j] = False

		# fill the found prime number in a new array
		for i in range(size):
			if primesOrNot[i]:
				RSA.primes.append(i)


	@staticmethod
	def choosePrime():
		i = random.randint(0, len(RSA.primes) - 1)
		prime = RSA.primes[i]
		RSA.primes.remove(prime)
		return prime


	@staticmethod
	def choose_e(phi_n):
		e = 2
		while True:
			if math.gcd(e, phi_n) == 1:
				return e
			e += 1


	@staticmethod
	def calculate_d(phi_n, e):
		d = 2
		while True:
			if (d * e) % phi_n == 1:
				break
			d += 1


	def generateKeys():
		p = RSA.choosePrime() 
		q = RSA.choosePrime() 

		RSA.n = p * q
		phi_n = (p - 1) * (q - 1)


		RSA.public_key = RSA.choose_e(phi_n)


		RSA.private_key = RSA.calculate_d(phi_n, RSA.public_key)


	# To encrypt the given number
	def encrypt(message):
		e = RSA.public_key

		# X^e mod n 
		encrypted_text = 1
		while e > 0:
			encrypted_text *= message
			encrypted_text %= RSA.n
			e -= 1

		return encrypted_text


	# To decrypt the given number
	def decrypt(encrypted_text):
		d = RSA.private_key

		# y^d mod n 
		decrypted = 1
		while d > 0:
			decrypted *= encrypted_text
			decrypted %= RSA.n
			d -= 1

		return decrypted


	def encoder(message):
		encoded = []
		for letter in message:
			decimal_val = ord(letter)
			cipher_letter = RSA.encrypt(decimal_val)
			encoded.append(cipher_letter)
		return encoded


	def decoder(cipher):
		stream = ''

		for cipher_letter in cipher:
			decimal_val = RSA.decrypt(cipher_letter)
			stream += chr(decimal_val)
		return stream 


	# if __name__ == '__main__':
	# 	primefiller()
	# 	setkeys()
	# 	message = "Test Message"
	# 	# Uncomment below for manual input
	# 	# message = input("Enter the message\n")
	# 	# Calling the encoding function
	# 	coded = encoder(message)

	# 	print("Initial message:")
	# 	print(message)
	# 	print("\n\nThe encoded message(encrypted by public key)\n")
	# 	print(''.join(str(p) for p in coded))
	# 	print("\n\nThe decoded message(decrypted by public key)\n")
	# 	print(''.join(str(p) for p in decoder(coded)))