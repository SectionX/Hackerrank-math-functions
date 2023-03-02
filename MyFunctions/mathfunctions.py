

def fastpow(x,y):

    '''Calculates powers at O(logn)
       Doesn't work with fractions
       negatives.'''

    ans=1
    while y>0 :
        if y&1==1:
            ans=ans*x
        x=x*x
        y>>=1
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
    operations.
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


if __name__ == '__main__':

    n, m = 524645, 379018
    a = n+m -1
    assert modcombinations(a - 1, m - 1, 10**9+7) == 470983035
    input()
