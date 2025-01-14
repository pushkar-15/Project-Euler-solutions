def solve():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200

    ways = [0] * (target + 1) # ways[i] = ways to create amount i (order does not matter)
    ways[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
    
    return ways[-1]

if __name__ == "__main__":
    print(solve())