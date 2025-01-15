def solve():
	numerator, denominator = 1, 1
	for d in range(10, 100):
		for n in range(10, d):
			n0, n1 = n // 10, n % 10
			d0, d1 = d // 10, d % 10
			if (n0 == d1 and n1 * d == n * d0) or (n1 == d0 and n0 * d == n * d1):
				numerator *= n
				denominator *= d
	return denominator // gcd(numerator, denominator)

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

if __name__ == "__main__":
	print(solve())

# n / d = (10n0 + n1) / (10d0 + d1)
# case 1: n1 = d1 which by solving implies n0 = d0 (not allowed, so discard the case)
# case 2: n0 = d0 which by solving implies n1 = d1 (not allowed, so discard the case)
# case 3: n0 = d1 implies n1 / d0 = n / d
# case 4: n1 = d0 implies n0 / d1 = n / d