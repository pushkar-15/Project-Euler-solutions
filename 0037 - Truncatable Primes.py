import time, math, itertools

def solve():
	return sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), 11))

def is_truncatable_prime(n):
	i = 10
	# truncate right to left:
	while i <= n:
		if not is_prime(n % i): return False
		i *= 10

	# truncate left to right:
	while n:
		if not is_prime(n): return False
		n //= 10
	
	return True

def is_prime(n):
	if n <= 1: return False
	elif n <= 3: return True
	elif n%2 == 0: return False
	for i in range(3, math.isqrt(n) + 1, 2):
		if n % i == 0: return False
	return True

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds")