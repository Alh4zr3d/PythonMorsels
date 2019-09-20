import math

class Circle:
    def __init__(self,radius = 1):
        self.radius = radius
#        self.diameter = self.radius * 2
#        self.area = math.pow(self.radius,2) * math.pi

    def __repr__(self):
        return f"Circle({str(self.radius)})"

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * math.pow(self.radius,2)

    @property
    def radius(self):
        return self._radius

    @diameter.setter
    def diameter(self,diameter):
        self.radius = diameter / 2

    @radius.setter
    def radius(self,radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = radius
