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
    bits_a = []
    for bit in a:
        bits_a.append(int(bit))
    bits_b = []
    for bit in b:
        bits_b.append(int(bit))

    print(bits_a)
    print(bits_b)
    return 0


div = sender("1000", "111010")
od = modulo_two_division(f"{div:b}", "111010")
