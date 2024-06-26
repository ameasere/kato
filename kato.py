# // Main Class //

class Kato:
    def __init__(self, key, iv):

        self.__plaintext = None
        self.__ciphertext = None
        self.__key = None
        self.__iv = None

        if not isinstance(key, bytes):
            raise KatoInternalError("Key must be a bytes-like object, 461")

        elif not isinstance(iv, bytes):
            raise KatoInternalError("Initialisation Vector must be a bytes-like object, 461")

        if not len(key) == 16:
            raise KatoInternalError("Key must be 16 bytes long, 462")
        else:
            self.__key = key

        if not len(iv) == 16:
            raise KatoInternalError("Initialisation Vector must be 16 bytes long, 462")
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

        self.rounds = 14
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

    def __encrypt_grp(self, plaintext, key):
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

    def __decrypt_grp(self, ciphertext, key):
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

    def __encrypt_ddr(self, plaintext, key):
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

    def __decrypt_ddr(self, ciphertext, key):
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

    def __add_round_key(self, state, round_key):
        """
        Performs the AddRoundKey operation in Rijndael/AES encryption.

        Parameters:
        state (list of lists): The state matrix (4x4) representing the current state.
        round_key (list of lists): The round key matrix (4x4) used for the current round.

        Returns:
        list of lists: The resulting state matrix after adding the round key.
        """
        result_state = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result_state[i][j] = state[i][j] ^ round_key[i][j]
        return result_state

    def __key_expansion(self, key):
        """
        Expands the key to generate round keys for each round of encryption.

        Parameters:
        key (bytes): The original encryption key.

        Returns:
        list of lists: The expanded round keys for each round.
        """
        # Convert key to hexadecimal
        key_hex = [hex(byte) for byte in key]
        w0 = key_hex[:4]
        w1 = key_hex[4:8]
        w2 = key_hex[8:12]
        w3 = key_hex[12:16]
        # g(w3) = s-box substitution + xor with rcon
        # s-box is a list of lists
        # For the hex values in w3: first hex bit is the row, second hex bit is the column
        # For example, if w3[0] = 0x01, then the row is 0 and the column is 1
        # Get this value from the s-box, this is the new value of w3[0]
        # XOR this value with rcon[0] to get the new value of w3[0]
        # Repeat this for all 4 bytes in w3
        # All values in the s-box are in the form of 0x00

        gw3 = []
        for i in range(4):
            row = int(w3[i], 16) >> 4
            col = int(w3[i], 16) & 0x0F
            s_box_val = self.s_box[row][col]
            rcon_val = self.rcon[i]
            gw3.append(s_box_val ^ rcon_val)
        # w4 = w0 XOR gw3
        w4 = [hex(int(w0[i], 16) ^ gw3[i]) for i in range(4)]
        # w5 = w4 XOR w1
        w5 = [hex(int(w4[i], 16) ^ int(w1[i], 16)) for i in range(4)]
        # w6 = w5 XOR w2
        w6 = [hex(int(w5[i], 16) ^ int(w2[i], 16)) for i in range(4)]
        # w7 = w6 XOR w3
        w7 = [hex(int(w6[i], 16) ^ int(w3[i], 16)) for i in range(4)]
        # Round key = w4, w5, w6, w7
        round_key = w4 + w5 + w6 + w7
        return round_key

    def encrypt(self, plaintext):
        if not isinstance(plaintext, bytes):
            raise KatoInternalError("Plaintext must be a bytes-like object, 461")
        else:
            self.__plaintext = plaintext  # Private attribute.

        # 1: Key Expansion
        # 2: Initial Round
        # 3: Rounds

        # First time round: XOR the message with the IV.
        state = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                state[j][i] = plaintext[i + 4 * j] ^ self.__iv[i + 4 * j]

        # Key Expansion
        self.__key_expansion(self.__key)


    def decrypt(self, ciphertext):
        if not isinstance(ciphertext, bytes):
            raise KatoInternalError("Ciphertext must be a bytes-like object, 461")
        else:
            self.__ciphertext = ciphertext  # Private attribute.


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
    k = Kato(b"1234567890123456", b"1234567890123456")
    k.encrypt(bytes("abcdefghijklmnop", "utf-8"))  # If you provide the same key and plaintext, the first state table remains all 0.

