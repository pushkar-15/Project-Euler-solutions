def sum_divisible_by(n):
    last = 999 // n
    return n * last * (last + 1) // 2

def solve():
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)

if __name__ == "__main__":
    print(solve())