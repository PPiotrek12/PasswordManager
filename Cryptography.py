from imports import *

class Cryptography:
	@staticmethod
	def __random_string():
	    letters = string.ascii_letters
	    result_str = ''.join(random.choice(letters) for i in range(23))
	    return result_str

	def __init__(self, password):
		password = password.encode()
		print(dir(strings))
		return
		salt = strings.cryptography_salt.encode()
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
