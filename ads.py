# 1.
# a,b,c = 5,3,2
# print(a-b+c) # 4
# a,b,c = c,a,b
# print(a-b+c) # 0? 

# 1.
# [n,x,m, q, *r,e]= a,b,c,4.5,3,3.4,3,3,5,2,3
# print(n,x,m,q,r,e)
# print(type(q),type(x))

# 1. 
# x = int(input("enter number:"))
# y = float(input("enter number:"))
# r=x+y
# print(type(x) ,'\nres:' + str(round(r)))

# 1.
# import os
# site = input()

# if 'https://' in site:
#     os.system('start ' + site)
#     print('if')

# elif 'www.' in site:
#     site = 'https://' + site
#     os.system('start ' + site)
#     print('elif')

# else:
#     site = 'https://www.' + site
#     os.system('start ' + site)
#     print('else')

# 1.
# import os
# import time

# os.system('start https://www.youtube.com/')

# time.sleep(4)

# os.startfile('C:\WINDOWS\system32\mspaint.exe')

# 1.
# while True:
#     x= int(input('number:'))
#     count = 0
#     y=1

#     while count < x :
#         count += 1
#         y *= count

#     print(y)

# 1.
# x='qwertyuiopasdfghjklzxcvbnm'
# y=input('string:\n')

# # for i in x:
# #     count = 0
# #     for r in y:
# #         if i == r:
# #             count += 1
# #     if count>0:
# #         print('letters' , i, 'was', count)

# 1.
# for x in range(3,-10, -4):
#     print(x)

# 1.
# n = list(range(3,-10, -4))
# x= n.copy()
# n.append(5)
# n.insert(2,69)
# s=n.count(5)
# n.sort()
# n.reverse()
# n.pop(-1)
# n.remove(-1)
# n.extend([25,-42,-69])
# print(n)
# print(x)
# y = n[0::3]
# print(y)

# 1.
# x=(4.5, 4.55, 2.3, 5, 3.3, 4, 6)
# a,b,c,d,e,f,g=x
# y=[]
# for i in range(len(x)):
#     y.append(x[i]+3)

# print(x)
# print(type(x),y)
# print(a,b,c,d,e,f,g)

# y=tuple(y)
# x += y
# print(x)


# 1.

# import os
# import time
# spisok=[]
# for adr, dirs, files in os.walk('D:\\!PROGRAMMING\Python'):
#     for file in files:
#         full = os.path.join(adr , file)
#         if time.time() - os.path.getctime(full) < 7*86400:
#             spisok.append(full)
    
# print(spisok) 


# 1.
# print('before func')
# def show():
#     print('dfhs')

# def show2(a):
#     x = 7
#     return x**a

# y=show2(2)
# print(y)

# 1.
# def name(r,*a):
#     print(a)

# name(43,32,12)




# def ex_it(*a, key=False):
#     new_list = []
#     for i in a:
#         for j in i:
#             if j not in new_list:
#                 new_list.append(j)
#     if key == True:
#         new_list.sort()
#     return new_list

# z= [9,8,6,2,4,3]
# x=[3,4,8,5,3]
# c=[9,6,3,8,7]
# t=ex_it(z,x,c, key = True)
# print(t)

# 1.
# d1={'a':7}
# d1['c']='dsf'

# print(d1)
# del d1['a']
# d1['a']=42+4
# print(d1)

# d2=dict( [ [1,'a'], ["dsa", 34] ] ,a=7,f='f',c = 4 )
# print(d2)

# d3=dict.fromkeys([1,4,9,16,25], ['lox'])
# print(d3)

# d4 = d1.copy()
# print(d1.items())
# print(d1.keys())
# print(d1.values())
# d1.update(d3)
# print(d1)

# if 'c' in d1:
#     d1['c']

# y = d1.get('ca', 'calox')
# print(y)

# t = d1.popitem()
# print(t, d1)

# price= {'salymi': 4, 'salo': 43, 'edar': 54}

# users={
#     'flox': {'pas':425, 'id':4},
#     'salox': {"pas": 534, 'id':34},
#     'dalox': {'pas': 5432, 'id':4453}
# }

# def buy():
#     pay=0
#     while True:
#         enter= input('why are you here noob?\n')
#         if enter=='end':
#             break
#         pay += price[enter]
#     return pay

# print(buy())


# 1.

# price= {'salymi': 4, 'salo': 43, 'edar': 54}

# shit={}

# for key, val in price.items():
#     val*=.5
#     shit[key]=val
# #     shit[i]=price[i]*4e-2+5
# print(price,shit)



# 1.
# import os

# list_paths= []

# for adr, dir, file in os.walk('D:\\'):
#     for i in file:
#         full_path= os.path.join(adr,i)
#         list_paths.append(full_path)


# for x in list_paths:
# for i in r:
#     if 'Python' in i:
#         print(i)
# u= r.read()
# print(u)


# r = open('D:\\GTA TTDISA_SINGLE\samp.exe', 'rb')
# y=open('copy samp.exe', 'wb')

# while True:
#     var = r.read(1024*1024)
#     print(var.__sizeof__())
#     if var.__sizeof__()==33:
#         break

