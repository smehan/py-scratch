__author__ = 'shawnmehan'

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def test_divs(number, start, stop):
    no_remainder = [True]
    for n in range (start, stop):
        if number % n == 0:
            no_remainder.append(True)
        else:
            no_remainder.append(False)
    if no_remainder.__contains__(False):
        return False
    else:
        return True


def get_smallest(start, stop, ceiling):
    for s in range(1, ceiling):
        if test_divs(s, start, stop):
            return s
        else:
            continue


print get_smallest(1,20,100000000000)