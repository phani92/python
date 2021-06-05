# This example handles vectors of n dimension

class Vector:

    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        sum = []
        for i in range(len(self.vec)):
            sum.append(self.vec[i] + vec2.vec[i])
        return Vector(sum)

    def __mul__(self, vec2):
        mul = 0
        for i in range(len(self.vec)):
            mul += self.vec[i] * vec2.vec[i]
        return mul


v1 = Vector([5, 6, 7])
print(v1)
v2 = Vector([5, 6, 7])
print(v2)
print(f"The sum of {v1} and {v2} is {v1+v2}")
print(f"The dot product of {v1} and {v2} is {v1*v2}")
