with open('files/donkey.txt') as f:
    line = str(f.readline())
    line = line.replace("donkey", "xxxx")

with open('files/donkey.txt','w') as f:
  f.write(line)
