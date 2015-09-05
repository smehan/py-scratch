__author__ = 'shawnmehan'
"""Class to get Nth prime"""


def get_primes(n):
    primefac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primefac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primefac.append(n)
    return primefac


def get_nth_prime(nth):
    primes = []
    i = 2
    while len(primes) < nth:
        out = get_primes(i)
        if primes.count(out[-1]) == False:
            primes.append(out[-1])
        i += 1
    return primes

print "Nth prime is: ", get_nth_prime(10001)[-1]
