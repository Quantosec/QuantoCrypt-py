#!python3

import hashlib

class MD5:
    def __init__(self, data = ""):
        self.data = data.encode("utf-8")

    def hex(self):
        """Returns hex representation of MD5 data.

        Returns:
            A string in hexadecimal format representing the MD5 data.

        """
        return hashlib.md5(self.data).hexdigest()

class SHA256:
    def __init__(self, data = ""):
        self.data = data.encode("utf-8")

    def hex(self):
        return hashlib.sha256(self.data).hexdigest()