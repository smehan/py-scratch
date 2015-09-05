__author__ = 'shawnmehan'

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def test_divs(number, start, stop):
    no_remainder = [True]
    for n in range(start, stop):
        if number % n == 0:
            no_remainder.append(True)
        else:
            no_remainder.append(False)
    if no_remainder.__contains__(False):
        return False
    else:
        return True


def get_smallest2(step):
    i = step
    while (i % 2 != 0 or i % 3 != 0 or i % 4 != 0 or i % 5 != 0 or
         i % 6 != 0 or i % 7 != 0 or i % 8 != 0 or i % 9 != 0 or
         i % 10 != 0 or i % 11 != 0 or i % 12 != 0 or i % 13 != 0 or
         i % 14 != 0 or i % 15 != 0 or i % 16 != 0 or i % 17 != 0 or
         i % 18 != 0 or i % 19 != 0 or i % 20 != 0):
        i += step
    return i


def get_smallest(start, stop, ceiling):
    for s in range(1, ceiling):
        if test_divs2(s, start, stop):
            return s
        elif s % 100000 == 0:
            print "...{:d}...".format(s)
        else:
            continue


def get_smallest3():
    """ And then we have this, which is amazingly efficient and can scale much higher than
            the naive implementation
    """
    from fractions import gcd
    return reduce(lambda x, y: x*y//gcd(x, y), range(1, 101))

print get_smallest3()
