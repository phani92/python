## Example to convert a list into a vertical string.

try:
  num = int(input("Enter a num\n"))
  table = [str(num*i) for i in range(1,21)]
  vTable = "\n".join(table)
  print(vTable)
except Exception as error:
  print("You have entered character other than a number")
