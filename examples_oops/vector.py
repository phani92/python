## Example for base, derived class and super method.

# Base Class
class C2DVector:
    def __init__(self, x, y):
        self.iCap = x
        self.jCap = y

    def addVectors(self):
        return self.iCap + self.jCap

# Derived Class
class C3DVec(C2DVector):
    def __init__(self, x, y, z):
        self.iCap = x
        self.jCap = y
        self.kCap = z

    def addVectors(self):
        return super().addVectors() + self.kCap

# Create objects
coOrd1 = C2DVector(4, 5)
coOrd2 = C3DVec(5, 6, 7)

print("Sum of the 2d vectors", coOrd1.iCap, "and",
      coOrd1.jCap, "is", coOrd1.addVectors())
print("Sum of the 3d vectors", coOrd2.iCap, ',', coOrd2.jCap,
      "and", coOrd2.kCap, "is", coOrd2.addVectors())
