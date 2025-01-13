# Brute Force

import itertools as it

def solve():
	digits = list(range(10))
	millionth_permutation = it.islice(it.permutations(digits), int(1e6 - 1), None)
	return "".join(str(d) for d in next(millionth_permutation))


if __name__ == "__main__":
	print(solve())