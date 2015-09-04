import math

__author__ = 'shawnmehan'

"""If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_sum_multiples(n):
    s = 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s


def get_sum_geometric(n, t):
    return n*(t/n)*((t/n)+1)/2

print(get_sum_multiples(1000))
print(get_sum_geometric(3,1000-1)+get_sum_geometric(5,1000-1)-get_sum_geometric(15,1000-1))




