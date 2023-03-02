import math


def changebaseto10(int, base):
    sm = 0
    n = list(map(int, list(str(n)[::-1])))
    for y, i in enumerate(n):
        sm += i * (base ** y)
    return sm


def changebase10tonewbase(int, base):

    bn = ''
    while n > 0:
        bn += str(n % base)
        n //= base
    bn = bn[::-1]
    return int(bn)

def pythagorean(x, y):
    return math.sqrt(x**2 + y**2)

def isFibo(n):
     return math.sqrt(5*n**2+4) % 1 == 0 or  math.sqrt(5*n**2-4) % 1 == 0



def complexmultiplication(complex1, complex2):

    '''Complex multiplication with very high numbers
    returns NaN due to float type. This algorithm is
    to be used with python integer tuples.'''

    x1 = complex1[0]
    x2 = complex2[0]
    y1 = complex1[1]
    y2 = complex2[1]
    return (x1*x2 - y1*y2) % m, (x1*y2 + y1*x2) % m


def gcd(x, y):

    '''Eucleides's algorithm'''

    if y == 0:
        return x
    return gcd(y, x % y)


def fastpow(x,y):

    '''Calculates powers at O(logn)
       Doesn't work with fractions,
       negatives.

       Russian Peasant Algorithm'''

    ans = 1
    while y > 0 :
        if y & 1 == 1:
            ans = ans * x
        x = x * x
        print(x)
        y >>= 1
    return ans




def modfastpow(x, y, q):

    '''
    To be used with modulo inversions
    '''

    result = 1
    while y > 0:
        if y & 1 == 1:
            result = result * x % q
        x = x * x % q
        y >>= 1
    return result



def modfactorial(n, p):

    '''
    Calculates factorials with modulo
    operations. Based on Wilson's Theorem
    '''

    result = 1
    for i in range(1, n+1):
        result = result * i % p
    return result


def modfactorialinverted(n, p):

    '''
    Calculates the inverse factorial
    with modulo operations. Based on
    Fermat's little theorem.
    '''

    result = modfactorial(n, p)
    return modfastpow(result, p-2, p)


def modcombinations(n, r, modl):

    '''
    Combinations formula to be used with
    modulo inversions.
    '''

    k = n - r
    n = modfactorial(n, modl)
    r = modfactorialinverted(r, modl)
    k = modfactorialinverted(k, modl)
    return n*r*k % modl



def matrixmultiplication(A, B):
    # Check for validity
    if len(B) != len(B):
        print("Wrong Dimensions")
    result = []

    for i in range(len(A)):
        smlist = []
        for z in range(len(B[0])):
            sm = 0
            for y in range(len(A[0])):
                sm += A[i][y] * B[y][z]
            smlist.append(sm)
        result.append(smlist)

    return result


def fastmatrixexpo(base, power):

    #set result to 1
    result = []
    tmp = []
    for i in range(len(base)):
        tmp = []
        for y in range(len(base)):
            tmp.append(0) if i != y else tmp.append(1)
        result.append(tmp)

    while power > 0:
         if power & 1 == 1:
             result = matrixmultiplication(result, base)
         base = matrixmultiplication(base, base)
         power >>= 1

    return result


'''
def matrixoperationsechelon()
for a in range(1,20):

    matrix = [
        [a,1,2],
        [1,2,1],
        [2,1,a]
    ]


    for i in range(2):
        for z in range(1,3-i):
            r = matrix[i+z][i] / matrix[i][i]
            for j in range(3):
                matrix[i+z][j] -= matrix[i][j] * r

    if sum(matrix[2]) == 0:
        print(a)

for a system to have no solution, we have to prove that 0 == some constant
for eigen values we calculate |A-λΙ| = 0
for eigen vectors we calculate (A-λ)v = 0 for each solution λ

        '''
