import random

from exercise1_q2 import sender
from exercise1_q2 import receiver
from exercise1_q2 import modulo_two_division

# x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1
CRC_32_POLY = 0b0000_0100_1100_0001_0001_1101_1011_0111

random_data = random.randbytes(1520)