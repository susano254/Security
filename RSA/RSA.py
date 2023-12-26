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
	def pickRandomPrime():
		i = random.randint(0, len(RSA.primes) - 1)
		prime = RSA.primes[i]
		RSA.primes.remove(prime)
		return prime


	def generateKeys():
		p = RSA.pickRandomPrime() 
		q = RSA.pickRandomPrime() 

		n = p * q
		phi_n = (p - 1) * (q - 1)

		e = 2
		while True:
			if math.gcd(e, phi_n) == 1:
				break
			e += 1

		# d = (k*Φ(n) + 1) / e for some integer k
		public_key = e

		d = 2
		while True:
			if (d * e) % fi == 1:
				break
			d += 1

		private_key = d


	# To encrypt the given number
	def encrypt(message):
		global public_key, n
		e = public_key
		encrypted_text = 1
		while e > 0:
			encrypted_text *= message
			encrypted_text %= n
			e -= 1
		return encrypted_text


	# To decrypt the given number
	def decrypt(encrypted_text):
		global private_key, n
		d = private_key
		decrypted = 1
		while d > 0:
			decrypted *= encrypted_text
			decrypted %= n
			d -= 1
		return decrypted


	# First converting each character to its ASCII value and
	# then encoding it then decoding the number to get the
	# ASCII and converting it to character
	def encoder(message):
		encoded = []
		# Calling the encrypting function in encoding function
		for letter in message:
			encoded.append(encrypt(ord(letter)))
		return encoded


	def decoder(encoded):
		s = ''
		# Calling the decrypting function decoding function
		for num in encoded:
			s += chr(decrypt(num))
		return s


	if __name__ == '__main__':
		primefiller()
		setkeys()
		message = "Test Message"
		# Uncomment below for manual input
		# message = input("Enter the message\n")
		# Calling the encoding function
		coded = encoder(message)

		print("Initial message:")
		print(message)
		print("\n\nThe encoded message(encrypted by public key)\n")
		print(''.join(str(p) for p in coded))
		print("\n\nThe decoded message(decrypted by public key)\n")
		print(''.join(str(p) for p in decoder(coded)))