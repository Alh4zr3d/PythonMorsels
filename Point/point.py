class Point:
    def __init__(self,x,y,z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, cmpr):
        return (self.x, self.y, self.z) == (cmpr.x, cmpr.y, cmpr.z)

    def __add__(self,add):
        result = Point(self.x + add.x, self.y + add.y, self.z + add.z)
        return result

    def __sub__(self,sub):
        result = Point(self.x - sub.x, self.y - sub.y, self.z - sub.z)
        return result

    def __mul__(self,multip):
        result = Point(multip * self.x, multip * self.y, multip * self.z)
        return result

    def __rmul__(self,multip):
        result = Point(multip * self.x, multip * self.y, multip * self.z)
        return result

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
