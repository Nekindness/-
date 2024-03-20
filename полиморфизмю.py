class Shape:
    def draw(self):
        raise NotImplementedError("Subclasses must implement the draw method")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")

shapes = [Circle(), Square(), Triangle()]

for shape in shapes:
    shape.draw()