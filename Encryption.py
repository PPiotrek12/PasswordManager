from Cryptography import Cryptography
from Reverse import Reverse

class Encryption():
	def __init__(self, cryptography_password):
		self.__cryptography = Cryptography(cryptography_password)
		self.__reverse = Reverse()

	def encrypt(self, text):
		cryptography_text = self.__cryptography.encrypt(text)
		reverse_text = self.__reverse.encrypt(cryptography_text)
		#...
		return reverse_text

	def decrypt(self, text):
		#...
		reverse_text = self.__reverse.decrypt(text)
		cryptography_text = self.__cryptography.decrypt(reverse_text)
		return cryptography_text
