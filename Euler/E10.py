__author__ = 'shawnmehan'

"""Find sum of P_n < L"""

from GetPrimes import *


def get_sum_primes(ceiling):
    """
    Computes sum of primes P_i with P_n < ceiling
    :param ceiling: ceiling limit under which all P_i must remain
    :return: Sum of all valid primes
    """
    total = 0
    count = 1
    flag = True
    while flag:
        nextPrime = rwh_primes(count)
        if nextPrime[-1] < ceiling:
            total += nextPrime[-1]
            count += 1
        else:
            flag = False
        if count % 10000 == 0:
            print "...{:d}...".format(count)
    return total

print "Sum of primes is: ", get_sum_primes(2000000)
