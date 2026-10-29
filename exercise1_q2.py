import math


def sender_str(m: str, poly: str) -> int:

    digits_to_add = (math.ceil(math.log2(int(poly, 2))))
    message_p = int(m, 2) << digits_to_add
    remainder = modulo_two_division_str(f"{message_p:b}", poly)
    message_bin = int(m, 2)
    return (message_bin << digits_to_add) + remainder

def receiver_str(m: str, poly: str) :
    remainder = modulo_two_division_str(m, poly)
    poly_bin = int(poly, 2)
    digits_to_remove = (math.ceil(math.log2(int(poly_bin))))
    original = int(m, 2) >> digits_to_remove
    return  f"{original:b}", remainder == 0


def modulo_two_division_str(a: str, b: str) -> int:
    """returns the remainder of two modulo division"""
    remaining = int(a, 2)
    b_binary = int(b, 2)
    return modulo_two_division(remaining, b_binary)

def modulo_two_division(a: int, b: int) -> int:
    length_b = math.ceil(math.log2(b))
    remaining = a
    while remaining >= b:
        digits = math.ceil(math.log2(remaining))
        remaining = remaining ^ (b << (digits - length_b))

    return remaining


message = input("Enter a message: ")
polynomial = input("Enter a polynomial: ")

message_transmitted = f"{sender_str(message, polynomial):b}"
print(f"Message transmitted: {message_transmitted}")
message_received, valid = receiver_str(message_transmitted, polynomial)
if valid:
    print(f"Message received: {message_received}, without error")
else:
    print(f"Message received: {message_received}, with error")




