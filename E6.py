__author__ = 'shawnmehan'

""" 2640 for N = 10"""

""" geometric sum (1 + 2 + ... + N) = N*(N+1)/2 """

def get_square_sum(n):
    sum = n*(n+1)/2
    square_sum = sum**2
    return square_sum

def get_sum_squares(n):
    sum_squares = 0
    for i in range(1,n+1):
      sum_squares += i**2
    return sum_squares

n = 10000000
print "Difference for N=", n, " is :", get_square_sum(n) - get_sum_squares(n)

