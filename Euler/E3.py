__author__ = 'shawnmehan'
"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143
"""
import math

number = 13195
cf = [1]
for n in range(2,number/2):
    if number % n == 0:
        cf.append(n)

pf = list(cf)
for n in range(1,len(cf)):
    reverse_i = len(cf) - n
    print "Hey", cf[-n], reverse_i
    for m in range(1,len(pf)):
        if cf[-n] % cf[m] == 0 and cf[-n] != cf[m]:
            del pf[-1]
            break

for e in pf:
    print e