#     y.write(var)

# print('contr')
# r.close()
# y.close()


# r = open('text2.txt', 'a', encoding='utf-16')
# r.write('\nstr выпвапв ваі')
# # print(r)

# r.close()

# h=open('text2.txt', encoding='utf-16')

# print(h.read())
# h.close()

# 1.
# t={'gg', 1,2,3,3,2,1,(4,5), 'f'}
# t.
# print(t)
# y=set()

# x=(1,2,3,4,5,6,7)  # cortage
# y=[1,2,3,4,5,6,7] # list
# u={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7} # dictionary
# h={1,2,3,4,5,6,7} # ?opportunity?

# print(x.__sizeof__())
# print(y.__sizeof__())
# print(u.__sizeof__())
# print(h.__sizeof__())

# import time

# def f(*args):
#     list=[]
#     for i in args:
#         for y in i:
#             if y not in list:
#                 list.append(y)
#     return list 

# z=list(range(1000))
# x=list(range(500,1500))
# c=list(range(1000,2000))

# start = time.time()
# f(z,x,c)
# # print(f(z,x,c))
# stop= time.time() - start
# print(stop)

# start2= time.time()
# r= set(z)
# t=r.union(set(x), set(c))
# stop2= time.time() - start2
# print(stop2)

# z={1,2,3,5}
# x={3,4,5,6,8}
# z.add(6)
# z.discard(77)
# # y= z.union(x)
# # z.update(x)
# t=z.intersection(x)
# e=z.difference(x)
# print(e)
# print(z)
# print(t)

# n=set()

# r = open('text2.txt', encoding='utf-16')

# n.update(set(r.read().split()) )

# r.close()

# print(n)




# 1.
# a='deloxXs\'d dfsGgf. \"gGay" '
# url = 'https:\\www.youtube.com\\new'
# x= 'D:\\!PROGRAMMING\\Python'
# print(a[0:5:2])
# print('lox' in a)
# print(a.upper())
# print(a.capitalize())

# x1= x.replace('\\','\/')
# print(x1)

# x2=x1.split('\/')
# print(x2[-1])

 
# text= open('text.txt')
# # print(text.read())
# t=text.read()
# # l = ','

# t1=t.split("\\")
# print(t1.__len__())






# 1.
# e=input('lox? ')
# s= "hello %s, f for ur %s" % (e, 'dodika')
# print(s) 

# sak= 'halo {1} , yur fak is {0}'.format(e,'lox')
# print(sak)

# s2=f'hal {e} , i ur noob {"gay"}'
# print(s2)



# 1. 

# willkozz code

# while True:
#     try:
#         e = float(input('?'))
#         print('terpim...', 100/e)
#         # break

#     except ValueError:
#         print('terpi carlik!')
#         # e = float(input('?'))
#     except ZeroDivisionError:
#         print('lox krchn 0000!')
#     else:
#         print('chetayetzya!')
#     finally:
#         print('ne chetayetzya')



# import sys
# url = [ 'text2.txt', 'text25.txt','text1.txt', 'text55.txt']

# ld=[]
# li=[]

# try:
#     for u in url:
#         try:
#             r = open(u)
#             li.append(r.read())
#             print('here', li)
#         except Exception:
#             ld.append(u)
#             print('there', ld)
#             sys.exit()
#             continue
# finally:
#     r = open('save.txt', 'a')
#     for i in li:
#         r.write(i)
#     r.write('\n\nlox:' +str(ld))
#     r.close()
#     print('done down!')


# 1.

# r=open('file.txt', 'a')
# try:
#     r.write('\nsmth' + '\n')
#     10/0
#     r.write('y?\n')
    

# except ZeroDivisionError:
#     print('0lox0')

# finally:
#     r.close()
#     print('fine')

# with open('file.txt', 'a') as r:
#     r.write('\n\nsmth ]\n')
#     10/0
#     r.write('MZMN?')

# print('fak')



# 1.
# import test
# from test import *
# # print(help(test))
# # calc()
# x=7
# print(dir(test))
# print(N**-(a123)+a123)

# from sys import *
# # print(dir())
# # print(test.calc())




# 1. КОСТилы

# from tkinter import *
# import random, time

# def dice():
#     x= random.choice(['b.png','b2.png','b3.png','b4.png','b5.png','b6.png'])
#     return x

# def img(e):
#     global b1,b2
#     for i in range(10):
#         b1 = PhotoImage(file=(dice()))
#         b2 = PhotoImage(file=(dice()))
#         lab1['image'] = b1
#         lab2['image'] = b2
#         root.update()
#         time.sleep(0.1)
        

# root = Tk()
# root.geometry('400x200')
# root.title('Lox or not?')
# root.resizable(height=False, width=False)
# root.iconphoto(True, PhotoImage(file=('iconka.png')))
# desktop = PhotoImage(file=('holst.png'))
# Label(root, image=desktop).pack()
# lab1 = Label(root)
# lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
# lab2 = Label(root)
# lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
# root.bind('<1>', img)
# img('e')

# root.mainloop()



