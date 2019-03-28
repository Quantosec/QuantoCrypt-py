#!python3

import base64
import hashlib
from Crypto import Random
import Crypto.Cipher

class AES:
    def __init__(self, data = "", key = "", keyLength = 32):
        """Initialises AES cipher class.

        Args:
            data: Data to encrypt or decrypt.
            key: Key to encrypt or decrypt data with.
            keyLength: Generally excluded, the maximum length of the key when
                padding.

        """

        self.data = data
        self.key = key
        self.keyLength = keyLength

    def _pad(self, string):
        """Pads the key in the string.

        Args:
            string: String to be padded.

        """

        return string + (self.keyLength - len(string) % self.keyLength) * chr(self.keyLength - len(string) % self.keyLength)
    
    def _unpad(self, string):
        """Unpads the key in the string.

        Args:
            string: String to be unpadded.

        """

        return string[:-ord(string[len(string) - 1:])]
    
    def encrypt(self):
        """Encrypts the data with the key in the cipher.

        Returns:
            The encrypted data, in base64 format.

        """

        data = self._pad(self.data)
        iv = Random.new().read(Crypto.Cipher.AES.block_size)
        cipher = Crypto.Cipher.AES.new(hashlib.sha256(self.key.encode("utf-8")).digest(), Crypto.Cipher.AES.MODE_CBC, iv)

        return base64.b64encode(iv + cipher.encrypt(data)).decode()
    
    def decrypt(self):
        """Decrypts the data with the key in the cipher.

        Returns:
            The decrypted data, in plaintext.

        """

        data = base64.b64decode(self.data)
        iv = data[:Crypto.Cipher.AES.block_size]
        cipher = Crypto.Cipher.AES.new(hashlib.sha256(self.key.encode("utf-8")).digest(), Crypto.Cipher.AES.MODE_CBC, iv)

        return self._unpad(cipher.decrypt(data[Crypto.Cipher.AES.block_size:])).decode()