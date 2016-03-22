# Copyright 2015 Shawn R Mehan <shawn dot mehan at shawn dot mehan dot com>
def dict2list(dct, keylist): return([dct[k] for k in keylist])

def list2dict(L, keylist): return({k:v for (k,v) in (zip(keylist, L) )})


dct = {'a':'A', 'b':'B', 'c':'C'}
keylist = ['a', 'b','c']
L = ['A','B','C']
print(dict2list(dct, keylist))
print(list2dict(L, keylist))