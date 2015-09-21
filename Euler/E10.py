__author__ = 'shawnmehan'

"""Find sum of P_n < L"""

from GetPrimes import *


def get_sum_primes(ceiling):
    """
    Computes sum of primes P_i with P_n < ceiling
    :param ceiling: ceiling limit under which all P_i must remain
    :return: Sum of all valid primes
    """
    allPrimes = rwh_primes(ceiling)
    total = 0
    for n in allPrimes:
        total += n
    return total, len(allPrimes)

total, count = get_sum_primes(2000000)
print "Sum of first ",count, " primes is: ", total
