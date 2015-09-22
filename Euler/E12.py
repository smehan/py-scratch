__author__ = 'shawnmehan'

"""Class to calculte the triangle numbers and then determine how many divisors they have.
Objective is to find first triangle number with > 500 divisors"""


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


def get_divisors2(n):
    divisors = []
    for d in range(1, n):
        """If d is in the list, we have crossed the half-way point and can stop"""
        if d in divisors:
            break
        """Otherwise, test to see if a divisor, and then add both to set"""
        if n % d == 0:
            r = n / d
            divisors.append(d)
            divisors.append(r)
    return sorted(divisors)


tri_sum = 0
tri_sum_divs = 0
for i in range(6000):
    tri_sum += i+1
    tri_sum_divs = get_divisors2(tri_sum)
    if len(tri_sum_divs) > 300:
        print "Close: %dth triangle number, %d, has length: %d" % (i, tri_sum, len(tri_sum_divs))
    if len(tri_sum_divs) > 500:
        print i
        break

print tri_sum, len(tri_sum_divs), tri_sum_divs


