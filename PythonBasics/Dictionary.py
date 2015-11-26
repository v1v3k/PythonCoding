__author__ = 'george'

A= {1:10, 2:20, 3:30, 4:40}

print A.keys()
print A.values()
print A.items()

for k,v in A.items():
    print k,v

print 1 in A.keys()
print type(A)


print '-----------'
#creates new instane
B= A.copy()
B[1]=22
print A
print B

print '----------'
#Points to same instance
B=A
B[1]=22
print A
print B



A= {1:10, 2:20, 3:30, 4:40}
B= {5:50}

A.update(B)
print A
B= {5:50,1:30}
A.update(B)
# B overwrites A
print A


print A
print A.get(1)
# retrun Value
print A.get(10)
# None