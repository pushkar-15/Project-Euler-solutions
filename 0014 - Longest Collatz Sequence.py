# Recursive DP by caching

import functools

@functools.cache
def collatz_chain_length(x):
	if x == 1: return 1
	if x % 2 == 0: return 1 + collatz_chain_length(x // 2)
	else: return 1 + collatz_chain_length(3 * x + 1)

def solve():
	ans = max(range(1, 1000000), key=collatz_chain_length)
	return str(ans)

if __name__ == "__main__":
	print(solve())