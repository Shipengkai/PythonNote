class Product:
    def __init__(self, value):
        self.price = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negetive.')
        self.__price = value


print('start')
p1 = Product(10)
p1.price = -1
print(p1.price)
