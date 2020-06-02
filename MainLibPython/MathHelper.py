import math

class MathHelper:
    def add(self, num1, num2):
        x = lambda a, b : a + b
        return x(num1, num2)
    
    def mul(self, num1, num2):
        x = lambda a, b : a * b
        return x(num1, num2)

    def pow(self, num1, num2):
        return math.pow(num1, num2)

    def formatFloat(self, num): 
        return "{:.2f}".format(num)