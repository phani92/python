# Example for overloading operators using complex numbers

class ComplexNumber:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    # Overloading string operator
    def __str__(self):
        if self.img < 0:
            return(f"{self.real} - {-self.img}i")
        return(f"{self.real} + {self.img}i")

    # overloading '+'
    def __add__(self, num):
        sum_real = self.real + num.real
        sum_img = self.img + num.img
        return(ComplexNumber(sum_real, sum_img))

    # Overloading '-'
    def __mul__(self, num):
        mul_real = (self.real * num.real) - (self.img * num.img)
        mul_img = (self.real * num.img) + (self.img * num.real)
        return(ComplexNumber(mul_real, mul_img))


cmp1 = ComplexNumber(1, -4)
print(cmp1)
cmp2 = ComplexNumber(331, -37)
print(cmp2)
print("The sum is", cmp1 + cmp2)
print("The product is", cmp1 * cmp2)
