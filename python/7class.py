# 1 & 2
# Class： blueprint for creating new object
# Object: instance of a class

# Class: Human
# Objects: John. Mary, Jack,


class Point:
    color = 'red'
    # constructor method
    # set initial values for x and y coordinates
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __init__(self, x, y):  # we didn't call it derictly
        # attributes
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f'Point({self.x}, {self.y})')


point1 = Point.zero()
point2 = Point(1, 1)
print(point1+point2)
