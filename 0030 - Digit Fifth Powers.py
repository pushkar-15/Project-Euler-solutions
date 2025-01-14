# Brute Force

def solve():
    def satisfies(n):
        return n == sum(int(c) ** 5 for c in str(n))
    
    return sum(n for n in range(2, int(1e6)) if satisfies(n))

if __name__ == "__main__":
    print(solve())

# Finding the upper limit for our search space:
# n * 9^5 > 10^n for n==6
# Hence, the number is atmost 6 digits