class Kato:
    def __init__(self, key):
        self.key = key
        self.key_length = len(key)
        self.s_box = [

        ]
        self.inv_s_box = [

        ]
        self.r_con = [

        ]
        self.mix_columns = [

        ]
        self.inv_mix_columns = [

        ]
        self.rounds = 14
        self.block_size = 16

    def encrypt(self, plaintext):
        pass

    def decrypt(self, ciphertext):
        pass
