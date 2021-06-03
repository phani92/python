marks = []
baseInpStr = "Enter the mark of student <i> \n"
for i in range(6):
  baseInpStr = baseInpStr.replace("<i>", str(i))
  studentMark = input(baseInpStr)
  marks.insert(i,int(studentMark))
  marks.sort()
print(marks)
print("sum is", sum(marks))
