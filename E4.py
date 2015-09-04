__author__ = 'shawnmehan'

""" two digit products 91*99 = 9009, largest palindrome of such multiples.
What is largest 3-digits palindrome
"""

import itertools

def get_list(n):
    l = []  # set up output list
    n_string = str(n)  # convert number to string
    for c in n_string:
        l.append(c)
    return l


def get_reverse_list(l):
    r = []  # set up output list
    for c in range(0,len(l)):  # flip the list
        r.append(l[-(c+1)])
    return r


def is_palindrome(l1, l2):
    if l1 == l2:
        return True
    else:
        return False


def largest_product():
    max_product = 0
    for i, j in itertools.product(range(1, 1000), range(1, 1000)):
        product = i * j
        if max_product > product:  # smaller than what we already found so skip
            continue
        front = get_list(product)
        back = get_reverse_list(front)
        if (is_palindrome(front, back)):
            max_product = product
    return max_product

print largest_product()
