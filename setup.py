# this file contains some placeholders
# that are changed in a local copy if a release is made

import setuptools

README = 'README.md'  # the path to your readme file
README_MIME = 'text/markdown'  # it's mime type

with open(README, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kato",
    version="1",
    author="ameasere",
    description="Rijndael-inspired Symmetric Encryption PoC",
    url="https://github.com/ameasere/kato",
    long_description=long_description,
    long_description_content_type=README_MIME,
    packages=setuptools.find_packages(),
    author_email="leigh@ameasere.com",
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent"
    ],
    install_requires=["pycryptodomex"
    ]
)
