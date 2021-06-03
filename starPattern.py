star = '*'
space = " "

# *
# * *
# * * *
num = int(input("Please enter a number\n"))
for i in range(num):
    print(star * (i+1))

#     *
#   * * *
# * * * * *
for i in range(num):
    print(space * (num-i-1), end = "")
    print(star * ((2*(i+1))-1), end = "")
    print(space * (num-i-1))
