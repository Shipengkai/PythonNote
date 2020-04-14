# 1 & 2
# Class： blueprint for creating new object
# Object: instance of a class

# Class: Human
# Objects: John. Mary, Jack,


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(type(point.__init__()))