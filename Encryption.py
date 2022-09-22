from imports import *

class Encryption():
	def __init__(self, cryptography_password):
		self.cryptography = Cryptography(cryptography_password)
		self.reverse = Reverse()

	def encrypt(self, text):
		cryptography_text = self.cryptography.encrypt(text)
		reverse_text = self.reverse.encrypt(cryptography_text)
		#...
		return reverse_text

	def decrypt(self, text):
		#...
		reverse_text = self.reverse.decrypt(text)
		cryptography_text = self.cryptography.decrypt(reverse_text)
		return cryptography_text
