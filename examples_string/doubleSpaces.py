str = "Hello Double  spaces. There are  no single  but  only double spaces."
## Find returns the index of the first occurrence.
print(str.find("  "))

## Replaces double spaces with single space
if(str.find("  ") != -1):
  str = str.replace("  ", " ")
  print(str)