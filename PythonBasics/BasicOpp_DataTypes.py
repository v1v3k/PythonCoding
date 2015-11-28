__author__ = 'george'
import math
x=10
y=3
print x / long(y)	#quotient of x and y	(1)
print x / float(y)	#quotient of x and y	(1)
print x // float(y)	#(floored) quotient of x and y	(4)(5)
print int(x // float(y))	#(floored) quotient of x and y	(4)(5)
print x % y	#remainder of x / y	(4)
x=-10
print abs(x)	#absolute value or magnitude of x	(3)
x=10
print int(x)	#x converted to integer	(2)
print long(x)	#x converted to long integer	(2)
print float(x)	#x converted to floating point	(6)
re=x
im=y
print (complex(re,im))	#a complex number with real part re, imaginary part im. im defaults to zero.
print complex(re,im).conjugate()	#conjugate of the complex number c. (Identity on real numbers)
print divmod(x, y)	#the pair (x // y, x % y)	(3)(4)
print pow(x, y)	#x to the power y	(3)(7)
print x ** y	#x to the power y	(7)

x=1.234
print math.ceil(x)
print math.floor(x)
print math.trunc(x)
x=1.9
print math.trunc(x)
#float func
print round(1.2345,2)
# 1.23
print round(1.2375,2)
#1.24
print round(1.2345)
#1
# print round(1.888)
#2
#binnary conversion
print 'Bin opp start ----------------'
print bin(2)
print (1234).bit_length()
print (0.5).as_integer_ratio()
# print (1,2)
#Bit Opp
'''
a & b
a | b
a ^ b   -- Exor opperation
~a
a<<2
a>>2
'''
a=5
print bin(a)
a= a<<2
print bin(a)
a =a >>4
print bin(a)
'''
0b101
0b10100
0b1
'''