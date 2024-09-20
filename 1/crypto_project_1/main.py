import random


def add(a, b):
    a = (int(a, 2))
    b = (int(b, 2))
    return format(((a + b) % (2 ** 16)), '016b')


def multiplication(a, b):
    a = (int(a, 2))
    b = (int(b, 2))
    return format(((a * b) % ((2 ** 16) + 1)), '016b')


def xor(a, b, n):
    a = (int(a, 2))
    b = (int(b, 2))
    return format(a ^ b, f'0{n}b')


def cyclic_shift(k, shift):
    return k[shift:] + k[:shift]


def splitter(n, number):
    split = [(n[i:i + number]) for i in range(0, len(n), number)]
    return split


def generate_random_num(n):
    number = random.getrandbits(n)
    binary_string = format(number, '0b')
    return binary_string


def keygen(key):
    keys = []
    for i in range(8):
        temp = splitter(key, 16)
        keys.extend(temp[0:8])
        cyclic_shift(key, 25)

    return keys


def Encryption_algorithm(plaintext, key, nr, round):
    plaintext = splitter(plaintext, 16)
    index = nr * 6

    if round < 8:
        step_1 = multiplication(plaintext[0], key[index])
        step_2 = add(plaintext[1], key[index + 1])
        step_3 = add(plaintext[2], key[index + 2])
        step_4 = add(plaintext[3], key[index + 3])
        step_5 = xor(step_1, step_3, 16)
        step_6 = xor(step_2, step_4, 16)
        step_7 = multiplication(step_5, key[index + 4])
        step_8 = add(step_7, step_6)
        step_9 = multiplication(step_8, key[index + 5])
        step_10 = add(step_7, step_9)
        step_11 = xor(step_1, step_9, 16)
        step_12 = xor(step_3, step_9, 16)
        step_13 = xor(step_2, step_10, 16)
        step_14 = xor(step_4, step_10, 16)

        plaintext_round_result = f'{step_11}{step_12}{step_13}{step_14}'

    else:
        step_1 = multiplication(plaintext[0], key[index])
        step_2 = add(plaintext[1], key[index + 1])
        step_3 = add(plaintext[2], key[index + 2])
        step_4 = multiplication(plaintext[3], key[index + 3])
        plaintext_round_result = f'{step_1}{step_2}{step_3}{step_4}'

    return plaintext_round_result


plaintext = "0111010001100101011100110111010001001001010001000100010101000001"
key = "01101011011001010111100101100111011001010110111001100101011100100110000101110100011001010110010001001001010001000100010101000001"


def first_mode(plain_text, key):
    result = ""
    plain_text_blocks = splitter(plain_text, 64)
    key_blocks = splitter(key, 128)

    for i in range(len(plain_text_blocks)):
        ciphertext = plain_text_blocks[i]
        current_key = keygen(key_blocks[0])

        for round_num in range(9):
            ciphertext = Encryption_algorithm(ciphertext, current_key, round_num, round_num)

        result += ciphertext

    print("Cipher Text : " + str(result))
    return


def CBC(plain_text, key):
    result = ""
    key_blocks = key
    plain_text_blocks = splitter(plain_text, 64)
    key_blocks = splitter(key_blocks, 128)
    num = generate_random_num(64)

    for i in range(len(plain_text_blocks)):
        current_key = keygen(key_blocks[0])
        ciphertext = xor(plain_text_blocks[i], num, 64)

        for round_num in range(9):
            ciphertext = Encryption_algorithm(ciphertext, current_key, round_num, round_num)

        num = ciphertext
        result += ciphertext

    print("Cipher Text : " + str(result))
    return


def CTR(plaintext, key):
    result = ""
    key_blocks = key

    plain_text_blocks = splitter(plaintext, 64)
    key_blocks = splitter(key_blocks, 128)
    counter = 0

    for i in range(len(plain_text_blocks)):
        target_key = keygen(key_blocks[0])

        ciphertext = format(counter, '064b')

        for round_num in range(9):
            ciphertext = Encryption_algorithm(ciphertext, target_key, round_num, round_num)

        ciphertext = xor(ciphertext, plain_text_blocks[i], 64)
        result += ciphertext

        counter += 1

    print("Cipher Text : " + str(result))
    return


# first_mode(plaintext, key)
# CBC(plaintext, key)
# CTR(plaintext, key)
