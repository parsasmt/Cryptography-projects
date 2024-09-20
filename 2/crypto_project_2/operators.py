def add32(a, b):
    int1 = int(a, 2)
    int2 = int(b, 2)
    sum_binary = bin((int1 + int2) % (2 ** 32))[2:]
    sum_binary = sum_binary.zfill(32)
    return sum_binary


def add64(a, b):
    int1 = int(a, 2)
    int2 = int(b, 2)
    sum_binary = bin((int1 + int2) % (2 ** 32))[2:]
    sum_binary = sum_binary.zfill(64)
    return sum_binary



def xor32(a, b):
    int1 = int(a, 2)
    int2 = int(b, 2)

    xor_result = int1 ^ int2
    xor_binary = bin(xor_result)[2:]
    xor_binary = xor_binary.zfill(32)
    return xor_binary



def xor64(a, b):
    int1 = int(a, 2)
    int2 = int(b, 2)

    xor_result = int1 ^ int2
    xor_binary = bin(xor_result)[2:]
    xor_binary = xor_binary.zfill(64)
    return xor_binary


