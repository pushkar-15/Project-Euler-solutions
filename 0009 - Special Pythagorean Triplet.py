# Brute Force

def solve():
    triplet = [(x,y,1000-x-y) for x in range(1,1000) for y in range(1,x) if x**2 + y**2 == (1000-x-y)**2]
    ans = 1
    for x in triplet[0]:
        ans *= x
    return ans

if __name__ == "__main__":
    print(solve())