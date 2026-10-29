import math

def sender(m: int, poly: int) -> int:
    digits_to_add = (math.ceil(math.log2(poly)))
    message_p = m << digits_to_add
    remainder = modulo_two_division(message_p, poly)
    message_bin = m
    return (message_bin << digits_to_add) + remainder


def receiver(m: int, poly: int) :
    remainder = modulo_two_division(m, poly)
    digits_to_remove = (math.ceil(math.log2(poly)))
    original = m >> digits_to_remove
    return  original, remainder == 0


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


def sender_str(m: str, poly: str) -> int:
    return sender(int(m, 2), int(poly, 2))

def receiver_str(m: str, poly: str) :
    original, remainder = receiver(int(m, 2), int(poly,2))
    return  f"{original:b}", remainder

def main():
    message = input("Enter a message: ")
    polynomial = input("Enter a polynomial: ")

    message_transmitted = f"{sender_str(message, polynomial):b}"
    print(f"Message transmitted: {message_transmitted}")
    message_received, valid = receiver_str(message_transmitted, polynomial)
    if valid:
        print(f"Message received: {message_received}, without error")
    else:
        print(f"Message received: {message_received}, with error")


if __name__ == "__main__":
    main()





