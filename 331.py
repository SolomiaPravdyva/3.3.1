import math

class Figure:
    def dimension(self):
        raise NotImplementedError
    def perimeter(self):
        return None
    def square(self):
        return None
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None
    def volume(self):
        raise NotImplementedError
    def show(self):
        raise NotImplementedError

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def dimension(self):
        return "2D"
    def perimeter(self):
        return self.a + self.b + self.c
    def square(self):
        p = self.perimeter() / 2
        value = p * (p - self.a) * (p - self.b) * (p - self.c)
        if value < 0:
            return 0
        return math.sqrt(value)
    def volume(self):
        return self.square()
    def show(self):
        print(f"Triangle({self.a}, {self.b}, {self.c})")
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def dimension(self):
        return "2D"
    def perimeter(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.b
    def volume(self):
        return self.square()
    def show(self):
        print(f"Rectangle({self.a}, {self.b})")
class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def dimension(self):
        return "2D"
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def square(self):
        if self.a == self.b:
            return 0
        x = (
            self.a**2
            - self.b**2
            + self.c**2
            - self.d**2
        ) / (2 * (self.a - self.b))
        h2 = self.c**2 - x**2
        if h2 < 0:
            return 0
        h = math.sqrt(h2)
        return (self.a + self.b) * h / 2
    def volume(self):
        return self.square()
    def show(self):
        print(f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})")
class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a=a
        self.b=b
        self.h=h
    def dimension(self):
        return "2D"
    def perimeter(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.h
    def height(self):
        return self.h
    def volume(self):
        return self.square()
    def show(self):
        print(f"Parallelogram({self.a}, {self.b}, {self.h})")
class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def dimension(self):
        return "2D"
    def perimeter(self):
        return 2 * math.pi * self.r
    def square(self):
        return math.pi * self.r ** 2
    def volume(self):
        return self.square()
    def show(self):
        print(f"Circle({self.r})")

class Ball(Figure):
    def __init__(self, r):
        self.r = r
    def dimension(self):
        return "3D"
    def squareSurface(self):
        return 4 * math.pi * self.r ** 2
    def volume(self):
        return (4 / 3) * math.pi * self.r ** 3
    def show(self):
        print(f"Ball({self.r})")
class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h
        self.side = a
    def dimension(self):
        return "3D"
    def squareBase(self):
        return super().square()
    def height(self):
        return self.h
    def squareSurface(self):
        l = math.sqrt(self.h ** 2 + (self.side * math.sqrt(3) / 6) ** 2)
        return 3 * self.side * l / 2
    def volume(self):
        return self.squareBase() * self.h/3
    def show(self):
        print(f"TriangularPyramid({self.side}, {self.h})")
class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
    def dimension(self):
        return "3D"
    def squareBase(self):
        return super().square()
    def height(self):
        return self.h
    def squareSurface(self):
        l1 = math.sqrt(self.h**2 + (self.b/2)** 2)
        l2 = math.sqrt(self.h**2 + (self.a/2)** 2)
        return self.a * l1 + self.b * l2
    def volume(self):
        return self.squareBase() * self.h/3
    def show(self):
        print(f"QuadrangularPyramid({self.a}, {self.b}, {self.h})")
class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    def dimension(self):
        return "3D"
    def squareBase(self):
        return super().square()
    def height(self):
        return self.c
    def squareSurface(self):
        return 2 * (self.a * self.c + self.b * self.c)
    def volume(self):
        return self.a * self.b * self.c
    def show(self):
        print(f"RectangularParallelepiped({self.a}, {self.b}, {self.c})")
class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h
    def dimension(self):
        return "3D"
    def squareBase(self):
        return super().square()
    def height(self):
        return self.h
    def squareSurface(self):
        l = math.sqrt(self.r ** 2 + self.h ** 2)
        return math.pi * self.r * l
    def volume(self):
        return self.squareBase() * self.h / 3
    def show(self):
        print(f"Cone({self.r}, {self.h})")
class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h
    def dimension(self):
        return "3D"
    def squareBase(self):
        return super().square()
    def height(self):
        return self.h
    def squareSurface(self):
        return super().perimeter() * self.h
    def volume(self):
        return self.squareBase() * self.h
    def show(self):
        print(f"TriangularPrism({self.a}, {self.b}, {self.c}, {self.h})")
#----------
def create_figure(parts):
    name=parts[0]
    nums = list(map(float, parts[1:]))

    if name == "Triangle":
        return Triangle(*nums)
    elif name == "Rectangle":
        return Rectangle(*nums)
    elif name == "Trapeze":
        return Trapeze(*nums)
    elif name == "Parallelogram":
        return Parallelogram(*nums)
    elif name == "Circle":
        return Circle(*nums)
    elif name == "Ball":
        return Ball(*nums)
    elif name == "TriangularPyramid":
        return TriangularPyramid(*nums)
    elif name == "QuadrangularPyramid":
        return QuadrangularPyramid(*nums)
    elif name == "RectangularParallelepiped":
        return RectangularParallelepiped(*nums)
    elif name == "Cone":
        return Cone(*nums)
    elif name == "TriangularPrism":
        return TriangularPrism(*nums)
    return None

def process_file(filename):
    figures = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                figure = create_figure(parts)
                if figure:
                    figures.append(figure)
    except FileNotFoundError:
        print("Файл не знайдено")
        return
    print(f"\n--- Аналіз файлу {filename} ---")
    max_figure = None
    max_measure = -1
    for fig in figures:
        measure = fig.volume()
        if measure > max_measure:
            max_measure = measure
            max_figure = fig
    print("\nФігура з найбільшою мірою:")
    max_figure.show()
    print(f"Найбільша міра = {max_measure}")

process_file("input01.txt")
#process_file("input02.txt")
#process_file("input03.txt")
