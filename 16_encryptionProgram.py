import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters  # we could use "0013894fjF,djk##" ouselves as well but we can use these string functinos for ease/ " " for a whitespace character

chars = list(chars)
key = chars.copy()


random.shuffle(key)

# print(f"chars: {chars}")
# print()
# print(f"Key: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
    
print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")