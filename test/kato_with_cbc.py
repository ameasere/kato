# // Main Class //
import colorama  # Debugging purposes only.
# Import Rijndael key expansion algorithm
from aeskeyschedule import key_schedule, reverse_key_schedule


class Kato:
    def __init__(self, key, iv):

        self.__plaintext = None
        self.__ciphertext = None
        self.__key = None
        self.__iv = None

        if not isinstance(key, bytes):
            raise KatoInternalError("Key must be a bytes-like object, 461")

        if not len(key) == 16:
            raise KatoInternalError("Key must be 16 bytes long, 462")
        else:
            self.__key = key

        if not isinstance(iv, bytes):
            raise KatoInternalError("IV must be a bytes-like object, 461")

        if not len(iv) == 16:
            raise KatoInternalError("IV must be 16 bytes long, 462")
        else:
            self.__iv = iv

        self.key_length = len(key)
        self.s_box = [  # Implemented custom S-Box from paper: doi: 10.1016/j.protcy.2013.12.443
            [0x31, 0x2E, 0x04, 0xAB, 0xC6, 0x70, 0x91, 0x61, 0x19, 0x9F, 0xDC, 0x7D, 0xAD, 0x7F, 0xAC, 0xFF],
            [0x56, 0x82, 0xE8, 0x67, 0xA0, 0x43, 0xB2, 0x4A, 0x36, 0x08, 0x17, 0x22, 0xB8, 0x4F, 0x0E, 0xAE],
            [0xFE, 0xD6, 0x78, 0x95, 0xD9, 0x45, 0x0B, 0x96, 0x58, 0x3F, 0x8C, 0x55, 0x03, 0x92, 0xE0, 0x63],
            [0x18, 0x1F, 0x26, 0x00, 0x13, 0x9A, 0xE4, 0xDB, 0x44, 0x8B, 0x6C, 0x25, 0x81, 0x69, 0x1D, 0x27],
            [0x80, 0xE9, 0xE7, 0x5A, 0x3E, 0x0C, 0xAF, 0x7E, 0x2C, 0x05, 0x2B, 0x3C, 0x0D, 0x2F, 0x84, 0x51],
            [0xBB, 0xCE, 0x74, 0x29, 0x3D, 0x8D, 0xD5, 0xF9, 0xEF, 0x5E, 0x86, 0x50, 0x3B, 0x34, 0x09, 0x97],
            [0xD8, 0xC5, 0xF1, 0xEB, 0xE6, 0xDA, 0xC4, 0x71, 0x11, 0x9B, 0x64, 0x21, 0x39, 0x35, 0x89, 0x6D],
            [0xA5, 0x7B, 0x14, 0xA3, 0xC2, 0xC8, 0xCD, 0xF5, 0x53, 0xBA, 0x4E, 0x8E, 0x54, 0x83, 0x68, 0x9D],
            [0xDD, 0xFD, 0x57, 0x02, 0x12, 0x1A, 0x1E, 0xA6, 0xFA, 0x6E, 0x24, 0x01, 0x93, 0x60, 0x99, 0x65],
            [0xA1, 0xC3, 0x48, 0x37, 0x88, 0xED, 0x5F, 0x06, 0xAA, 0x46, 0x8A, 0xEC, 0xDF, 0xFC, 0xD7, 0xF8],
            [0x6F, 0xA4, 0xFB, 0xEE, 0xDE, 0x7C, 0x2D, 0x85, 0xD1, 0x41, 0xB3, 0xCA, 0xCC, 0x75, 0xA9, 0xC7],
            [0xF0, 0x6B, 0x1C, 0xA7, 0x7A, 0x94, 0x59, 0xBF, 0x76, 0x28, 0xBD, 0x77, 0xA8, 0x47, 0x0A, 0x16],
            [0xA2, 0x42, 0x32, 0xB0, 0x4B, 0xB6, 0xF2, 0x6A, 0x9C, 0x5D, 0x07, 0x2A, 0xBC, 0xF7, 0x52, 0x3A],
            [0xB4, 0xF3, 0xEA, 0x66, 0x20, 0xB9, 0xCF, 0xF4, 0xD3, 0x40, 0x33, 0x30, 0xB1, 0xCB, 0x4C, 0x8F],
            [0xD4, 0x79, 0x15, 0x23, 0x38, 0xB5, 0x73, 0x10, 0x1B, 0x9E, 0x5C, 0x87, 0xD0, 0xC1, 0x49, 0xB7],
            [0x72, 0x90, 0xE1, 0xE3, 0xE2, 0x62, 0x98, 0xE5, 0x5B, 0xBE, 0xF6, 0xD2, 0xC0, 0xC9, 0x4D, 0x0F]
        ]

        self.inv_s_box = [
            # Implemented custom inverse S-Box from above S-Box.
            [0x33, 0x8B, 0x83, 0x2C, 0x02, 0x49, 0x97, 0xCA, 0x19, 0x5E, 0xBE, 0x26, 0x45, 0x4C, 0x1E, 0xFF],
            [0xE7, 0x68, 0x84, 0x34, 0x72, 0xE2, 0xBF, 0x1A, 0x30, 0x08, 0x85, 0xE8, 0xB2, 0x3E, 0x86, 0x31],
            [0xD4, 0x6B, 0x1B, 0xE3, 0x8A, 0x3B, 0x32, 0x3F, 0xB9, 0x53, 0xCB, 0x4A, 0x48, 0xA6, 0x01, 0x4D],
            [0xDB, 0x00, 0xC2, 0xDA, 0x5D, 0x6D, 0x18, 0x93, 0xE4, 0x6C, 0xCF, 0x5C, 0x4B, 0x54, 0x44, 0x29],
            [0xD9, 0xA9, 0xC1, 0x15, 0x38, 0x25, 0x99, 0xBD, 0x92, 0xEE, 0x17, 0xC4, 0xDE, 0xFE, 0x7A, 0x1D],
            [0x5B, 0x4F, 0xCE, 0x78, 0x7C, 0x2B, 0x10, 0x82, 0x28, 0xB6, 0x43, 0xF8, 0xEA, 0xC9, 0x59, 0x96],
            [0x8D, 0x07, 0xF5, 0x2F, 0x6A, 0x8F, 0xD3, 0x13, 0x7E, 0x3D, 0xC7, 0xB1, 0x3A, 0x6F, 0x89, 0xA0],
            [0x05, 0x67, 0xF0, 0xE6, 0x52, 0xAD, 0xB8, 0xBB, 0x22, 0xE1, 0xB4, 0x71, 0xA5, 0x0B, 0x47, 0x0D],
            [0x40, 0x3C, 0x11, 0x7D, 0x4E, 0xA7, 0x5A, 0xEB, 0x94, 0x6E, 0x9A, 0x39, 0x2A, 0x55, 0x7B, 0xDF],
            [0xF1, 0x06, 0x2D, 0x8C, 0xB5, 0x23, 0x27, 0x5F, 0xF6, 0x8E, 0x35, 0x69, 0xC8, 0x7F, 0xE9, 0x09],
            [0x14, 0x90, 0xC0, 0x73, 0xA1, 0x70, 0x87, 0xB3, 0xBC, 0xAE, 0x98, 0x03, 0x0E, 0x0C, 0x1F, 0x46],
            [0xC3, 0xDC, 0x16, 0xAA, 0xD0, 0xE5, 0xC5, 0xEF, 0x1C, 0xD5, 0x79, 0x50, 0xCC, 0xBA, 0xF9, 0xB7],
            [0xFC, 0xED, 0x74, 0x91, 0x66, 0x61, 0x04, 0xAF, 0x75, 0xFD, 0xAB, 0xDD, 0xAC, 0x76, 0x51, 0xD6],
            [0xEC, 0xA8, 0xFB, 0xD8, 0xE0, 0x56, 0x21, 0x9E, 0x60, 0x24, 0x65, 0x37, 0x0A, 0x80, 0xA4, 0x9C],
            [0x2E, 0xF2, 0xF4, 0xF3, 0x36, 0xF7, 0x64, 0x42, 0x12, 0x41, 0xD2, 0x63, 0x9B, 0x95, 0xA3, 0x58],
            [0xB0, 0x62, 0xC6, 0xD1, 0xD7, 0x77, 0xFA, 0xCD, 0x9F, 0x57, 0x88, 0xA2, 0x9D, 0x81, 0x20, 0x0F]
        ]

        self.rcon = [
            0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36
        ]

        self.rounds = 10
        self.block_size = 16

    @staticmethod
    def transpose_matrix(matrix):
        n = len(matrix)

        # Transpose the matrix
        transposed = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                transposed[i][j] = matrix[j][i]

        return transposed

    @staticmethod
    def __add_round_key(state, round_key):
        """
        Performs the AddRoundKey operation in Rijndael/AES encryption.

        Parameters:
        state (list of lists): The state matrix (4x4) representing the current state.
        round_key (bytes): The round key to be added to the state matrix.

        Returns:
        list of lists: The resulting state matrix after adding the round key.
        """
        # Convert round_key from bytes to a 4x4 matrix
        round_key = [[round_key[i + 4 * j] for i in range(4)] for j in range(4)]
        result_state = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result_state[i][j] = state[i][j] ^ round_key[i][j]
        return result_state

    @staticmethod
    def omflip_matrix(input_matrix, key):
        # Constants for bitwise operations
        mask = 0xFFFFFFFF
        shift = 5

        # Perform linear permutation
        output_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j, pos in enumerate(key):
                output_matrix[i][j] = input_matrix[i][pos]

        # Perform bitwise operations
        for i in range(4):
            for j in range(4):
                output_matrix[i][j] = ((output_matrix[i][j] << shift) | (output_matrix[i][j] >> (32 - shift))) & mask

        return output_matrix

    @staticmethod
    def omflip_decrypt_matrix(encrypted_matrix, key):
        # Constants for bitwise operations
        mask = 0xFFFFFFFF
        shift = 5

        # Inverse permutation of the key
        inv_key = [key.index(i) for i in range(4)]

        # Reverse bitwise operations
        decrypted_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                decrypted_matrix[i][j] = ((encrypted_matrix[i][j] >> shift) | (
                        encrypted_matrix[i][j] << (32 - shift))) & mask

        # Reverse linear permutation
        output_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j, pos in enumerate(inv_key):
                output_matrix[i][j] = decrypted_matrix[i][pos]

        return output_matrix

    @staticmethod
    def cipher_block_chaining(block, iv):
        """
        Performs the CBC operation on a block of ciphertext.

        Parameters:
        block (bytes): The block of ciphertext to be processed.
        iv (bytes): The initialization vector to be used.

        Returns:
        bytes: The resulting block of ciphertext after CBC.
        """
        # XOR the block with the IV
        # The block is a 4x4 matrix, list of lists
        result_block = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result_block[i][j] = block[i][j] ^ iv[i * 4 + j]
        return result_block

    def encrypt(self, plaintext):
        """
        if not isinstance(plaintext, bytes):
            raise KatoInternalError("Plaintext must be a bytes-like object, 461")
        else:
            self.__plaintext = plaintext  # Private attribute.
        """

        # 1: Key Expansion
        # 2: Initial Round
        # 3: Rounds

        # Initial State with plaintext
        state = []
        for i in range(0, len(plaintext), 4):
            state.append([plaintext[i], plaintext[i + 1], plaintext[i + 2], plaintext[i + 3]])
        # Key Expansion
        round_keys = key_schedule(self.__key)
        # XOR this with the initial key
        print(f"{colorama.Fore.BLUE}Starting Encryption with state: {state}{colorama.Style.RESET_ALL}")
        for n in range(self.rounds):
            # XOR with IV first
            state = self.cipher_block_chaining(state, self.__iv)
            state = [[self.s_box[state[i][j] // 16][state[i][j] % 16] for j in range(4)] for i in range(4)]
            state = self.transpose_matrix(state)
            state = self.__add_round_key(state, round_keys[n + 1])
            print(f"{colorama.Fore.RED}Round {n + 1} | State: {state} | Round Key Used: {round_keys[n+1]} {colorama.Style.RESET_ALL}")
        state = self.omflip_matrix(state, [3, 1, 0, 2])

        print(f"{colorama.Fore.GREEN}Encrypted State: {colorama.Style.RESET_ALL}")
        for row in state:
            print(row)

        # TEMP: convert to ciphertext bytes
        # Return as list of lists
        # We can't return as bytes, as all the hex numbers are >1000
        return state

    def decrypt(self, ciphertext):
        """
        if not isinstance(ciphertext, bytes):
            raise KatoInternalError("Ciphertext must be a bytes-like object, 461")
        else:
            self.__ciphertext = ciphertext  # Private attribute.
        """

        # Decryption: do everything in reverse order.

        # 1. Make the state matrix from the ciphertext
        # Reverse of b"".join([bytes(row) for row in state])
        state = ciphertext

        # 2. Initial Round Key Expansion (in reverse)
        round_keys = key_schedule(self.__key)[::-1]

        state = self.omflip_decrypt_matrix(state, [3, 1, 0, 2])
        print(f"{colorama.Fore.BLUE}Starting Decryption with state: {state}{colorama.Style.RESET_ALL}")
        for n in range(self.rounds):
            state = self.__add_round_key(state, round_keys[n])
            state = self.transpose_matrix(state)
            state = [[self.inv_s_box[state[i][j] // 16][state[i][j] % 16] for j in range(4)] for i in range(4)]
            # XOR with IV first
            state = self.cipher_block_chaining(state, self.__iv)

            print(
                f"{colorama.Fore.RED}Round {n + 1} | State: {state} | Round Key Used: {round_keys[n]} {colorama.Style.RESET_ALL}")

        print(f"{colorama.Fore.GREEN}Decrypted State: {colorama.Style.RESET_ALL}")
        try:
            plaintext = b"".join([bytes(row) for row in state])
            return plaintext
        except:
            return state


# /// Exception Handlers ///

class KatoInternalError(Exception):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        self.with_traceback(None)  # Tracebacks can leak sensitive information.

        super().__init__(message)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.message}, {self.code}"

    def __str__(self):
        return self.message


class KatoInternalWarning(Warning):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        self.with_traceback(None)  # Tracebacks can leak sensitive information.

        super().__init__(message)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.message}, {self.code}"

    def __str__(self):
        return self.message


if __name__ == "__main__":
    import random

    # Key must have no repeating values
    key = bytes(random.sample(range(256), 16))
    iv = bytes(random.sample(range(256), 16))
    k = Kato(key, iv)
    ciphertext = k.encrypt(bytes("abcdefghijklmnop",
                                 "utf-8"))  # If you provide the same key and plaintext, the first state table remains all 0.
    print(f"Ciphertext: {ciphertext}")
    plaintext = k.decrypt(ciphertext)
    print(plaintext)
