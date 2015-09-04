__author__ = 'shawnmehan'
"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 - 6857
"""
import math

number = 600851475143
cf = [1]

for n in range(2,math.trunc(math.sqrt(number))):
    if number % n == 0:
        cf.append(n)

pf = list(cf)
for n in range(1,len(cf)):
    for m in range(1,len(pf)):
        if cf[-n] % cf[m] == 0 and cf[-n] != cf[m]:
            pf.remove(cf[-n])
            break

print "Max is: ", pf[-1]

""" alternative is to build up factors"""

newNumber = number
largestFactor = 0
n = 2

while n*n <= newNumber:
    if newNumber % n == 0:
        newNumber = newNumber / n
        largestFactor = n
    else:
        n += 1
if newNumber > largestFactor: # remainder is a prime number
    largestFactor = newNumber

print "Largest Prime Factor is: ", largestFactor
