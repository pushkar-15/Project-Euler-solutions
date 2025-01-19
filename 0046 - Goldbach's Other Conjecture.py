import time, math, itertools

def solve():
	for n in itertools.count(9, 2):
		if not is_prime(n) and not can_goldbach(n):
			return n

def can_goldbach(n):
	for k in itertools.count(1):
		if is_prime(n - 2*k**2): return True
		if n - 2*k**2 <= 0: return False
			
def is_prime(n):
	if n <= 0 or n == 1 or n % 2 == 0 : return False
	if n <= 3: return True
	for i in range(3, math.isqrt(n) + 1, 2):
		if n % i == 0: return False
	return True

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds")