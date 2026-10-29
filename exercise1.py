import math


def sender(message: str, polynomial: str):
    # convert poly to decimal
    bin_poly = int(polynomial,2)
    # number of zeros to add
    poly_digit = math.floor(math.log2(bin_poly))
    # add zeros to message
    message_zero = int(message, 2) << poly_digit
    return message_zero

def modulo_two_division(a: str, b: str) -> int:

    length_b = math.ceil(math.log2(int(b,2)))
    remaining = int(a, 2)
    b_binary = int(b, 2)
    while remaining >= b_binary:
        digits = math.ceil(math.log2(remaining))
        remaining = remaining ^ (b_binary << (digits - length_b))

    return remaining


div = sender("1000", "111010")
od = modulo_two_division("110100111101", "1011")
print(od)
