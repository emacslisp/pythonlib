class Number():
    def __init__(self):
        print("Number Created")
    def who_am_i(self):
        print("I am an number")
    def value(self):
        print("Number's value")
    def someMethod(self):
        raise NotImplementedError('SubClass must implement this abstract method')

class ComplexNumber(Number):
    def __init__(self):
        Number.__init__(self)
        print("Complex Number is create")
    def who_am_i(self):
        print("I am Complex Number")
        print(super().who_am_i())
    def someMethod(self):
        print("ComplexNumber someMethod")

class RealNumber(Number):
    def __init__(self):
        Number.__init__(self)
        print("Real Number is create")
    def someMethod(self):
        print("Real Number someMethod")
    
myNumber = ComplexNumber()
myNumber.who_am_i()
myNumber.someMethod()

rNumber = RealNumber()
rNumber.someMethod()