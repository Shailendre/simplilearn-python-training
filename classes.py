# classes in python
# simple calculator class

class calculator:
    """docstring for calculator."""

    # instance methods, since need to pass that instance
    # addition
    # self is same this in java, referring to this object.
    def add(self, x, y):
        return x + y

    # instance methods, since need to pass that instance
    # substraction
    def sub(self, x, y):
        return x - y

    # static methods
    def mul(x,y):
        return x * y
# https://stackoverflow.com/questions/47240737/function-takes-2-arguments-but-3-are-given
c = calculator()
# for all defs to be called through instances
# need to add self.
# allinstance methods should have self

# internally it reseolves to:
# calculator.add(c, 2, 3)
print(c.add(2,3))
# static methods, called using class name
print(calculator.mul(4,5))
