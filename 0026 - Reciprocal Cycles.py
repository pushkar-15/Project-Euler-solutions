def solve():
    def multiplicative_order(a, d):
        if gcd(a, d) != 1:
            return 0
        order = 1
        current = a % d
        while current != 1:
            current = (current * a) % d
            order += 1
        return order
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # primes = list(primerange(1, 1000))  # Generate all primes below 1000 (more efficient to iterate p over prime numbers only)
    primes = range(2, 1000)
    
    max_length = 0
    result = 0
    
    for p in primes:
        cycle_length = multiplicative_order(10, p)
        if cycle_length > max_length:
            max_length = cycle_length
            result = p
    
    return str(result)

if __name__ == "__main__":
    print(solve())


# By solving, we get:
# Answer is the smallest k which satisfies 	10^k ≣ 1 (mod d)
# (this is called the multiplicative order of 10 in the field of d)
# We search only for primes because non-prime numbers tend to have shorter repeating cycles because their reciprocals reduce to simpler fractions.