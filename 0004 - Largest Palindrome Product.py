# m * n == xyz * abc == pqrqp or pqrrqp == Product
# Product is a factor of 11, so atleast m or n is a factor of 11.

def isPalindrome(s):
    p, q = 0, len(s) - 1
    while p < q:
        if s[p] != s[q]: return False
        p, q = p + 1, q - 1
    return True

def solve():
    a = 999
    largestPalindromeProduct = 0

    while a >= 100:
        if a % 11 == 0: b, db = 999, 1 # a is a multiple of 11
        else: b, db = 990, 11 # b is a multiple of 11

        while b >= a:
            if a * b <= largestPalindromeProduct: break
            if isPalindrome(str(a * b)): largestPalindromeProduct = a * b
            b -= db

        a -= 1
    
    return largestPalindromeProduct


if __name__ == "__main__":
    print(solve())