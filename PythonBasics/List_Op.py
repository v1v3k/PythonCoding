__author__ = 'george'

from random import random

def random1(x):
    return random()


list1= [1,3,5,6,7,8,10,11]
list3 =['a','b','c','d']

#Index opperations
print 'Index Operations list 3', list3
# ['a','b','c','d']
print list3[-3:]
# ['b', 'c', 'd']
print list3[-2]
# c
print list3[-3:-1]
# ['b', 'c']
print list3[:-1]
# ['a', 'b', 'c']
print list1[1:4]
# prints from 1 to 4-1
print list1[:]
# prints from 0 to n-1



#append
print list1.append(10)
print (list1)


#pop
print list1.pop()
#pops index n-1
print list1.pop(2)
#pops index at index 2
print list1.pop(0)
#pops index at index 0


#insert
print list1.insert(0,'start inseertion')
list1.append(332)
# append at end
list1.index(332)
# tells index of first time value is seen
list1.remove(332)
# removes 1st occurance of 332
list1.append(332)
# append 332 to the end
list1.insert(5,332)
# insert at index 5
print list1.count(332)
# counts number of times 332 is seen in list1
list1[0]='newval'
# update list1
del list1[2]
# del specific element
# len
print len(list1)
# concat
print list1 + list3
# List multiplication operation
print ['%%']*10
print [None]*10
# Check presence
print 3 in list1
print 999 in list1
# extend
print list1.extend(list3)


