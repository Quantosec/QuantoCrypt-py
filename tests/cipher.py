#!python3

import QuantoCrypt.cipher

data = input("Enter some data to encrypt/decrypt: ")
key = input("Enter the key to encrypt/decrypt with: ")
doEncrypt = (input("Encrypt the data? [Y/n]") != "n")

print("")

if doEncrypt:
    print(QuantoCrypt.cipher.AES(data, key).encrypt())
else:
    print(QuantoCrypt.cipher.AES(data, key).decrypt())