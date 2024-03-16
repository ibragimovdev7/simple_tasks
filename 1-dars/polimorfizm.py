from math import pi

class Shakl:
    def __init__(self, name):
        self.name = name

    def yuzi(self):
        pass

class Doira(Shakl):

    def __init__(self, radius):
        super().__init__('Doira')
        self.radius = radius

    def yuzi(self):
        return self.radius**2 * pi

    def __str__(self):
        return f'Doira yuzi: {self.yuzi()} ga teng.'


ob1 = Doira(4)
print(ob1)

