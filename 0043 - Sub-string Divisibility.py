import time, itertools

def solve():
	return sum(int("".join(map(str, num)))
		for num in itertools.permutations(list(range(10)))
		if is_substring_divisible(num))


DIVISIBILITY_TESTS = [2, 3, 5, 7, 11, 13, 17]

def is_substring_divisible(num):
	return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % d == 0
		for (i, d) in enumerate(DIVISIBILITY_TESTS))

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds") # 2.7456960678100586 seconds

