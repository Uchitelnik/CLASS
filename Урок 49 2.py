class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def perimeter(self):
                return (self.length + self.width) * 2

    def area (self):
        return self.length * self.width


har = Rectangle(23 , 12)

print(har.perimeter())

print(har.area( ))