__author__ = 'george'
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

s='12edwdqq'

print  [i for i in permutations(s,2)]
k=  [i for i in permutations(s,2)]
print len(k)
print  [i for i in combinations(s,2)]
k= [i for i in combinations(s,2)]
print len(k)
print  [i for i in combinations_with_replacement(s,2)]
k=[i for i in combinations_with_replacement(s,2)]
print len(k)

