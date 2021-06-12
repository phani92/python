# Student library management system
# Implement a student library system using oops where students can borrow a book from the list of books.
# Create a separate library and student class.
# Your program must be menu driven.
# You are free to choose methods and attributes of your choice.

# Globals
studentObjList = []
libObjList = []
mainMenu = ['<1> Add student',
            '<2> Show list of students',
            '<3> Show list of departments',
            '<4> Exit']

# Classes


class Student:
    id = 1
    books = []

    @classmethod
    def incrementId(cls):
        cls.id += 1

    def __init__(self, name):
        self.name = name
        self.id = Student.id
        Student.incrementId()

    def showDetails(self):
        print(f"Name: {self.name} and ID: {self.id}")


class Library:

    def __init__(self, dept, listOfBooks):
        self.dept = dept
        self.listOfBooks = listOfBooks


def addStudent():
    name = str(input("Enter students name\n"))
    studentObjList.append(Student(name))
    print("Student successfully added!")

def reqHandle(inp):
    reqMenuStr = '''
                    <1> Show Books
                    <2> Request Book
                    <3> Add/Return Book
                    <4> Back\n'''
    library = libObjList[inp].listOfBooks

    while(True):
        choice = int(input(reqMenuStr))

        if choice == 1:
            print("List of available books are:")
            for index, item in enumerate(library):
                print(f"  <{index+1}> {item}")

        elif choice == 2:
            book = input("Enter the book you want to borrow.\n")
            if book in library:
                library.remove(book)
                print(f"You have been successfully issued the book, {book}.")
            else:
                print(f"This {book} is not available.")

        elif choice == 3:
            book = input("Enter the book you want to return.\n")
            library.add(book)
            print(f"Thank you for returning the book, {book}.")

        elif choice == 4:
            break

        else:
            print("Invalid Choice")



def handleDept():
    deptMenuStr = ""
    # Display departments
    for index, item in enumerate(libObjList):
        deptMenuStr += f"  <{index+1}> {item.dept} \n"
    deptMenuStr += f"  <{len(libObjList)+1}> Back"
    deptMenuStr = deptMenuStr[1:]

    # starts a loop to choose between departments
    while(True):
        print(f"List of available departments \n {deptMenuStr}")
        inp = int(input("select a department\n")) - 1

        if(inp < len(libObjList)):
            # Handle student request
            reqHandle(inp)

        elif(inp == len(libObjList)):
            break

        else:
            print("invalid choice")

# static function to create libraries for different departments


def addExampleLibraries():
    lib_eee = Library("EEE", ['Electrical-Machines', 'Network-Theory', 'HVDC'])
    libObjList.append(lib_eee)

    lib_cse = Library("CSE", ['Basic-Programming', 'C', 'Java'])
    libObjList.append(lib_cse)

    lib_mech = Library("MECH", ['fem', 'mefa', 'fdhm'])
    libObjList.append(lib_mech)


if __name__ == "__main__":

    # Stringify the elements in the list of main menu
    mainMenuStr = "  " + "\n \t\t\t".join(mainMenu)
    addExampleLibraries()

    while(True):
        try:
            choice = int(
                input(f'''
                ****** Welcome to Central Library ****** \n
                       Choose from the below options:\n
                      {mainMenuStr}\n'''))

            # options ladder
            if(choice == 1):
                addStudent()

            elif(choice == 2):
                for item in studentObjList:
                    item.showDetails()

            elif(choice == 3):
                handleDept()

            elif(choice == 4):
                print("Thank you for using the Central Library.")
                exit()

            else:
                print("Enter a valid choice")

        except Exception as error:
            print(error)
