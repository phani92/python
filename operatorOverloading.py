class Number:
  def __init__(self, num):
      self.num = num

  def __add__(self, num2):
    return self.num + num2.num

num1 = Number(5)
num2 = Number(6)
sum = num1 + num2
print( "Sum is",sum )