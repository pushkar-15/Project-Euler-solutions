# Sieve of Eratosthenes

def solve():
    marked = [0] * int(2e6)
    value = 3
    s = 2

    while value < int(2e6):
        if marked[value] == 0:
            s += value
            i = value
            while i < 2e6:
                marked[i] = 1
                i += value
        value += 2
    
    return s

if __name__ == "__main__":
    print(solve())