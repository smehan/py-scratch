__author__ = 'shawnmehan'

"""Class to calculte the triangle numbers and then determine how many divisors they have.
Objective is to find first triangle number with > 500 divisors"""

from fractions import gcd

def get_sum_next_tri_num(n, s):
    s += n
    return s

def get_divisors(n):
    divisors = []
    if n % 2 != 0:
        divisors.append(2)
        divisors.append(n % 2)
    if n % 3 != 0:
        divisors.append(3)
        divisors.append(n % 3)
    for d in range(4, n/4):
        if n % d == 0:
            divisors.append(d)
    divisors.append(n)
    return sorted(divisors)


tri_sum = 0
for i in range(4000):
    tri_sum += i+1
    tri_sum_divs = get_divisors(tri_sum)
    if len(tri_sum_divs) > 500:
        print i
        break

print tri_sum,len(tri_sum_divs), tri_sum_divs


