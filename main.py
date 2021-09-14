from ben_ryan_key_expansion import keyExpansion
from textwrap import wrap
from mix_columns import mixColumn
import numpy as np
import codecs

def convert_to_matrix(plaintext):
    if len(plaintext) > 16:
        return None

    aes_matrix = []

    for i in range(0, len(plaintext), 4):
        four_bytes_section = plaintext[i: i + 4]
        aes_matrix.append(list(four_bytes_section))

    return aes_matrix

def sub_bytes(arg):
    return np.transpose(convert_to_matrix(arg))

def shift_rows(arg):
    arg[0] = np.roll(arg[0], 0)
    arg[1] = np.roll(arg[1], 1)
    arg[2] = np.roll(arg[2], 2)
    arg[3] = np.roll(arg[3], 3)

    return arg

def mix_columns(matrix):
    for i in range(4):
        matrix[i] = mixColumn(matrix[i])

    print('Mixed: ', matrix)
    return matrix

def xor_key(key_round, plaintext):
    result = []

    for i in range(4):
        y = i * 4

        result.append(bytes([int(key_round[i], 16) ^ int.from_bytes(plaintext[y], 'big')]))
        result.append(bytes([int(key_round[i], 16) ^ int.from_bytes(plaintext[y + 1], 'big')]))
        result.append(bytes([int(key_round[i], 16) ^ int.from_bytes(plaintext[y + 2], 'big')]))
        result.append(bytes([int(key_round[i], 16) ^ int.from_bytes(plaintext[y + 3], 'big')]))

    return result


def key_expansion(key):
    return keyExpansion(wrap(key, 2))

def encrypt(key, plaintext, rounds):
    key_expanded = key_expansion(key)

    result = xor_key(key_expanded[0], plaintext)

    for i in range(rounds):
        result = sub_bytes(result)
        result = shift_rows(result)
        result = mix_columns(result)
        # mix columns
        result = xor_key(key_expanded[i], np.array(result).flatten())

    result = sub_bytes(result)
    result = shift_rows(result)
    result = xor_key(key_expanded[-1], np.array(result).flatten())

    return result

# We will receive chunks of 16 bytes to encrypt when reading the file:
#
# f = open("selfie.jpeg", "rb")
# try:
#     byte = f.read(1)
#     while byte != "":
#         # Do stuff with byte.
#         byte = f.read(1)
#         print(byte)
# finally:
#     f.close()
print(encrypt('0f1571c947d9e8590cb7add6af7f6798', [b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8',b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8'], 2))
