import random
from unittest import result

from exercise1_q2 import sender
from exercise1_q2 import receiver

# x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1
CRC_32_POLY = 0b100000100110000010001110110110111
random_data = random.randbytes(1520)

arr = list()
i = 8
while i <= 64:
    a = list()
    for j in range(1, 51):
        transmitted = sender(int.from_bytes(random_data, byteorder="big"), CRC_32_POLY)
        random_start = random.randint(0, 1520+32-i-1)
        random_end = random_start + i
        for k in range(random_start, random_end):
            transmitted = transmitted | (1 << k)
        a.append(transmitted)

    arr.append(a)
    i = i + 8


results = list()
length = len(arr)
for i in range(length):
    a = list()
    for j in range(50):
        received = arr[i][j]
        r, correct = receiver(received, CRC_32_POLY)
        a.append(correct)
    results.append(a)


i = 8
print("burst length(bits)   trails      errors      detection rate")
for index in range(len(results)):
    burst_length = (index + 1) * 8
    count = sum(1 for x in arr[index] if x)
    length = len(arr[index])
    print(f"{burst_length}    {length}    {count}    {count/length * 100}%")

