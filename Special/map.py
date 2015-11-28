__author__ = 'george'
from operator import itemgetter

items = [1, 2, 3, 4, 5]

''' lambda    var = lambda x,y: x+y'''
g = lambda x: x**2
print g(8)
# 8^2


''' Map imp  list = map(function,iter) '''
def sqr(x):
    return x ** 2
print list(map(sqr, items))
# Output [1, 4, 9, 16, 25]


''' Zip implemntation  [(a,b)] = zip(iter1,iter2) '''
a=[1,2,3,4]
b=[5,6,7,8]
z=zip(a,b,b)
print z
# Output [(1, 5, 5), (2, 6, 6), (3, 7, 7), (4, 8, 8)]
dict={}
for (i,j) in zip(a,b):
    dict[i]=j
print dict
# {1: 5, 2: 6, 3: 7, 4: 8}


''' Filter:  filter ( function , iter) '''
x = list(range(-5,5))
y = list(filter(lambda i: i<0,[-1,2,-3,4,5]))
print y
# [-1,-3]


''' reduce  reduce(function(x,y) iter,)'''
inte = reduce(lambda x,y:x+y,[1,2,3,4,5,6])
print inte
# 21

#Lambda
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
print sorted(student_tuples, key=itemgetter(1,2))

# if sort done on multiple atter in diff direction -> sort multiple times starting with lower preference
