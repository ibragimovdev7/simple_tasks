class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

class SuperCalc(Calc):
    def __init__(self, x, y):
        super().__init__(x, y)

    def pow(self):
        return self.x ** self.y

x = int(input('x = '))
y= int(input('y = '))

ob1 = SuperCalc(x,y)
print((ob1.pow()))