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
def function1(chiffre):
    p, q = getPAndQ()
    while p == q or chiffre >= p * q:
        p, q = getPAndQ()
    n = p * q
    phiN = (p - 1) * (q - 1)
    e = 5
    return p, q, n, phiN, e


# compute the private key d
def inv_mod(e, phiN):
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
    d = inv_mod(e, phiN)
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
    phiN = p * q
    d = inv_mod(e, phiN)
    print('p =', p, 'q =', q, 'phiN =', phiN, 'd =', d)
    print('encrypted message :', ciphertext)
    M = decrypt(ciphertext, d, n)
    print('decrypted message :', M)


'''
Exercise 4 :
Kp1 (391;3) | e1 = 3 | n1 = 391 | c1 = 208  
Kp2 (55;3)  | e2 = 3 | n2 = 55  | c2 = 38
Kp3 (87;3)  | e3 = 3 | n3 = 87  | c3 = 32
-------------------------------------------
We know that :
c1 = pow(m,e1,n1) <=> 208 = pow(m,3,391)
c2 = pow(m,e2,n2) <=> 38 = pow(m,3,55)
c3 = pow(m,e3,n3) <=> 32 = pow(m,3,87)
-------------------------------------------
Chinese Reminder Theorem :
X ≡ 
    x1 = a1 mod M1
    x2 = a2 mod M2
    x3 = a3 mod M3
X = [a1*m1*pow(M1,-1) + a2*m2*pow(M2,-1) + a3*m3*pow(M3,-1)] mod n1*n2*n3
-------------------------------------------
In our case : 
c1 = pow(m,3,n1)
c2 = pow(m,3,n2)
c3 = pow(m,3,n3)

<=> c = pow(m,3) 
<=> X = c
<=> X = pow(m,3)
<=> m = pow(X,1.0/3.0) (message equals to cube root of X)

m1 = n2*n3 | m2 = n1*n3 | m3 = n1*n2
M1 = m1 mod n1 | M2 = m2 mod n2 | M3 = m3 mod n3

X = [c1*m1*pow(M1,-1) + c2*m2*pow(M2,-1) + c3*m3*pow(M3,-1)] mod n1*n2*n3
<=> X = [208*4785*pow(4785,-1,391) + 38*34017*pow(34017,-1,55) + 32*21505*pow(21505,-1,87)] mod 1870935
<=> X = [208*4785*pow(93,-1,391) + 38*34017*pow(27,-1,55) + 32*21505*pow(16,-1,87)] mod 1870935

pow(93,-1,391) = 185
pow(27,-1,55) = 53
pow(16,-1,87) = 49

<=> X = [208*4785*185 + 38*34017*53 + 32*21505*49] mod 1870935
<=> X = [184126800 + 68510238 + 33719840] mod 1870935
<=> X = 286356878 mod 1870935
<=> X = 103823

We said : m = pow(X,1.0/3.0) 
<=> m = pow(103823,1.0/3.0) 
<=> m = 47
'''


# get a round of n
def round(n):
    if n - int(n) < 0.5:
        n = int(n)
    else:
        n = int(n) + 1
    return n


# n mod M
def nModM(m, n):
    x = m / n
    peX = int(x)
    Nx = x - peX
    x = Nx * n
    x = round(x)
    return x


# function for exercise 4
def exercise4():
    e = 3
    n1, n2, n3 = 391, 55, 87
    c1, c2, c3 = 208, 38, 32
    print('Kp1 (', n1, ';', e, ') | e =', e, 'n1 =', n1, '| c1 =', c1)
    print('Kp2 (', n2, ';', e, ') \t| e =', e, 'n2 =', n2, ' | c2 =', c2)
    print('Kp3 (', n3, ';', e, ') \t| e =', e, 'n3 =', n3, ' | c3 =', c3)
    print('--------------------------')
    print('Chinese Reminder Theorem :')
    print('X = [a1*m1*pow(M1,-1) + a2*m2*pow(M2,-1) + a3*m3*pow(M3,-1)] mod n1*n2*n3')
    print('Thanks to this theorem we can say that :')
    print('c = pow(m,e)')
    print('<=> c = X')
    print('<=> X = pow(m,e)')
    print('<=> m = pow(X,1.0/e)')
    print('--------------------------')
    m1, m2, m3, modGene = n2 * n3, n1 * n3, n1 * n2, n1 * n2 * n3
    print('m1 =', m1, '; m2 =', m2, '; m3 =', m3)
    print('X = [', c1, '*', m1, '*pow(', m1, ',-1,', n1, ') + ', c2, '*', m2, '*pow(', m2, ',-1,', n2, ') + '
          , c3, '*', m3, '*pow(', m3, ',-1,', n3, ')] mod', modGene)
    Nm1 = nModM(m1, n1)
    while Nm1 > n1:
        Nm1 = nModM(m1, n1)
    Nm2 = nModM(m2, n2)
    while Nm2 > n2:
        Nm2 = nModM(m2, n2)
    Nm3 = nModM(m3, n3)
    while Nm3 > n3:
        Nm3 = nModM(m3, n3)
    print('X = [', c1, '*', m1, '*pow(', Nm1, ',-1,', n1, ') + ', c2, '*', m2, '*pow(', Nm2, ',-1,', n2, ') + '
          , c3, '*', m3, '*pow(', Nm3, ',-1,', n3, ')] mod', modGene)
    Nm1 = (inv_mod(Nm1, n1))
    Nm2 = (inv_mod(Nm2, n2))
    Nm3 = (inv_mod(Nm3, n3))
    print('X = [', c1, '*', m1, '*', Nm1, '+', c2, '*', m2, '*', Nm2, '+', c3, '*', m3, '*', Nm3, '] mod', n1 * n2 * n3)
    a1, a2, a3 = c1 * m1 * Nm1, c2 * m2 * Nm2, c3 * m3 * Nm3
    print('X = [', a1, '+', a2, '+', a3, '] mod', modGene)
    print('X =', a1 + a2 + a3, 'mod', modGene)
    X = pow(a1 + a2 + a3, 1, modGene)
    print('X =', X)
    print('--------------------------')
    print('We said that :')
    print('X = pow(m,3)')
    print('<=> pow(m,3) =', X)
    print('<=> m = pow(X,1.0/e')
    print('<=> m = pow(', X, '1.0/', e, ')')
    m = pow(X, 1.0 / e)
    print('<=> m =', m)
    print('<=> m =', round(m))


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
    # exercise2()
    exercise4()


if __name__ == "__main__":
    main()
