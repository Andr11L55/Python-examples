class A:
    def a(self):
        print('A')

class B:
    def a(self):
        print('B')

class C(B):
    def a(self):
        print('C')


class D(C,A):
    def a(self):
        super(B, self).a()
        # print(self.__class__.__mro__)

# print(D.__mro__)
D().a()



from ads import Player

Player.set_cls_filed(10)
x = Player()
print(x.lvl)

Player.set_cls_filed()
y = Player()
print(y.lvl)
y.lvl="5"














class Vertification:
    def __init__(self, login, password):
        self.login = login
        self.password= password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password)< 8:
            raise ValueError('too easy pas')

    def save(self):
        with open('users.txt', 'a') as r:
            r.write(f'{self.login, self.password}' + ' \n')