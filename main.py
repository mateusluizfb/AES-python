import numpy as np

# Rows should handled as columns, and columns as rows
def convert_to_matrix(plaintext):
    if len(plaintext) > 16:
        return None

    aes_matrix = []

    for i in range(0, len(plaintext), 4):
        four_bytes_section = plaintext[i: i + 4]
        caracter_list = list(four_bytes_section)
        aes_matrix.append(caracter_list)

    return aes_matrix

def sub_bytes(arg):
    return np.transpose(arg)

def shift_rows(arg):
    print(arg)

    arg[0] = np.roll(arg[0], 0)
    arg[1] = np.roll(arg[1], 1)
    arg[2] = np.roll(arg[2], 2)
    arg[3] = np.roll(arg[3], 3)

    return arg

def mix_columns(arg):
    pass

def add_key(arg):
    pass

def encrypt(plaintext):
    plaintext_matrix = convert_to_matrix(plaintext)
    result = None
    result = sub_bytes(plaintext_matrix)
    result = shift_rows(result)

    print(result)

print(encrypt("1234567812345678"))
