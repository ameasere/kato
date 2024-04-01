import random


def generate_key():
    """
    Generates a random encryption key for Group Encryption (GRP).

    Returns:
    dict: A dictionary representing the encryption key.
    """
    key = {}
    chars = list(range(256))
    random.shuffle(chars)
    for i in range(256):
        key[i] = chars[i]
    return key


def encrypt_grp(plaintext, key):
    """
    Encrypts plaintext using Group Encryption (GRP) algorithm.

    Parameters:
    plaintext (str): The plaintext to be encrypted.
    key (dict): The encryption key.

    Returns:
    str: The encrypted ciphertext.
    """
    ciphertext = ""
    for char in plaintext:
        encrypted_char = key[ord(char)]
        ciphertext += chr(encrypted_char)
    return ciphertext


def decrypt_grp(ciphertext, key):
    """
    Decrypts ciphertext encrypted using Group Encryption (GRP) algorithm.

    Parameters:
    ciphertext (str): The ciphertext to be decrypted.
    key (dict): The encryption key.

    Returns:
    str: The decrypted plaintext.
    """
    plaintext = ""
    for char in ciphertext:
        decrypted_char = chr(list(key.keys())[list(key.values()).index(ord(char))])
        plaintext += decrypted_char
    return plaintext


def encrypt_ddr(plaintext, key):
    """
    Encrypts plaintext using Double Data Rate (DDR) algorithm.

    Parameters:
    plaintext (str): The plaintext to be encrypted.
    key (str): The encryption key.

    Returns:
    str: The encrypted ciphertext.
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % len(key)]
        ciphertext += chr(ord(char) + ord(key_char))
    return ciphertext


def decrypt_ddr(ciphertext, key):
    """
    Decrypts ciphertext encrypted using Double Data Rate (DDR) algorithm.

    Parameters:
    ciphertext (str): The ciphertext to be decrypted.
    key (str): The encryption key.

    Returns:
    str: The decrypted plaintext.
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % len(key)]
        plaintext += chr(ord(char) - ord(key_char))
    return plaintext


# DDR and GRP credit: Princeton University, http://palms.ee.princeton.edu/PALMSopen/lee04permutation_book.pdf


# Example usage:
plaintext = "Hello, World!"
key = generate_key()
for _ in range(14):
    c = encrypt_grp(plaintext, key)
    c = encrypt_ddr(c, "key")

print("Encrypted:", c)

for _ in range(14):
    p = decrypt_ddr(c, "key")
    p = decrypt_grp(p, key)

print("Decrypted:", p)