import time, math

def sieve_of_eratosthenes(n):
	is_prime = [True] * (n + 1)
	is_prime[0] = is_prime[1] = False
	
	for i in range(math.isqrt(n) + 1):
		if is_prime[i]:
			for j in range(i*i, len(is_prime), i):
				is_prime[j] = False
	return is_prime

def solve():
	is_prime = sieve_of_eratosthenes(int(1e6))

	def is_circular_prime(n):
		s = str(n)
		return all(is_prime[int(s[i:] + s[:i])] for i in range(len(s)))
	
	return sum(1 for num in range(len(is_prime)) if is_circular_prime(num))

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds")