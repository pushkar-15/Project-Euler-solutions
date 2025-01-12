import math

def solve():
    return math.lcm(*[x for x in range(1,21)])

if __name__ == "__main__":
    print(solve())

# can be further improved