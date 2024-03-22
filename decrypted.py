import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypted.py" or file == "secret_key.key" or file == "decrypted.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("secret_key.key", "rb") as key_file:
    secret_key = key_file.read()
passphare = "Cyb3rT3$!"
user_password = input("Enter your password to decrypt your files: ")
if user_password == passphare:
    for file in files:
        with open(file, "rb") as file_decrypted:
            content = file_decrypted.read()
        content_decrypt = Fernet(secret_key).decrypt(content)
        with open(file, "wb") as file_decrypted:
            file_decrypted.write(content_decrypt)
        print("You recovered all your files")
else:
    print("Enter the right password to recover your files")
