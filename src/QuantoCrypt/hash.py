#!python3

import hashlib

class MD5:
    def __init__(self, data = ""):
        self.data = data
    
    def raw(self):
        """Returns raw representation of MD5 data.

        Returns:
            A 128-bit string in raw format representing the MD5 data.
        """

        return hashlib.md5(self.data.encode("utf-8")).digest()

    def hex(self):
        """Returns hex representation of MD5 data.

        Returns:
            A 32-byte string in hexadecimal format representing the MD5 data.
        """

        return hashlib.md5(self.data.encode("utf-8")).hexdigest()

class SHA1:
    def __init__(self, data = ""):
        self.data = data
    
    def raw(self):
        """Returns raw representation of SHA1 data.

        Returns:
            A 160-bit string in raw format representing the SHA1 data.
        """

        return hashlib.sha1(self.data.encode("utf-8")).digest()

    def hex(self):
        """Returns hex representation of SHA1 data.

        Returns:
            A 40-byte string in hexadecimal format representing the SHA1 data.
        """

        return hashlib.sha1(self.data.encode("utf-8")).hexdigest()

class SHA224:
    def __init__(self, data = ""):
        self.data = data
    
    def raw(self):
        """Returns raw representation of SHA512 data.

        Returns:
            A 224-bit string in raw format representing the SHA224 data.
        """

        return hashlib.sha224(self.data.encode("utf-8")).digest()

    def hex(self):
        """Returns hex representation of SHA224 data.

        Returns:
            A 56-byte string in hexadecimal format representing the SHA224
            data.
        """

        return hashlib.sha224(self.data.encode("utf-8")).hexdigest()

class SHA256:
    def __init__(self, data = ""):
        self.data = data
    
    def raw(self):
        """Returns raw representation of SHA256 data.

        Returns:
            A 256-bit string in raw format representing the SHA256 data.
        """

        return hashlib.sha256(self.data.encode("utf-8")).digest()

    def hex(self):
        """Returns hex representation of SHA256 data.

        Returns:
            A 64-byte string in hexadecimal format representing the SHA256
            data.
        """

        return hashlib.sha256(self.data.encode("utf-8")).hexdigest()

class SHA384:
    def __init__(self, data = ""):
        self.data = data
    
    def raw(self):
        """Returns raw representation of SHA384 data.

        Returns:
            A 384-bit string in raw format representing the SHA384 data.
        """

        return hashlib.sha384(self.data.encode("utf-8")).digest()

    def hex(self):
        """Returns hex representation of SHA384 data.

        Returns:
            A 96-byte string in hexadecimal format representing the SHA384
            data.
        """

        return hashlib.sha384(self.data.encode("utf-8")).hexdigest()

class SHA512:
    def __init__(self, data = ""):
        self.data = data
    
    def raw(self):
        """Returns raw representation of SHA512 data.

        Returns:
            A 512-bit string in raw format representing the SHA512 data.
        """

        return hashlib.sha512(self.data.encode("utf-8")).digest()

    def hex(self):
        """Returns hex representation of SHA512 data.

        Returns:
            A 128-byte string in hexadecimal format representing the SHA512
            data.
        """

        return hashlib.sha512(self.data.encode("utf-8")).hexdigest()