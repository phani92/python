num = int(input("Please enter a number\n"))
for i in range(2,num):
  if(num % i == 0):
    print(num,"is not prime")
    break
else:
  print(num,"is prime")
