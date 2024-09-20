from requirements import key, s_box_1, s_box_2, s_box_3, s_box_4
from operators import add32, add64, xor64, xor32

plaintext = '0xa0a35e8ca7710'
salt = '0xd62af4866aafe96e'
work_factor = 13


def find_sbox_output(sbox, input):
    colunm = int(str(input[0]) + str(input[6]) + str(input[7]), 2)
    row = int(str(input[1]) + str(input[2]) + str(input[3]) + str(input[4] + str(input[5])), 2)
    output = sbox[row][colunm]
    output = bin(int(output, 16))[2:]
    output = output.zfill(32)

    return output




def w(input):
    split_plaintext = [(input[i:i + 8]) for i in range(0, len(input), 8)]
    res_sbox1 = find_sbox_output(s_box_1, split_plaintext[0])
    res_sbox2 = find_sbox_output(s_box_2, split_plaintext[1])
    res_sbox3 = find_sbox_output(s_box_3, split_plaintext[2])
    res_sbox4 = find_sbox_output(s_box_4, split_plaintext[3])
    add1 = add32(res_sbox1, res_sbox2)
    xor = xor32(add1, res_sbox3)
    add2 = add32(xor, res_sbox4)
    return add2




def round(input, key):
    key = key.rstrip('L')  # Remove 'L' character
    key = bin(int(key, 16))[2:]
    left_32bit = input[0:32]
    right_32bit = input[32:64]
    w_input = xor32(left_32bit, key)
    new_left = xor32(w(w_input), right_32bit)
    new_right = left_32bit
    output = new_left + new_right
    return output

def lastrounrd(input, key):

    left_32bit = input[0:32]
    right_32bit = input[32:64]
    new_left = xor32(right_32bit, bin(int(key[31].rstrip('L'), 16))[2:])
    new_right = xor32(left_32bit, bin(int(key[30].rstrip('L'), 16))[2:])
    output = new_left + new_right
    return output


def box(input, key):
    cipher = input
    for i in range(32):
        cipher = round(cipher, key[i])
    cipher = lastrounrd(cipher, key)
    return cipher

def main_algorithm(plaintext, key, salt, work_factor):
    plaintext = bin(int(plaintext, 16))[2:].zfill(64)
    salt = bin(int(salt, 16))[2:].zfill(64)
    new_ciphertext = plaintext
    for i in range(2 ** work_factor):
        box_output = box(new_ciphertext, key)
        ciphertext = xor64(salt, box_output)
        new_ciphertext = ciphertext

    integer_value = int(ciphertext, 2)
    hex_str = hex(integer_value)
    hex_str = '0x' + hex_str[2:]
    print(hex_str)

main_algorithm(plaintext, key, salt, work_factor)
