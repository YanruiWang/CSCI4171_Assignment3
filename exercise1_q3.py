import random
from unittest import result

from exercise1_q2 import sender
from exercise1_q2 import receiver
from exercise1_q2 import modulo_two_division

# x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1
CRC_32_POLY = 0x04C11DB7
random_data = random.randbytes(1520)

arr = [[]]
i = 1
while i <= 64:
    a = [] * 50
    for j in range(1, 51):
        transmitted = sender(int.from_bytes(random_data, byteorder="big"), CRC_32_POLY)
        random_start = random.randint(1, 1520+32-i)
        random_end = random_start + j
        for k in range(random_start, random_end):
            transmitted = transmitted ^ (1 << k)
        a.append(transmitted)

    arr.append(a)
    i = i * 2


results = [[]]
length = len(arr)
for i in range(2, length):
    a = []
    for j in range(50):
        received = arr[i][j]
        r, correct = receiver(received, CRC_32_POLY)
        a.append(correct)
    results.append(a)

print(results)
