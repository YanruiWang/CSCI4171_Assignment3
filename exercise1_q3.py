import random
from unittest import result

from exercise1_q2 import sender
from exercise1_q2 import receiver

# x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1
CRC_32_POLY = 0x04C11DB7
random_data = random.randbytes(1520)

arr = list()
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


results = list()
length = len(arr)
for i in range(length):
    a = []
    for j in range(50):
        received = arr[i][j]
        r, correct = receiver(received, CRC_32_POLY)
        a.append(correct)
    results.append(a)


i = 1
for index in range(len(results)):
    burst_length = 2 ** index
    count = sum(1 for x in arr[index] if x)
    length = len(arr[index])
    print(f"{burst_length}    {length}    {count}    {count/length}")
