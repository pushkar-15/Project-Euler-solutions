# Brute Force

LIMIT = 28124

def solve():
	divisor_sum = [0] * LIMIT
	for i in range(1, LIMIT):
		for multiple in range(i*2, LIMIT, i):
			divisor_sum[multiple] += i
	abundants = [num for (num, sum) in enumerate(divisor_sum) if sum > num]
	
	is_expressible = [False] * LIMIT
	for i in abundants:
		for j in abundants:
			if i + j < LIMIT:
				is_expressible[i + j] = True
	
	return sum([num for num in range(LIMIT) if is_expressible[num] == False])


if __name__ == "__main__":
	print(solve())