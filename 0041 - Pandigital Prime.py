import time, math

COMPOSITES = [0,2,4,6,8,9]

def solve():
	for n in range(7, 3, -1):
		a = [d for d in range(n, 0, -1)]
		while True:
			if a[-1] not in COMPOSITES:
				num = int("".join(str(x) for x in a))
				if is_prime(num): return num
			if not prev_permutation_exists(a): break

def prev_permutation_exists(a): # store a's previous permutation in a and return if it exists
	i = len(a) - 1
	while i >= 0 and a[i-1] <= a[i]: i -= 1
	if i == 0: return False
	j = len(a) - 1
	while a[i-1] <= a[j]: j -= 1
	a[i-1], a[j] = a[j], a[i-1]
	a[i : ] = a[len(a) - 1 : i - 1 : -1]
	return True

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

# n can not be in [1, 2, 8, 9] because all 8 and 9 pandigital numbers are divisible by 3.