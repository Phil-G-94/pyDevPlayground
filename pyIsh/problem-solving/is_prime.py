from math import sqrt

def is_prime(number: int) -> bool:
    if number <= 1: return False
    if number == 2: return True
    if number % 2 == 0: return False

    num_sqrt = int(sqrt(number))  # only check up to sqrt(num)
    for i in range(3, num_sqrt + 1, 2):  # check odd numbers only
        if number % i == 0:  # i divides num evenly
            return False

    return True  # no factors found, num is prime