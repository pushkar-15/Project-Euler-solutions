import time, math, itertools

def solve():
	for j in itertools.count(1):
		for k in range(1, j):
			Pj = (3*j-1)*j//2
			Pk = (3*k-1)*k//2
			if is_pentagonal(Pj + Pk) and is_pentagonal(abs(Pj - Pk)):
				return abs(Pj - Pk)

def is_pentagonal(p):
	if p < 1: return False
	if math.isqrt(1 + 24 * p) ** 2 != 1 + 24 * p: return False
	if (1 + math.isqrt(1 + 24 * p)) % 6 == 0: return True
	return False

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds")
