matrix = [
    [0x10, 0x20, 0x30, 0x40],
    [0x50, 0x60, 0x70, 0x80],
    [0x90, 0xA0, 0xB0, 0xC0],
    [0xD0, 0xE0, 0xF0, 0x00]
]


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([f'{x:02X}' for x in row]))


def transpose_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    transposed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed[i][j] = matrix[j][i]

    return transposed


if __name__ == '__main__':
    print_matrix(matrix)
    print()
    print_matrix(transpose_matrix(matrix))
