from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import random
import string
import os

class Cryptography:
	@staticmethod
	def __random_string():
	    letters = string.ascii_letters
	    result_str = ''.join(random.choice(letters) for i in range(23))
	    return result_str

	def __init__(self, password):
		password = password.encode()
		salt = b';,\xea\x9e\xaf\x13\x9f\xbb\xb9\xc6y\x89Y\r\x8a\x81'
		kdf = PBKDF2HMAC( algorithm=hashes.SHA256(), length=32, salt=salt, iterations=480000, )
		self.key = base64.urlsafe_b64encode(kdf.derive(password))
		self.fernet = Fernet(self.key)
	def encrypt(self, text):
		return self.fernet.encrypt(text.encode()).decode()
	def decrypt(self, text):
		try:
			return self.fernet.decrypt(text.encode()).decode()
		except:
			return Cryptography.__random_string() #podane haslo bylo zle

class Reverse:
	def __init__(self):
		pass
	def encrypt(self, text):
		return text[::-1]
	def decrypt(self, text):
		return text[::-1]

class Encription():
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


#done: szyfrowanie dziala
#todo: zrobic interfejs