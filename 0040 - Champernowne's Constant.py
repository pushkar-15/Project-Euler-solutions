import time

def solve():
	s = "".join(str(n) for n in range(int(1e7))) # s[i] = ith character (1-based indexing because s starts with '0')
	ans = 1
	for i in range(7):
		ans *= int(s[10**i])
	return ans

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds")