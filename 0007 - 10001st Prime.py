# Brute Force

import time
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    upper_bound = int(math.sqrt(n)) + 1
    for i in range(3, upper_bound, 2):
        if n % i == 0:
            return False
    return True

def solve():
    count, candidate = 1, 3  # Start with count=1 because 2 is prime
    target = 10001
    
    while count < target:
        if is_prime(candidate):
            count += 1
        candidate += 2
    
    return candidate - 2

if __name__ == "__main__":
    start_time = time.time()
    result = solve()
    print(result)
    print(time.time() - start_time)