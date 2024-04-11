"""
Strict Avalanche Criterion (SAC) test for Kato.

When changing a single input bit, the output should change with a probability of 0.5 or more.
We should test this using random bytes and change 1 bit at a time.
"""
import unittest
import random
from kato import Kato
from colorama import Fore, Style

from colorama import Fore, Style


def sac_ecb_test(key, plaintext, encrypt_func):
    """
    Perform Strict Avalanche Criterion (SAC) test for ECB mode encryption.

    Args:
    - key: The encryption key.
    - plaintext: The plaintext to encrypt.
    - encrypt_func: A function that takes a key and plaintext as input and returns the ciphertext.

    Returns:
    - True if the test passes (output changes with probability >= 0.5), False otherwise.
    """
    changed_bits_count = 0
    total_bits = 128  # 16 bytes * 8 bits/byte

    for i in range(16):
        for j in range(8):
            # Flip one bit in the key and plaintext
            key_modified = bytes([key[i] ^ (1 << j) if k == i else key[k] for k in range(16)])
            plaintext_modified = bytes([plaintext[i] ^ (1 << j) if k == i else plaintext[k] for k in range(16)])

            # Encrypt modified plaintext with modified key
            ciphertext_modified = encrypt_func(key_modified, None, plaintext_modified)

            # Check if the output changes
            if ciphertext_modified != encrypt_func(key, None, plaintext):
                changed_bits_count += 1

    # Check if at least 50% of the bits change
    print(f"{Fore.GREEN}Probability of change: {changed_bits_count / total_bits}{Style.RESET_ALL}")
    return changed_bits_count >= total_bits / 2

def sac_cbc_test(key, iv, plaintext, encrypt_func):
    """
    Perform Strict Avalanche Criterion (SAC) test for CBC mode encryption.

    Args:
    - key: The encryption key.
    - iv: The initialization vector.
    - plaintext: The plaintext to encrypt.
    - encrypt_func: A function that takes a key, iv, and plaintext as input and returns the ciphertext.

    Returns:
    - True if the test passes (output changes with probability >= 0.5), False otherwise.
    """
    changed_bits_count = 0
    total_bits = 128  # 16 bytes * 8 bits/byte

    for i in range(16):
        for j in range(8):
            # Flip one bit in the key, iv, and plaintext
            key_modified = bytes([key[i] ^ (1 << j) if k == i else key[k] for k in range(16)])
            iv_modified = bytes([iv[i] ^ (1 << j) if k == i else iv[k] for k in range(16)])
            plaintext_modified = bytes([plaintext[i] ^ (1 << j) if k == i else plaintext[k] for k in range(16)])

            # Encrypt modified plaintext with modified key and iv
            ciphertext_modified = encrypt_func(key_modified, iv_modified, plaintext_modified)

            # Check if the output changes
            if ciphertext_modified != encrypt_func(key, iv, plaintext):
                changed_bits_count += 1

    # Check if at least 50% of the bits change
    print(f"{Fore.GREEN}Probability of change: {changed_bits_count / total_bits}{Style.RESET_ALL}")
    return changed_bits_count >= total_bits / 2


class TestSAC(unittest.TestCase):
    def test_sac_ecb(self):
        key = bytes(random.sample(range(256), 16))
        plaintext = bytes(random.sample(range(256), 16))

        # Define your encrypt function (replace this with your actual encryption function)
        def encrypt_func(key, iv, plaintext):
            if iv is not None:
                k = Kato(key, iv)
                return k.encrypt(plaintext)
            else:
                k = Kato(key)
                return k.encrypt(plaintext)

        if sac_ecb_test(key, plaintext, encrypt_func):
            print(Fore.GREEN + "ECB SAC Test Passed!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "ECB SAC Test Failed!" + Style.RESET_ALL)

    def test_sac_cbc(self):
        key = bytes(random.sample(range(256), 16))
        iv = bytes(random.sample(range(256), 16))
        plaintext = bytes(random.sample(range(256), 16))

        # Define your encrypt function (replace this with your actual encryption function)
        def encrypt_func(key, iv, plaintext):
            if iv is not None:
                k = Kato(key, iv)
                return k.encrypt(plaintext)
            else:
                k = Kato(key)
                return k.encrypt(plaintext)

        if sac_cbc_test(key, iv, plaintext, encrypt_func):
            print(Fore.GREEN + "CBC SAC Test Passed!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "CBC SAC Test Failed!" + Style.RESET_ALL)


if __name__ == '__main__':
    unittest.main()
