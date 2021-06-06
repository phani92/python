# Python

- Collection of python implementations.
- Personal notes.
- If anything is useful please feel free to use them.
- Everything in python is object.
- `pip freeze > requirements.txt` creates a list of installed modules and copies the text into the text file.
- Special shout out to [Harry](https://www.codewithharry.com/) for the amazing course and practice problems.

## Variables and data types

- Integers
- Floating points
- strings
- Variable names are case sensitive
- `Dunder` or `magic` methods in Python are the methods having two prefix and suffix underscores in the method name. Eg: `__Init__`

## Print statement

- print(type(<variable>))
- print(<variable>)

## Strings

- Single quotes - 'Hello' -
- Double quotes - "Hello's" - Use this if there are single quotes in the string.
- Triple quotes - '''Hello''' -
- A string can be added directly - a + b
- `skip` is a keyword to skip characters in a string.
- `find` - It finds the index of first occurrence of the word in the string.
- `replace` - It replaces all the words in a string.
- `Escape sequence characters` - For example `\n` for next line or `\t` for a tab space can be used inside a string of double quotes. - "I am \n doing great.". - It will print "doing great" in next line.
- `oldWord` and `newWord`
- Care needs to be taken that the variable is assigned again to a new variable or the applied method is lost. `x = x.replace('")`
- `(f"string{varName}")` - this is a formatted string where varName is replaceable.

## Lists and Tuples

### `List`

- It is an ordered list similar to an array.
- It can be created using `[]`
- Access using index using `a[0]` etc..
- A list can be created using multiple data types. In the same list there can be numbers, strings etc..
- List slicing can be done with the help of `slicing` - `variable[0:n]`
- `List methods` - these methods are applied to the direct list itself.
  - `<list>.sort()` - sorts the list
  - `<list>.reverse()` - reverses the list
  - `<list>.insert(<num>)` - Adds <num> at the end of the list
  - `<list>.pop(<index>)` - Removes element at <index>
  - `<list>.remove(<val>)` - Removes the respective value from the list.

### `Tuples`

- It can be created using `()`.
- Tuple does not allow update of elements inside it.
- Tuple can be created in the following ways
  - Empty tuple - `t1 = ()`
  - tuple with single element - `t1 = (1,)` "The comma is important"
  - tuple with multiple elements - `t1 = (1,2,3,4)`
- Methods
  - print
  - index
  - count

## Dictionary and sets

### Dictionary

- Collection of key value pairs
- syntax

  ```
    myDict = {
      "Key": "Value",
    }

    print(myDict['key'])
  ```

- Properties:
  - It is unordered
  - It is mutable that means a value can be changed.
  - It is indexed
  - Does not allow adding duplicate keys
- Methods:
  - `dict_keys` - It gives the list of the keys in a dictionary.
  - `dict_values` - It gives the list of the values in a dictionary.
  - `dict_items` - it gives the (key, value) of all the contents of a dictionary.
  - `myDict.update(dictStruct)` - It updates the dict with the new key, value pair.
  - `myDict.get('key')` - It fetches the value of the respective key from the dictionary. There can be a question that instead of using get method why cant we use index to fetch the value ? That is something like `myDict['key']` which will also return the value correctly. But when the key we are searching is not present in the list then the index method returns error and get method returns `none`. Therefore to avoid errors it is better to use `get` method.

### Sets

- Set is a collection of non repetitive elements.
  - syntax
    ```
      a = {1,2,3,4,5}
    ```
- Empty set:
  ```
    a = {} # This syntax will create an empty dictionary and not an empty set.
    b = set() # This is correct
  ```
- Properties:
  - Unordered
  - unindexed - that means the elements cannot be accessed by index
  - There is no way to change items in sets
  - It does not allow duplicate values
- Methods:
  - `s.add` - a.add(x) adds element into the set
  - One cannot add a list into the set. Example: `s.add([4,5,6])` is not supported. But it supports adding tuple into the set, i.e `s.add(4,5,6)` is supported. Therefore, list and dicts cannot be added into the set as they are not hashable.
  - `s.len` - returns length of the set
  - `s.remove` - If we try to remove any element that is not present in the set then the python compiler will throw an error.
  - `s.pop` - removes any element from the set.
  - `s.clear` - clears the set
  - `s.union` - returns a new set with the elements from two sets.
  - `s.intersection` - returns a set with only the common items.

## Conditional expressions

- `if else if ladder`
  ```
    if (condition):
      # code
    elif (condition):
      # code
    else:
      # code
  ```
- `multiple if conditions`
  ```
    if (condition):
      # code
    if (condition):
      # code
    else:
      # code
  ```

## Loops

- There are two types of loops, namely `while` and `for` loops
- `while` - The block executes until the condition is true.
  ```
    while (condition):
      # statements
  ```
- `for` - Iterates through a sequence list
  ```
    for item in list:
      # statements
  ```
  - `range` - `for(itrStartVal, itrEndVal, itrStepVal)`
  ```
    for i in range(8):
      # iterates until 7
  ```
  ```
    for i in range(2,8):
      # starts from 2 and iterates until 7
  ```
  ```
    for i in range(2,8,2):
      # starts from 2 and iterates until 7 with a step of 2
  ```
  - `else`
  ```
    for i in range(n):
      # iterates until n
    else:
      # do something
  ```
  - `break` - it breaks and ends the loop

## Functions

- syntax
  ```
    def <funcName>:
      # Do anything
      # Return
  ```
- default arguments
  ```
    def funcName(name="stranger"):
      # default value is used as `stranger` if no value is specified in name
      # Do anything
      # Return
  ```

## Files

- Use files to store in nvm
- There are two types of files: `textFiles` and `binaryFiles`
- Operations
  - open('FileName','Mode')
    ```
    f = open('xyz.txt','r')
    ```
  - By default the mode is 'r' which is for reading.
  - other modes are 'w' (writing), 'a' (appending) and '+' (updating).
  - Additional modes are 'rb' for read in binary mode and 'rt' will open for read in text mode.
  - close
    ```
    f.close()
    ```
  - read
    - `f.read()` to read the file.
    - `f.read(n)` to read the first n characters in a file.
    - `f.readLine()` to read one line from the file.
  - `with` is called as context mode. When a file is opened using `with` parameter then it is not required to close the file.
    ```
      with open('fileName','r') as f:
        a = f.read()
    ```

## Object Oriented Programming

- `DRY` principle
- class and objects similar to c++
- in python we identify them as:
  ```
  Noun - class
  Adjective - attributes
  Verbs - methods
  ```
- syntax - `var = class()`.
- objects of a given class can invoke the methods available to it without revealing the implementation details to the user. This is called as `Abstraction` and `encapsulation`.
- class attributes can be directly changed by accessing the element.

  ```
    class employee:
      company = "Avion"

    employee phani
    print(phani.company) # will print Avion
    employee.company = "AvionReturns"
    print(phani.company) # will print AvionReturns as the class attribute value was changed.
  ```

- `Instance attributes` are the elements of the class for a particular object.
- Instance attribute take preference over class attribute. If any attribute that is not defined in the class is tried to be accessed then the compiler will throw an error.
- `self` is similar to `this` of c++.
- `static method decorator` - Sometimes we need a function that does not use the self parameter. In such a case we can define a static method like this:
  ```
  @staticmethod
  def greet():
    print("Hello")
  ```
- `constructor` - similar to c++, it is run first when the object is created.
  ```
  class employee:
    def __init__(self):
      print("Employee is created")
  ```
  - The parameter `self` can be given any identifier name. It does not have to be `self` only.
  ```
  def __init__(self):
  # is equal to
  def __init__(anyVal)
  ```
  - If there are positional arguments in the constructor then they have to be given during the initialization of an object.

## Inheritance

- A derived class can be created using a base class which will inherit all the properties of the base class.

  - Syntax with example:

  ```
  class Base:
    company = "Google"

    def showDetails(self):
      print(f"The employee works for {self.company}")

  class Derived(Base):
    product = "Youtube"
  ```

  - Important about `virtual functions` - the derived class can simply overwrite the base class's identical function by having a definition for it in the body of the derived class.

- Types:

  - Single inheritance - single parent and single child

  ```
  class Base:
    #Body

  class Derived(Base):
    # Body
  ```

  - Multiple inheritance - Two parent classes and single child

  ```
  class Base1:
    #Body

  class Base2:
    #Body

  class Derived(Base1, Base2):
    #
  ```

  - Multilevel inheritance - It is a cascading inheritance.

  ```
  class Base:
    # Body

  class Derived(Base):
    # Body

  class SubDerived(Derived):
    # Body
  ```

  - Precedence of execution of functions depends on the availability.
    - If a function is present in all the classes, i.e parent and child then the function in the child class will be executed.
    - If a function is present in the base class and derived class then the sub-derived class takes the function from the derived class.
    - If a function is present only in base class then there is no other option except using it directly.

- `super` method allows the function to also use the function from the base class.

  ```
  class Base:
    def exampleFunc(self):
      # Body

  class Derived(Base):
    def exampleFunc(self):
      super().exampleFunc()
      # The above line will use the function from the base class
  ```

- `Class` method - It is related to the class and not instance. there are two ways of accessing a element of the class and updating it.
  - method 1:
  ```
  def changeSalary(self, sal):
    self.__class__.salary = sal
  ```
  - method 2 using decorator:
  ```
  @classmethod
  def def changeSalary(cls, sal):
    cls.salary = sal
  ```
- `Property` decorator, there can be instances when a property is dependent on other members of the class. If these properties or variables are hardcoded then it is not easy to maintain these variables as all of them have to be changed by using methods or writing functions to set/get them. To ease this situation there is a feasibility in python to use property decorator.
  - syntax for getter:
    ```
    @property
    def <variableName>(self):
      return class.var1 + class.var2
    ```
  - syntax for setter:
    ```
    @property.setter
    def <variableName>(self, val):
      self.<var1> = val - var2
    ```
- `overloading of operators` - operators in python can be overloaded using dunder methods. It is about basically overloading or replacing the functionality of a default operator like `+` or `-` with custom defined functions as explained in the example `operatorOverloading.py`
- In the python documentation it is given which operators can be overloaded like `__Add__` or `__Mul__` etc... For complete lists checkout the [link](https:#www.python-course.eu/python3_magic_methods.php)

# Advanced Python

## Generic

### Main

- When files need to be imported and we want only a section of code from it to be executed then the program can be isolated using `__name__ == __main__`. It also acts as an entry point for the module similar to java or c++.

  - syntax and example:

    ```
    program_1:
      def egFunc:
        # Do something

      if __name__ == "__main__":
        print("this line will print only in program_1")

    program_2:
      import program_1

      program_1.egFunc()
      # The print statement will not be printed as it is inside __main__ condition.
    ```

### Global

- Accesses the global variables inside functions etc.. They can also be used to modify the variable outside of the current scope.
  - syntax
    ```
    global <var>
    ```

### Enumerate function

- It can be used in a for loop to enumerate a list. It basically also provides the index of the item in the list.
  - Syntax
    ```
    for index, item in enumerate(list):
      # index will return the index of the item in the list
    ```

### List comprehensions

- A line of code can be included in the list creation var `[]` which will consider the condition before populating the list.
  - syntax with example
    ```
    list1 = [3,45,6,7,8,9,10]
    # populates list with even numbers in list2 - comprehensive list
    list2 = [i for i in list1 if i%2==0]
    ```

## Exception handling in python

- `Try` and `except` are for handling errors and exceptions during the execution of the code. `Else` is also available to handle the case when `try` was successful
  - Syntax:
    ```
    try:
      # Regular block of statements
    except Exception as <var to store error code>
      # Block of statements to be executed when there is an error
    else:
      # statements to execute when `try` was executed successfully
    ```
  - There are different exception codes to handle errors, example `zeroDivisionError`, `TypeError` etc..
    - syntax:
    ```
    try:
      # Block of statements
    except zeroDivisionError:
      # Block of statements
    except TypeError:
      # Block of statements
    ```
  - `Try` with `finally` - It executes a piece of code when there is an exception and we need to handle a use-case such that a section of code is executed.
    - syntax:
    ```
    try:
      # Block of statements to execute
    except zeroDivisionError:
      # Block of statements to handle error
    finally:
      # Block of statements to finish
      # Important is it will be executed even if the program is exited in any of the above cases
    ```

## Virtual Environment

- It is an environment which is same as the system interpreter but is isolated from the other python environments on the system.
- It creates an independent python environment which seems to be similar to the one installed in the local system.
- When you want to use a python lib/module which has to be different to the one installed in the local system then a virtual environment can be created.
- Install `virtualEnv`
- Command to fire a project in virtual environment `virtualenv <projectName>`.
  - For linux users to activate the project use the command: `source <projectName>/bin/activate`
  - Windows users: `.\<projectName>\scripts\activate.ps1`
- All the packages required in the project are to be installed in the virtual environment.
- In the command shell, if a virtual environment is running then the project name can be seen in front.
  - `<projectName> PS D: bla bla path\pythonShell`
- To deactivate the environment, enter `deactivate`
- To delete a virtual environment, just delete the folder.
- `pip freeze > requirements.txt` can be used to save all the required pip modules for the project.
- When `pip install -r .\requirements.txt` is executed it will install all the modules listed in the txt file.

## Lambda functions

- Instead of defining a one liner functions, lambda functions can be used to created a small function.

  - syntax with example:

    ```
    def square(n):
      return n*n

    # The above function can also be written as follows:

    square = lambda n : n*n
    ```

## Bin - Join

- Creates a string from iterable objects.
  - syntax:
    ```
    list = ["str1", "str2", "str3"]
    combined_string = "and".join(list)
    ## output will be str1 and str2 and str3
    ```

## Format method - strings

- It is similar to `fString`
- In previous versions of python there was no `fString` and therefore format method was used.
  - syntax with example:
    ```
    name = "Phani"
    channel = "TravelWithPhani"
    str = "This is {} and his channel is {}".format(name, channel)
    ```

## Maps

- It can take a list and map a function to the input such that an output list is created with corresponding output for every input.

  - syntax with example:

    ```
    def square(n):
      return n*n

    list1 = [1,2,3,4,5]
    list2 = list(map(square, list1))
    # output is [1,4,9,16,25]
    ```

## Filter

- It creates a list of items for which the function returns true.
- syntax
  ```
  list(filter(<function>,<list>))
  ```
- a lambda function can also be used in the place of function.

## Reduce

- It has to imported from `functools`
- It applies a rolling computation to sequential pair of elements.
- syntax:
  ```
  val = reduce(<function>, <list>)
  ```
- It applies the function on the elements in the list and gives the final output. Example, sum of all the integers in the list.
