import random
import math

A=random.uniform(-10,10)
print("A= " + str(A))
x=A

if x <= 0:
    print("x <= 0")
    f=0
    print("f(A)= " + str(f)) 
elif 0 < x and x < 1:
    print("0 < x < 1")
    f=x**2
    print("f(A)= x**2 = " + str(f))
elif not x <= 0 or (0 < x and x < 1):
    print("Other case")
    pi=math.pi
    sin=math.sin( pi * x**2)
    f= x**2 - sin
    print("f(A)= " + str(f))
