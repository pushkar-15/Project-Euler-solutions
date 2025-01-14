# Brute Force

from math import isqrt

def is_unusual(n):
	for d in range(1, isqrt(n) + 1):
		if n % d == 0:
			if "123456789" == "".join(sorted(str(d) + str(n // d) + str(n))):
				return True
	return False

def solve():
	return sum(i for i in range(1, int(1e4)) if is_unusual(i))

if __name__ == "__main__":
	print(solve())