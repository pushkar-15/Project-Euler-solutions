import time

def solve():
	ans = 0
	for n in range(2, 10):
		for i in range(1, 10 ** (9 // n)):
			s = "".join(str(i*j) for j in range(1, n+1))
			if "123456789" == "".join(sorted(s)):
				ans = max(ans, int(s))
	return ans

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds")

# Finding upper limit for i:
# s = str(1*i) + str(2*i) + str(3*i) + ... + str(n*i)
# if i contains d digits, then s contains approximately n*d digits
# n*d <= 9 (given condition)
# Hence, d = floor(9/n)