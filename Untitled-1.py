import sys
import math
def f(x):
    return x**3-18*x-83
def f1(x):
    return 2*x**2-18
try:
        a=input()
        b=input()
    if a and b:
        i==a
        j==b
        while True:
                i=i-((f(a)*(j-i))/(f(j)-f(i)))
                j=j-f(j)/f1(j)
                if abs(j-i)<sys.float_info.epsilon:
                    break
except ValueError as err:
    print(err)
print(j)
