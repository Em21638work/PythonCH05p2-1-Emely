
def is_prime(n):
    i = 2
    notprime = 0
    result = False
    while i < n:
        if n % i == 0:
            notprime += 1
            break
        i += 1
    if notprime >= 1:
        result = False
    elif notprime == 0:
        result = True
    return result

def print_primes(n):
    allprime = []
    allprime.append(get_primes(n))
    print(allprime)
    
def get_primes(n):
    myprime = []
    i = 2
    result = False
    while i <= n:
        result = is_prime(i)
        if result == True:
            myprime.append(i)
        i += 1 
    return myprime