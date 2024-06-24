from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def peri(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2
    
    def peri(self):
        return 4 * self.length

# Creating an instance of Square
square = Square(5)

# Using the methods and printing the results
print("Area:", square.area())     # Output: Area: 25
print("Perimeter:", square.peri())  # Output: Perimeter: 20
