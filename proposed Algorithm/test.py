from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
passowd = b"A really secret message. Not for prying eyes."
cipher_text = cipher_suite.encrypt(passowd)
plain_text = cipher_suite.decrypt(cipher_text)
print(cipher_text)
print(plain_text)
