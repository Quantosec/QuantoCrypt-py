from setuptools import setup

setup(
    name = "QuantoCrypt",
    version = "0.1",
    description = "QuantoCrypt cryptography library for Python.",
    url = "https://github.com/Quantosec/QuantoCrypt-py",
    author = "Quantosec",
    author_email = "quantosec@gmail.com",
    license = "Quantosec Open-Source Licence",
    packages = ["QuantoCrypt"],
    zip_safe = False,
    install_requires = [
        "pycrypto>=2.6.1"
    ]
)