# 1.

# def decor(func):
#     def wrapper():
#         try:
#             h = func()
#         except Exception:
#             print('terpi karlik...')
#             h = func()
#         return h
#     return wrapper

# @decor # make=decor(make)
# def make():
#     e = float(input('terpish?\n'))
#     return e
# @decor # make2=decor(make2)
# def make2():
#     e = float(input('carlik?\n'))
#     return e


# make2()
# print('asu')
# make()




# 1.
# import os
# h= [10,8,7,6,5,4,3,2,1,5,3,1,5,2]
# newh= []
# for x in h:
#     newh.append(x*2)
# # print(newh)

# n=[x%9 for x in newh]
# r={x*5 for x in n}
# f={x: x-42 for x in r}
# # print(f)
# g=[x for x in n if x%2 == 0 and x>=0]
# print(g)

# gg=[os.path.join(s,i) for s,x,c in os.walk('D:\\') 
#     for i in c if '.txt' in i]
# print(len(gg),gg)



# # 1.

# h=['t y', 'l ox', 'o sb', 'ter pi']

# n= [x.split(' ') for x in h]
# z=(x for x in h) 
# # for i in z:
# #     print(i)
# print(type(n))
# next(z)

# 1.
# def some():
#     list_text = []
#     with open('text1.txt', encoding='utf-8') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text
    
# def some():
#     with open('text1.txt', encoding='utf-8') as r:
#         for x in r:
#             yield x


# p= some()
# for i in p:
#     print(i)




# 1.

# from dis import dis

# def some(x):
#     return "press F", x/0

# f = lambda x:(x/0,'press GG') 

# # print(some(55))

# print(f(55))
# # print(dis(some))
# # print(dis(f))

# li=[['a',45],['d',43],['y',48],['i',32],['u',25]]

# def s(x):
#     return x[1]

# r = sorted(li, key=lambda x: x[-1])
# r = list(filter(lambda x: x[1]>25, li))
# print(r)
















# OOP

# from tkinter import Tk
# x = [1,3,4,2,6,43,32] # object
# x.append('df')
# y=[7,42,4,2,3] # object
# print(x)

# root = Tk()
# root.mainloop()

# class Purse:
#     def __init__(self, valuta, name='Incog') :
#         if valuta not in ('USD', 'UAH'):
#             raise ValueError ('ruskiy!')
#         self.__money = 0.00
#         self.__valuta = valuta
#         self.__name = name
    
#     def top_up_balance(self,amount):
#         self.__money = self.__money + amount
#         return amount
    
#     def top_down_balance(self, amount):
#         if self.__money - amount < 0:
#             print('earn money to top down, lox!')
#             raise ValueError ('LOX!')
#         self.__money = self.__money - amount
#         return amount
    
#     def info(self):
#         print(self.__money) 
    
#     def __del__(self):
#         print('del wallet')

# x = Purse('UAH', 'deb')
# y=Purse('USD')
# x.top_up_balance(45.50)
# x.info()
# y.top_up_balance(228)
# y.info()
# x.top_up_balance(y.top_down_balance(7))
# x.info()
# # x.top_down_balance(150)

# # x.top_down_balance(55)
# y.info()
# x.name='FLOX'
# x.info()
# # print(x.money)


# del x



# from class3 import Vertification
# from tkinter import Button, Tk



# class V2(Vertification):
    
#     def __init__(self, login, password, age):
#         super().__init__(login, password)
#         self.age = age
#         self.__save()
        


#     def __save(self):
#         with open('users.txt') as r:
#             for i in r:
#                 if f'{self.login, self.password}' + ' \n' == i:
#                     raise ValueError ( 'this user already exists')
#         super().save()


#     def show(self):
#         return self.login, self.password, self.age

# x= V2('gsd532', '53425loxXD', 65)



# class App(Tk):

#     def __init__(self):
#         Tk.__init__(self)
#         self.geometry('400x400')
#         self.setUI()

#     def setUI(self):
#         Button(self, text="OK").pack()

# root=App()
# root.mainloop()
# print(root)

# from datetime import datetime as dt
# from time import sleep

# class Player:
    
#     __LVL, __HEALTH = 1, 100
#     __slots= ['__lvl', '__health', '__born']


#     def __init__(self):
#         self.__lvl = Player.__LVL
#         self.__health = Player.__HEALTH
#         self.__born = dt.now()

#     @property
#     def lvl(self):
#         return self.__lvl, f'{dt.now() - self.__born}'

#     @lvl.setter
#     def lvl(self, num):
#         self.__lvl+=Player.__typeTest(num)
#         if self.__lvl >= 100:
#             self.lvl=100

#     @classmethod
#     def set_cls_filed(cls, lvl=1, health=100):
#         cls.__LVL = Player.__typeTest(lvl)
#         cls.__HEALTH = Player.__typeTest(health)
    
#     @staticmethod
#     def __typeTest(value):
#         if isinstance(value, int):
#             return value
#         else:
#             raise TypeError ('Must be int')






class A:
    def __init__(self,n):
        self.n=n

a=A('class')
print(len((1, )))


