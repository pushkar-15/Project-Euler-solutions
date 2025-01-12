def solve():
    n = 100
    square_of_sum = (n * (n + 1) / 2) ** 2
    sum_of_squares = (n / 6) * (2*n + 1) * (n + 1)
    return abs(sum_of_squares - square_of_sum)

if __name__ == "__main__":
    print(solve())