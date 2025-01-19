import time, math, itertools

def solve():
	for n in itertools.count():
		if n==0 or n==1 or n==143: continue
		H = n * (2*n - 1)
		if is_pentagonal(H):
			return H

def is_pentagonal(p):
	if p < 1: return False
	if math.isqrt(1 + 24 * p) ** 2 != 1 + 24 * p: return False
	if (1 + math.isqrt(1 + 24 * p)) % 6 == 0: return True
	return False

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds")

# Every Hexagonal number is also Triangular.
# Thus check only if the generated Hexagonal number is also Pentagonal.