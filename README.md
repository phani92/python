# Python

- Collection of python implementations.
- Personal notes.
- If anything is useful please feel free to use them.
- Everything in python is object

## Variables and data types

- Integers
- Floating points
- strings
- Variable names are case sensitive

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
    a = {} // This syntax will create an empty dictionary and not an empty set.
    b = set() // This is correct
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
      // code
    elif (condition):
      // code
    else:
      / /code
  ```
- `multiple if conditions`
  ```
    if (condition):
      // code
    if (condition):
      // code
    else:
      / /code
  ```

## Loops

- There are two types of loops, namely `while` and `for` loops
- `while` - The block executes until the condition is true.
  ```
    while (condition):
      // statements
  ```
- `for` - Iterates through a sequence list
  ```
    for item in list:
      // statements
  ```
  - `range` - `for(itrStartVal, itrEndVal, itrStepVal)`
  ```
    for i in range(8):
      // iterates until 7
  ```
  ```
    for i in range(2,8):
      // starts from 2 and iterates until 7
  ```
  ```
    for i in range(2,8,2):
      // starts from 2 and iterates until 7 with a step of 2
  ```
  - `else`
  ```
    for i in range(n):
      // iterates until n
    else:
      // do something
  ```
  - `break` - it breaks and ends the loop

## Functions
- syntax
  ```
    def <funcName>:
      // Do anything
      // Return
  ```
- default arguments
  ```
    def funcName(name="stranger"):
      // default value is used as `stranger` if no value is specified in name
      // Do anything
      // Return
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
  