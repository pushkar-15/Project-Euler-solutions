# Brute Force:

import math, itertools

def solve():
	ans = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
		key=count_consecutive_primes)
	return str(ans[0] * ans[1])

def count_consecutive_primes(ab):
	a, b = ab
	for i in itertools.count():
		n = i * i + i * a + b
		if not is_prime(n):
			return i

def is_prime(n):
	if n <= 0 or n == 1 or n % 2 == 0 : return False
	if n <= 3: return True
	for i in range(3, math.isqrt(n) + 1, 2):
		if n % i == 0: return False
	return True

if __name__ == "__main__":
	print(solve())


# More efficient: use prime sieve to check primality after precomputation for [1,1000].

# Even more efficient: for n = 0 and n = 1, b = prime and 1+a+b = prime respectively,
# so for each prime b, iterate over primes p to get a = p-b-1.