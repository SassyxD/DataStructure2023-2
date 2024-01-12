"""Lab 01.04.py"""
class Rectangle:
    """Lab 01.04.py"""
    def __init__(self, height, width):
        self.height = height
        self.width = width
    """Lab 01.04.py"""
    def calculate_area(self):
        return self.height * self.width
    """Lab 01.04.py"""
    def calculate_perimeter(self):
        return (2 * self.width) + (2* self.height)
    """Lab 01.04.py"""
rectangle = Rectangle(float(input()), float(input()))
 
cond = input()
if cond == "area":
    resul1t = rectangle.calculate_area()
else:
    resul1t = rectangle.calculate_perimeter()
print("%.2f" % resul1t)
