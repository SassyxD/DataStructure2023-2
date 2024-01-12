"""Lab 01.05.py"""
class Point:
    """Lab 01.05.py"""
    def __init__(self, x=0, y=0):
        self.set_coordinates(x, y)
    """Lab 01.05.py"""
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    """Lab 01.05.py"""
    def get_coordinates(self):
        return (self.x, self.y)
    """Lab 01.05.py"""
    def calculate_distance(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) **2  ) ** 0.5
    """Lab 01.05.py"""
bossX = float(input())
bossY = float(input())
 
artX = float(input())
artY = float(input())
 
boss_coordinates = Point(bossX, bossY)
art_coordinates = Point(artX, artY)
 
distance = boss_coordinates.calculate_distance(art_coordinates)
print('%.2f' %distance)
