# Cracking Codes with Python: An Introduction to Building and Breaking Ciphers
# Al Sweigart
# http://inventwithpython.com/cracking/chapter13.html
def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None  # No mod inverse if a & m aren't relatively prime.
    u1, u2, u3 = 1, 0, a
    # v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # Note that // is the integer division operator.
        v1, v2 = (u1 - q * v1), (u2 - q * v2)
    return u1 % m

# Cracking Codes with Python: An Introduction to Building and Breaking Ciphers
# Al Sweigart
# http://inventwithpython.com/cracking/chapter13.html
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
