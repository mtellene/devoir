import random


# true if a number is prime, false otherwise
def isPrime(n):
    number = int(n)
    i = 2
    while i < number and number % i != 0:
        i = i + 1
    if i == number:  # if i = number
        return True
    else:  # if number % i = 0
        return False


# get pgcd between 2 numbers
def pgcd(a, b):
    if b == 0:  # compare a and nothing
        return a
    else:
        r = a % b  # r = a mod b
        return pgcd(b, r)


# generate 2 8-bits prime numbers
def getPAndQ():
    p = random.randint(1, pow(2, 8))  # random int between 1 and 2⁸
    q = random.randint(1, pow(2, 8))  # random int between 1 and 2⁸
    while not isPrime(p):  # while p is not prime
        p = random.randint(1, pow(2, 8))
    while not isPrime(q):  # while q is not prime
        q = random.randint(1, pow(2, 8))
    return p, q


# get p and q and find n, phiN and e
def function1():
    p, q = getPAndQ()
    while p == q:
        print(p, '==', q)
        p, q = getPAndQ()
    n = p * q
    phiN = (p - 1) * (q - 1)
    e = 5
    return p, q, n, phiN, e


def exercise1():
    p, q, n, phiN, e = function1()
    while pgcd(e, phiN) != 1:   # pgcd(e, phiN) must be 1
        print("FALSE")
        p, q, n, phiN, e = function1()
    print('p =', p, ' q =', q, 'n =', n, ' phiN =', phiN, ' e =', e)


def main():
    exercise1()


if __name__ == "__main__":
    main()
