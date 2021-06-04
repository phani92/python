class Calculator:

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def sum(self):
        return self.a + self.b

    def product(self):
        return self.a * self.b

    def difference(self):
        return abs(self.a - self.b)

    def quotient(self):
        return self.a / self.b

    def cube(self):
        return self.a ** 3

    def squareRoot(self):
        return self.a ** 0.5

    def getResults(self):
        print("sum of", self.a, "and", self.b, "is", self.sum())
        print("Difference between", self.a, "and",
              self.b, "is", self.difference())
        print("Product of", self.a, "and", self.b, "is", self.product())
        print("Quotient of", self.a, "and", self.b, "is", self.quotient())
        print("Cube of", self.a, "is", self.cube())
        print("Square root of", self.a, "is", self.squareRoot())
        print("\n")


example1 = Calculator(10, 5)
example1.getResults()
example2 = Calculator(100, 5)
example2.getResults()
example3 = Calculator(1000, 5)
example3.getResults()
example4 = Calculator(10000, 5)
example4.getResults()
