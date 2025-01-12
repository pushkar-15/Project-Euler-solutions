from math import factorial

def solve():
	return int(factorial(40) / (factorial(20) * factorial(20)))

if __name__ == "__main__":
	print(solve())