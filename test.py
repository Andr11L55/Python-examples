print(123.5)
a123=5
print("numberr= " +str(a123))
# fdggg
d=564/5
# print(d)
print("d = " +str(d)+ " - float")
print("t\tfd\ng")

N=6
S = N ** 2 # pow(N,a123)
print(S)
S += N % 5 
print(S)
a=5.4
import math
print(round(a))
print(math.floor(a))
print(math.ceil(a))
print(math.pi-1)
print(math.e ** 0)

# Calculation
 
#from colorama import init
#from colorama import Fore, Back, Style

#init()
def calc():
    what = input (" +, -, *, /, a ** b, a ** n,  b ** n " )
    a=float(input("a = " ))
    b=float(input("b = " ))
    # while(a==b)
    if what == "+" : 
        c=a+b
        print(str(c))

    elif what == "-" :
        c=a-b
        print(str(c))

    elif what == "*" : 
        c=a*b
        print(str(c))

    elif what == "/" and b!=0 : 
        c=a/b
        print(str(c))

    elif what == "a ** b" : 
        c=a  ** b
        d= math.pow(a,b)
        print(str(c))

    else :
        print("You don't read the instruction correctly! Asshole!")

print(__name__)
if __name__=='__main__':
    calc()



