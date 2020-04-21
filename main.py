import random
from binascii import unhexlify


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
def function1(chiffre):
    p, q = getPAndQ()
    while p == q or chiffre >= p * q:
        p, q = getPAndQ()
    n = p * q
    phiN = (p - 1) * (q - 1)
    e = 5
    return p, q, n, phiN, e


# compute the private key d
def getD(e, phiN):
    r, u, v, r1, u1, v1 = e, 1, 0, phiN, 0, 1
    while r1:  # while r1 !=0
        q = r // r1
        r, r1 = r1, r - q * r1  # r take r1 value
        u, u1 = u1, u - q * u1  # u take u1 value
        v, v1 = v1, v - q * v1  # v take v1 value
    return u % phiN


# encrypt message
def encrypt(chiffre, e, n):
    C = pow(chiffre, e, n)
    return C


# decrypt a message
def decrypt(C, d, n):
    M = pow(C, d, n)
    return M


# function of exercise 1
def exercise1():
    message = "110100110110111"
    chiffre = int(message, 2)  # convert the binary string to int

    p, q, n, phiN, e = function1(chiffre)
    while pgcd(e, phiN) != 1:  # pgcd(e, phiN) must be 1
        p, q, n, phiN, e = function1(chiffre)
    d = getD(e, phiN)
    print('p =', p, ' q =', q, 'n =', n, ' phiN =', phiN, ' e =', e, ' d =', d)
    print("#################")
    C = encrypt(chiffre, e, n)
    D = decrypt(C, d, n)
    print(message, 'equals to', chiffre, '(from binary string to int)')
    print(chiffre, 'encrypted equals to', C)
    '''print("Verification :")
    print(C, 'decrypted equals to', D)
    print(D, 'equals to', "{0:b}".format(D), '(from int to binary string)')  # "{0:b}".format(D) allows to convert int to binary'''


# get p and q with n
def factorisation(n):
    p = n - 2
    while n % p != 0:
        p = p - 2  # 2 by 2 -> faster
    q = int(n / p)
    return p, q


# function of exercise 2
def exercise2():
    ciphertext = 468
    n = 11
    e = 899
    p, q = factorisation(n)
    phiN = p*q
    d = getD(e, phiN)
    print('p =', p, 'q =', q, 'phiN =', phiN, 'd =', d)
    print('encrypted message :', ciphertext)
    M = decrypt(ciphertext, d, n)
    print('decrypted message :', M) 



'''
Exercise 5 :
Kp1 (493;3) | e1 = 3 | n1 = 493
Kp2 (493,5) | e2 = 5 | n2 = 493
You can say : c1 = pow(m,e1,n1) and c2 = pow(m,e2,n2)
Moreover gcd(e1,e2) = 1

Thanks to Bachet-Bézout, you can say : e1*u + e2*v = 1, Ǝ(u,v) ∈ ℤ²
<=> pow(c1,u) mod n + pow(c2,v) mod n   = ((pow(pow(m,e1),u)) mod n + (pow(pow(p,e2),v)) mod n) mod n 
                                        = pow(m,e1*u + e2*v) mod n
                                        = m mod n (e1*u + e2*v = 1)
                                        = m (m<=n)

We can conclude with : pow(c1,u) * pow(c2,v) = m mod n
                   <=> pow(293,u) * pow(421,v) = m mod 493
'''


def main():
    # exercise1()
    exercise2()


if __name__ == "__main__":
    main()
