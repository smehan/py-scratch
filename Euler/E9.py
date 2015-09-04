import math

__author__ = 'shawnmehan'

""" a<b<c, a^2+b^2=c^2, a+b+c=1000, return a*b*c
"""


def pythag_triplet():
    for a in range(1, 500):
        for b in range(a+1, 500):
            c = math.sqrt(a**2+b**2)
            if (a+b+c == 1000):
                return (a*b*c)

print(pythag_triplet())