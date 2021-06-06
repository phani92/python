## Example to create a comprehension list that contains the multiplication table of a user entered number.

try:
  n = int(input("Enter a number\n"))
  table = [n*i for i in range(1,21)]
  print(table)
except Exception as error:
  print(f"Please enter a valid number, {error}")
