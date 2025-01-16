import time

def solve():
	return max(range(1, 1001), key=number_of_solutions)

def number_of_solutions(p):
	result = 0
	for a in range(1, p // 2 + 1):
		for b in range(a, p // 2 + 1):
			c = p - a - b
			if a * a + b * b == c * c:
				result += 1
	return result

if __name__ == "__main__":
	s = time.time()
	print(solve())
	print(time.time() - s, "seconds") # 5.759488344192505 seconds