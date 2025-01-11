# n = p_0 * p_1 * ... * p_{m-1}
# p_{m-1} = n / (p_0 * p_1 * ... * p_{m-2})

import math

def smallest_prime_factor(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return i
    return n

def solve():
    n = 600851475143

    while True:
        p = smallest_prime_factor(n)
        if p < n: 
            n //= p
        else: 
            return n


if __name__ == "__main__":
    print(solve())