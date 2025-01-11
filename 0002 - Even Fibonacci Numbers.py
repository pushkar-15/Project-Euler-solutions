# Obseravtion: Every third Fibonacci number is even
# 0, 1, 1, 2, 3, 5, 8, ...
# x, y, x+y, x+2y, 2x+3y, 3x+5y, 5x+8y, ...
# E(n) = 4*E(n-1) + E(n-2)

# (alternative solution: use Binet's formula)

def solve():
    a, b, ans = 0, 2, 0
    while b <= 4e6:
        a, b, ans = b, a + 4*b, ans + b
    return ans

if __name__ == "__main__":
    print(solve())