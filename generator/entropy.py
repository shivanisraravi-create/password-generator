import math

def calculate_entropy(length, charset_size):
    if charset_size == 0:
        return 0
    return round(length * math.log2(charset_size), 2)
