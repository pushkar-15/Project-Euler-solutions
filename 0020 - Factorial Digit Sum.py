from math import factorial

def solve():
    return sum([int(d) for d in str(factorial(100))])

if __name__ == "__main__":
	print(solve())