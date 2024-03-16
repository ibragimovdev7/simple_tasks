class Car:
    model = 'Malibu'
    __price = 25000
    color = 'black'

    def getter(self):
        return self.__price

    def setter(self, new_price):
        self.__price = new_price
        return self.__price

    def __hello(self):
        return 'Hello world'

car1 = Car()

print(car1)