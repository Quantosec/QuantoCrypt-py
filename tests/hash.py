#!python3

import QuantoCrypt.hash

data = input("Enter some data to hash: ")

print("")

print("Hex hashes:")
print("MD5:     " + QuantoCrypt.hash.MD5(data).hex())
print("SHA1:    " + QuantoCrypt.hash.SHA1(data).hex())
print("SHA224   " + QuantoCrypt.hash.SHA224(data).hex())
print("SHA256:  " + QuantoCrypt.hash.SHA256(data).hex())
print("SHA384:  " + QuantoCrypt.hash.SHA384(data).hex())
print("SHA512:  " + QuantoCrypt.hash.SHA512(data).hex())

print("")

print("Byte length of hex hashes:")
print("MD5:     " + str(len(QuantoCrypt.hash.MD5(data).hex())))
print("SHA1:    " + str(len(QuantoCrypt.hash.SHA1(data).hex())))
print("SHA224   " + str(len(QuantoCrypt.hash.SHA224(data).hex())))
print("SHA256:  " + str(len(QuantoCrypt.hash.SHA256(data).hex())))
print("SHA384:  " + str(len(QuantoCrypt.hash.SHA384(data).hex())))
print("SHA512:  " + str(len(QuantoCrypt.hash.SHA512(data).hex())))

print("")

print("Stringified raw hashes:")
print("MD5:     " + str(QuantoCrypt.hash.MD5(data).raw()))
print("SHA1:    " + str(QuantoCrypt.hash.SHA1(data).raw()))
print("SHA224   " + str(QuantoCrypt.hash.SHA224(data).raw()))
print("SHA256:  " + str(QuantoCrypt.hash.SHA256(data).raw()))
print("SHA384:  " + str(QuantoCrypt.hash.SHA384(data).raw()))
print("SHA512:  " + str(QuantoCrypt.hash.SHA512(data).raw()))

print("")

print("Byte length of raw hashes:")
print("MD5:     " + str(len(QuantoCrypt.hash.MD5(data).raw())))
print("SHA1:    " + str(len(QuantoCrypt.hash.SHA1(data).raw())))
print("SHA224   " + str(len(QuantoCrypt.hash.SHA224(data).raw())))
print("SHA256:  " + str(len(QuantoCrypt.hash.SHA256(data).raw())))
print("SHA384:  " + str(len(QuantoCrypt.hash.SHA384(data).raw())))
print("SHA512:  " + str(len(QuantoCrypt.hash.SHA512(data).raw())))

print("")

print("Bit length of raw hashes:")
print("MD5:     " + str(len(QuantoCrypt.hash.MD5(data).raw()) * 8))
print("SHA1:    " + str(len(QuantoCrypt.hash.SHA1(data).raw()) * 8))
print("SHA224   " + str(len(QuantoCrypt.hash.SHA224(data).raw()) * 8))
print("SHA256:  " + str(len(QuantoCrypt.hash.SHA256(data).raw()) * 8))
print("SHA384:  " + str(len(QuantoCrypt.hash.SHA384(data).raw()) * 8))
print("SHA512:  " + str(len(QuantoCrypt.hash.SHA512(data).raw()) * 8))