## Example for try, exception, else and finally

try:
  n = int(input("Please enter a number\n"))
  a = n/4
  print(f"The answer is {a}")

except Exception as e:
  print(f"Error : {e}")

else:
  print("The block of statements here are executed only when try is executed successfully")

finally:
  print("The block of statements here are always executed")
