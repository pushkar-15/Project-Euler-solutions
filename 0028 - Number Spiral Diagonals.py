def solve():
    n = 500     # 2n+1 = 1001
    return int(8*n*(n+1)*(2*n+1)/3 + 2*n*(n+1) + 4*n + 1)

if __name__ == "__main__":
    print(solve())

# The spiral always has odd dimensions: 2n+1 * 2n+1
# For this, the corners are:
    # top left = n^2-n+1
    # top right = n^2
    # bottom left = n^2-2n+2
    # bottom right = n^2-3n+3
# Hence, the sum of diagonals is 8n(n+1)(2n+1)/3 + 2n(n+1) + 4n + 1