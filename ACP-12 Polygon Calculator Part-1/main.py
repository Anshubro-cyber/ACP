from abc import ABC, abstractmethod
class Polygon(ABC):
    """Abstract base class for polygons."""
    @abstractmethod
    def area(self):
        """Calculates the area of the polygon."""
        pass
class Triangle(Polygon):
    """Represents a triangle."""
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        """Calculates the area of a triangle."""
        return 0.5 * self.base * self.height
class Rectangle(Polygon):
    """Represents a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        """Calculates the area of a rectangle."""
        return self.length * self.width
class Square(Rectangle):
    """Represents a square (a special case of a rectangle)."""
    def __init__(self, side):
        super().__init__(side, side) # Use Rectangle's initializer
# Example usage
triangle = Triangle(5, 4)
rectangle = Rectangle(6, 3)
square = Square(4)
print("Triangle area:", triangle.area())
print("Rectangle area:", rectangle.area())
print("Square area:", square.area())