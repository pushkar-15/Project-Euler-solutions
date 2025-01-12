def solve():
	divisor_sum = [0] * int(1e4)
	for i in range(1, len(divisor_sum)):
		for j in range(i * 2, len(divisor_sum), i):
			divisor_sum[j] += i

	ans = 0
	for x in range(1, len(divisor_sum)):
		y = divisor_sum[x]
		if x != y and y < len(divisor_sum) and divisor_sum[y] == x: # check if amicable
			ans += x
	return ans

if __name__ == "__main__":
	print(solve())