import math

class ComplexNumber:
    pi = 3.1415
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


c = ComplexNumber(1, 2)

print(c.length())
print(c.pi)