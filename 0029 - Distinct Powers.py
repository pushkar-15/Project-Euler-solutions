# Brute Force

def solve():
    return len(set(a**b for a in range(2, 101) for b in range(2, 101)))

if __name__ == "__main__":
    print(solve())