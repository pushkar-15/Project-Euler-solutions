import time

def is_double_base_palindromic(n):
    base10 = str(n) == str(n)[::-1]
    base2 = str(bin(n)[2:]) == str(bin(n)[2:])[::-1]
    return base10 and base2

def solve():
    return sum(number for number in range(1, int(1e6), 2) if is_double_base_palindromic(number))

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds")