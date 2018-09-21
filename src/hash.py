import hashlib

class SHA256:
    def __init__(self, data = ""):
        self.data = data.encode("utf-8")

    def hex(self):
        return hashlib.sha256(self.data).hexdigest()