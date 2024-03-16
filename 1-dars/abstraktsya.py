from abc import ABC, abstractmethod


class Shakl(ABC):
    @abstractmethod
    def yuzi(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

class Uchburchak(Shakl):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def perimetr(self):
        return self.x + self.y + self.z

    def yuzi(self):
        return 'Hello world'

uch = Uchburchak(3,5,4)
print(uch)


class Tortburchak(Shakl):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimetr(self):
        return self.a + self.b + self.c + self.d
