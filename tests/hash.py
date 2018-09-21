#!python3
import QuantoCrypt.hash

data = input("Enter some data to hash: ")

print("MD5:     " + QuantoCrypt.hash.MD5(data).hex())
print("SHA256:  " + QuantoCrypt.hash.SHA256(data).hex())