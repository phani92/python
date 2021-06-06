# Example to open three files and if one of the file is not present then handle the exception.

for i in range(4):
    try:
        with open(f'files/{i}.txt', 'r') as f:
            a = f.read()
    except Exception as error:
        print(f"files/{i}.txt not found.")

print("Searching all files is finished.")
