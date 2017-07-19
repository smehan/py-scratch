# take a string, count the frequencies, run in order.
# Beauty here is the multiple inheritance OrderedCounter that preserves the order of sorted input.
# This is needed for Counter.most_common in < 3.6 that return random sets.
# 3.6 returns to sanity and returns in order so second works there.
from collections import Counter, OrderedDict

test_s = 'ggaaffbbbccdeb'
#test_s = 'qwertyuiopasdfghjklzxcvbnm'


class OrderedCounter(Counter, OrderedDict):
    pass

[print(*x) for x in OrderedCounter(sorted(list(test_s))).most_common(3)]
[print(*x) for x in Counter(sorted(list(test_s))).most_common(3)]