
# Prints multiplication table in a file

for i in range(2, 10):
  with open(f"files/tables/table_{i}", 'w') as f:
    for j in range(1,51):
      product = i * j
      string = str(i) + "x" + str(j) + "=" + str(product) + "\n"
      f.write(string)

