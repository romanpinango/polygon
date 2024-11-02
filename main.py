import math
import polygon


# Triangle Class
class Triangle(polygon.Polygon):
    def __init__(self, side1, side2, side3):
        super().__init__(3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        # Calculate area using Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))


# Rectangle Class
class Rectangle(polygon.Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


# Square Class (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# Usage example
triangle = Triangle(3, 4, 5)
print("Triangle perimeter:", triangle.perimeter())
print("Triangle area:", triangle.area())

rectangle = Rectangle(5, 10)
print("\nRectangle perimeter:", rectangle.perimeter())
print("Rectangle area:", rectangle.area())

square = Square(4)
print("\nSquare perimeter:", square.perimeter())
print("Square area:", square.area())