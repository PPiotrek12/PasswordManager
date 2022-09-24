from Cryptography import Cryptography

class Encryption():
	def __init__(self, key1, key2):
		self.__cryptography1 = Cryptography(key1)
		self.__cryptography2 = Cryptography(key2)

	def encrypt(self, text):
		cryptography1_text = self.__cryptography1.encrypt(text)
		cryptography2_text = self.__cryptography2.encrypt(cryptography1_text)
		#...
		return cryptography2_text

	def decrypt(self, text):
		#...
		cryptography2_text = self.__cryptography2.decrypt(text)
		cryptography_text = self.__cryptography1.decrypt(cryptography2_text)
		return cryptography_text
