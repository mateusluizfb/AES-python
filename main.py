import numpy as np

# Rows should handled as columns, and columns as rows
def convert_to_matrix(plaintext):
    if len(plaintext) > 16:
        return None

    aes_matrix = []

    for i in range(0, len(plaintext), 4):
        four_bytes_section = plaintext[i: i + 4]
        bytes_to_int_list = list(four_bytes_section)
        aes_matrix.append(bytes_to_int_list)

    return aes_matrix

def sub_bytes(arg):
    return np.transpose(arg)

def shift_rows(arg):
    arg[0] = np.roll(arg[0], 0)
    arg[1] = np.roll(arg[1], 1)
    arg[2] = np.roll(arg[2], 2)
    arg[3] = np.roll(arg[3], 3)

    return arg

def mix_columns(arg):
    mix_column_matrix = np.array([
        [2 , 3, 1, 1],
        [1 , 2, 3, 1],
        [1 , 1, 2, 3],
        [3 , 1, 1, 2]
    ])

    for i in range(4):
        res = np.matmul(mix_column_matrix, np.array(arg[i]))
        arg[i] = res

    return arg

def add_key(arg):
    pass

def encrypt(plaintext):
    print(plaintext)
    plaintext_matrix = convert_to_matrix(plaintext)
    result = None
    result = sub_bytes(plaintext_matrix)
    result = shift_rows(result)
    result = mix_columns(result)
    return result


# print(bytes([56]))
print(encrypt(b'1234567812345678'))
# print("1234567812345678".encode())
