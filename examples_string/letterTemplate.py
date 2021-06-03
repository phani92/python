letter = '''Dear <|name|>,
You are selected!
Joining date is <|date|>'''
name = input("Enter your name\n")
date = input("Enter your doj\n")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter)