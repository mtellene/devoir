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
    p = random.randint(1, (pow(2, 8)) - 1)  # random int between 1 and 2⁸-1
    q = random.randint(1, (pow(2, 8)) - 1)  # random int between 1 and 2⁸-1
    while not isPrime(p):  # while p is not prime
        p = random.randint(1, (pow(2, 8)) - 1)
    while not isPrime(q):  # while q is not prime
        q = random.randint(1, (pow(2, 8)) - 1)
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
def inv_mod(e, phiN, nbReturn):
    r, u, v, r1, u1, v1 = e, 1, 0, phiN, 0, 1
    while r1:  # while r1 !=0
        q = r // r1
        r, r1 = r1, r - q * r1  # r take r1 value
        u, u1 = u1, u - q * u1  # u take u1 value
        v, v1 = v1, v - q * v1  # v take v1 value
    if nbReturn == "1":
        return u % phiN
    elif nbReturn == "2":
        return u % phiN, v


# encrypt message
def encrypt(chiffre, e, n):
    C = pow(chiffre, e, n)
    return C


# decrypt a message
def decrypt(C, d, n):
    M = pow(C, d, n)
    return M


# get p and q with n
def factorisation(n):
    p = n - 2
    while n % p != 0:
        p = p - 2  # 2 by 2 -> faster
    q = int(n / p)
    return p, q


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
    print('-------------------------------------------')
    print('Chinese Remainder Theorem :')
    print('X = [a1*m1*pow(M1,-1) + a2*m2*pow(M2,-1) + a3*m3*pow(M3,-1)] mod n1*n2*n3')
    print('Thanks to this theorem we can say that :')
    print('c = pow(m,e)')
    print('<=> c = X')
    print('<=> X = pow(m,e)')
    print('<=> m = pow(X,1.0/e)')
    print('-------------------------------------------')
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
    Nm1 = (inv_mod(Nm1, n1, "1"))
    Nm2 = (inv_mod(Nm2, n2, "1"))
    Nm3 = (inv_mod(Nm3, n3, "1"))
    print('X = [', c1, '*', m1, '*', Nm1, '+', c2, '*', m2, '*', Nm2, '+', c3, '*', m3, '*', Nm3, '] mod', n1 * n2 * n3)
    a1, a2, a3 = c1 * m1 * Nm1, c2 * m2 * Nm2, c3 * m3 * Nm3
    print('X = [', a1, '+', a2, '+', a3, '] mod', modGene)
    print('X =', a1 + a2 + a3, 'mod', modGene)
    X = pow(a1 + a2 + a3, 1, modGene)
    print('X =', X)
    print('-------------------------------------------')
    print('We said that :')
    print('X = pow(m,3)')
    print('<=> pow(m,3) =', X)
    print('<=> m = pow(X,1.0/e)')
    print('<=> m = pow(', X, ', 1.0/', e, ')')
    m = pow(X, 1.0 / e)
    print('<=> m =', m)
    print('<=> m =', round(m))


# function for exercise 5
def exercise5():
    n = 493
    e1, e2 = 3, 5
    c1, c2 = 293, 421
    print('Kp1 (', n, ';', e1, ') | e1 =', e1, 'n =', n, '| c1 =', c1)
    print('Kp2 (', n, ';', e2, ') | e2 =', e2, 'n =', n, ' | c2 =', c2)
    print('-------------------------------------------')
    if pgcd(e1, e2) != 1:
        print('Désolé impossible...')
        return
    print('Bachet-Bézout :')
    print('e1*u + e2*v = 1')
    print('-------------------------------------------')
    print('We know :')
    print('c1 = pow(m,e1,n1) | c2 = pow(m,e2,n2)')
    print('m = (pow(c1,u) * pow(c2,u)) mod n')
    print('<=> m = (pow(m,e1*u) * pow(m,e2,v)) mod n')
    print('<=> m = pow(m,e1*u + e2*v) mod n')
    print('<=> m = pow(m,1) mod n   # e1*u + e2*v = 1')
    print('<=> m = m                # (m<=n)')
    print('-------------------------------------------')
    print('Now we know u, v and m = (pow(c1,u) * pow(c2,v)) mod n')
    print('So we can compute m')
    print('m = (pow(c1,u) * pow(c2,v)) mod n')
    u, v = inv_mod(e1, e2, "2")
    print('m = (pow(', c1, ',', u, ') * pow(', c2, ',', v, ')) mod', n)
    x = inv_mod(c2, n, "1")  # pow(c2,v) because v = -1
    print('m = (pow(', c1, ',', u, ') *', x, ') mod', n)
    y = pow(c1, u)
    print('m = (', y, '*', x, ') mod', n)
    print('m =', x * y, 'mod', n)
    print('m =', pow(x * y, 1, n))


def main():
    # exercise4()
    exercise5()


if __name__ == "__main__":
    main()
