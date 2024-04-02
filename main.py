# Завдання 1 - 2
import math


class Figure:
    def area(self):
        pass

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Площа фігури: {self.area()}"


class Rectangle(Figure):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def area(self):
        return 0.5 * self.side * self.height


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2)


class Right_triangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return 0.5 * self.a * self.b


class Trapeze(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


rectangle = Rectangle(5, 4)
print("Площа прямокутника: ", int(rectangle))
print(rectangle)

circle = Circle(4)
print(f"Площа кола: ", int(circle))
print(circle)

right_triangle = Right_triangle(3, 4)
print("Площа прямокутного трикутника: ", int(right_triangle))
print(right_triangle)

trapeze = Trapeze(3, 6, 5)
print("Площа трапеції: ", int(trapeze))
print(trapeze)

# Завдання 3
import math


class Shape:
    def __init__(self):
        pass

    def show(self):
        pass

    def save(self, filename):
        pass

    @staticmethod
    def load(filename):
        pass


class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print("Квадрат:")
        print("Координати верхнього лівого кута:", self.x, ",", self.y)
        print("Довжина сторони:", self.side_length)

    def save(self, filename):
        with open(filename, 'a', encoding="utf-8") as file:
            file.write(f"Квадрат,{self.x},{self.y},{self.side_length}\n")

    @staticmethod
    def load(filename):
        squares = []
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == 'Квадрат':
                    x, y, side_length = map(int, data[1:])
                    squares.append(Square(x, y, side_length))
        return squares


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print("Трикутник:")
        print("Координати верхнього лівого кута:", self.x, ",", self.y)
        print("Ширина:", self.width)
        print("Висота:", self.height)

    def save(self, filename):
        with open(filename, 'a', encoding="utf-8") as file:
            file.write(f"Трикутник,{self.x},{self.y},{self.width},{self.height}\n")

    @staticmethod
    def load(filename):
        rectangles = []
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == 'Трикутник':
                    x, y, width, height = map(int, data[1:])
                    rectangles.append(Rectangle(x, y, width, height))
        return rectangles


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print("Коло:")
        print("Координати центру:", self.x, ",", self.y)
        print("Радіус:", self.radius)

    def save(self, filename):
        with open(filename, 'a', encoding="utf-8") as file:
            file.write(f"Коло,{self.x},{self.y},{self.radius}\n")

    @staticmethod
    def load(filename):
        circles = []
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == 'Коло':
                    x, y, radius = map(int, data[1:])
                    circles.append(Circle(x, y, radius))
        return circles


class Ellipse(Shape):
    def __init__(self, x, y, major_axis, minor_axis):
        self.x = x
        self.y = y
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def show(self):
        print("Еліпс:")
        print("Координати центру:", self.x, ",", self.y)
        print("Велика вісь:", self.major_axis)
        print("Мала вісь:", self.minor_axis)

    def save(self, filename):
        with open(filename, 'a', encoding="utf-8") as file:
            file.write(f"Еліпс,{self.x},{self.y},{self.major_axis},{self.minor_axis}\n")

    @staticmethod
    def load(filename):
        ellipses = []
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == 'Еліпс':
                    x, y, major_axis, minor_axis = map(int, data[1:])
                    ellipses.append(Ellipse(x, y, major_axis, minor_axis))
        return ellipses


square1 = Square(0, 0, 5)
rectangle1 = Rectangle(0, 0, 6, 4)
circle1 = Circle(0, 0, 5)
ellipse1 = Ellipse(0, 0, 8, 4)

file_name = 'File1.txt'
square1.save(file_name)
rectangle1.save(file_name)
circle1.save(file_name)
ellipse1.save(file_name)

loaded_squares = Square.load(file_name)
loaded_rectangles = Rectangle.load(file_name)
loaded_circles = Circle.load(file_name)
loaded_ellipses = Ellipse.load(file_name)

for square in loaded_squares:
    square.show()

for rectangle in loaded_rectangles:
    rectangle.show()

for circle in loaded_circles:
    circle.show()

for ellipse in loaded_ellipses:
    ellipse.show()
