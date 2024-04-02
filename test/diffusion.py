import colorama


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


# Example usage:
input_matrix = [
    [0x00, 0x01, 0x02, 0x03],
    [0x04, 0x05, 0x06, 0x07],
    [0x08, 0x09, 0x0A, 0x0B],
    [0x0C, 0x0D, 0x0E, 0x0F]
]  # Example 4x4 input matrix
key = [3, 1, 0, 2]  # Example key for linear permutation
encrypted_matrix = omflip_matrix(input_matrix, key)
print(f"{colorama.Fore.RED}Input matrix: {colorama.Style.RESET_ALL}")
for row in input_matrix:
    print(row)
print(f"{colorama.Fore.BLUE}Encrypted matrix: {colorama.Style.RESET_ALL}")
for row in encrypted_matrix:
    print(row)

decrypted_matrix = omflip_decrypt_matrix(encrypted_matrix, key)
print(f"{colorama.Fore.GREEN}Decrypted matrix: {colorama.Style.RESET_ALL}")
for row in decrypted_matrix:
    print(row)
