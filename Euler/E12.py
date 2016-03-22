__author__ = 'shawnmehan'

"""Class to calculte the triangle numbers and then determine how many divisors they have.
Objective is to find first triangle number with > 500 divisors"""


import math, time
ti = time.time()


def nofactors2(num):
    count = 0
    x = math.sqrt(num)
    y = int(math.ceil(x))
    if x - y == 0:
        count = 1
    count += 2*len(filter(lambda a:num % a == 0, range(1, y)))
    return count


n = [0 for a in range(3)]
n[2] = nofactors2(22/2)
m = 1
for a in range(22, (10**5)-1, 2):
    n = [n[2], nofactors2(a+1), nofactors2((a+2)/2)]
    m = max(m, n[0]*n[1]-1, n[1]*n[2]-1)
    if m > 500:
        break
print m, a
print "Time taken(secs):", time.time() - ti


from math import sqrt
ti = time.time()
def triangle():
    a, b = 2, 1
    while 1:
        yield b
        b += a
        a += 1

for n in triangle():
    c = 0
    for i in xrange(1, int(sqrt(n)) + 1):
        if n % i == 0:
            c += 1
            if i * i != n:
                c += 1
    if c > 500:
        print "Answer: ", n
        break

print "Time taken(secs):", time.time() - ti




