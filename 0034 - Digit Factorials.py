from math import factorial, log10
import time

def solve():
	return sum(num for num in range(3, int(1e7)) if num == factorial_digit_sum(num))

def factorial_digit_sum(n):
	return sum(factorial(int(d)) for d in str(n))

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds") # 16.738316774368286 seconds
	
# Finding the upper limit for search space:
#   consider a n-digit number with all digits 9.
#   so, n * 9! <= number < 10^n (we need to find highest n satisfying this)
#   Hence by solving we get highest n = 7