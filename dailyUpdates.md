# Daily Updates For My Progress (100 days of code)

## Day 0: 28/11/2022

**Today's Progress**: I learn about the basic things what is programming and what is python? when its developed, whom is developed etc?

## Day 1: 29/11/2022

**Today's Progress**:Today I check how cool projects we can build using python...

## Day 2: 30/11/2022

**Today's Progress**:Today I learn How to integrate others' code into our code base and that integration, we called a module in python. it's simply a '.py' file that we install using a pip command.

for ex. pip install django

## Day 3: 01/12/2022

**Today's Progress**:
programming in python and let's start with the print function, 'print()' this is a print function in python, and note that in python everything is an object, so whatever you put inside that print function parenthesis of the print function will give you the output in the console,

suppose print('hello world')
this will give the result in the console, why quotes?
because python will get to know that you want to print as it is.

## Day 4: 02/12/2022

**Today's Progress**:
Learn about comments, multiline comments, escape sequence characters,
comments: Just write the notes inside the code for future reference and it did not print by python, for implementing the code just use the # before your notes,
whatever after the # sign is considered as comments.
Multiline Comments: so this is helpful while writing the paragraphs like sentences 5 or 6 lines of code, this will look nice, for making a multiline comment put notes inside triple single or double quotes like '''your multiline notes''' or """your multiline notes"""
Escape Sequence Character: just word sounds, it helps to put some kind of special character inside a string ex., \n (new line), \t (tab), etc.

## Day 5: 03/12/2022

**Today's Progress**:
Lets jump into the Programming fundamentals (Variables and Data types)

1. Variables: What is variables? as the name says anything that varies, so in programming if you want to save a value(data type) for future reference or reusability purpose we called that term a variables

   for ex a = 10
   so 'a' is a variable name that holds the memory address of the value 10. so 10 store somewhere in the ram.

   Variable is a container that stores the memory address of the particular data type

2. Data Types: the classification of the single value, to know what kind of values we are using in the program, so some classifications are provided by the python language. let see each classifications

   In real world we have numbers, various types of numbers, in python also we have numbers

   Number:

   a. Int: Int specifies the whole numbers like(0,1,20,-20,3)

   b. float: Float specifies the value with the decimal points (1.5, 20.00, -3.6)

   c. complex specifies real and imagenary numbers (8+2j)

   After we have characters, word

   a. str: it's a string type often we say collection of characters, well string is also considered a data structure if it store single character then its called data type or if it store more than single character its called data structure

   Boolean

   a.bool: Bool specifies the boolean field that stores only two values like True or False, Yes or No, 0 or 1 its based on boolean algebra, majorly boolean fields helps to anticipating the flow of the programme.

## Day 6: 04/12/2022

**Today's Progress**:
Lets learn operators

what is operator?
Operator is simply the symbol that helps to perform some operations on datatypes and it return a single down a single value

- There are 7 types of operators

1. Arithmetic Operator
2. Relational/Comparison Operator
3. logical operator
4. Assignment Operator
5. Bitwise Operator
6. Identity Operator
7. Membership Operator

Arithmetic Operator:
It simply helps to perform arithmetic operations like addition subtraction, multiplication, division etc

      |Symbol         | Example|
      |---------------|--------|
      |Addition(+)    | 15+7   |
      |subtraction    | 15-7   |
      |division       | 15/7   |
      |modulo         | 15%7   |
      |multiplication | 5*6    |
      |exponention    | 3**3   |
      |floor division | 15//7  |

<!-- 05/12/2022 -->

## Day 7: 05/12/2022

Relational/Comparision Operator:
As the Name shows it is compare the two or more data types with each other and it return the boolean value like True or False.

      |Symbol                | Example|
      |----------------------|--------|
      |greater than (>)      | 5 > 3  |
      |less than (<)         | 7 < 15 |
      |greater than equal(>=)| 6 >= 6 |
      |less than equal(<=)   | 15<=7  |
      |equal (==)            | 5==5   |
      |Not Equal (!=)        | 2!=3   |

<!-- 06/12/2022 -->

## Day 8: 06/12/2022

Logical Operator:
Here we are checking two or more conditions, which we check if two conditions are true then true or either one condition true then true.

      |Symbol      |      Example     |
      |------------|------------------|
      |and         | 5 > 3 and 2 == 2 |
      |or          |7 < 15 or 5>10    |
      |not         |not True not False|

Assignment Operator: this operator symbol helps to assign value to the variable, right hand side value assign to the left hand side.

Ex. name = 'ashwin' so , ashwin name will stored in left hand side of name variable

Bitwise Operator:
In Python, bitwise operators are used to performing bitwise calculations on integers. The integers are first converted into binary and then operations are performed on each bit or corresponding pair of bits, hence the name bitwise operators.

SO thats why I avoided it.

Identity Operator:
is and is not are the identity operator as the name says it checks the identity means it check if the objects memory address same or not.

Membership Operator:
if the object is exists in the sequence of objects or in data structure, its called membership operator its check using 'in' and 'not in'.

This are the 7 types of operators.

### Typecasting in python

changing one datatype to another is called type casting

int(), float(), str(), ord() etc

There are two way to do the typecasting.

1. Explicit Typecasting: Explicitly tell the python to changing data type to another

For ex a = '1' --> int(a) = it converts into integer.

2. Implicit Typecasting: here python will take care of the type casting in certain cases to avoid data loss

For ex a = 12/3 --> it will automatically return 4.0 i.e in a float data type

## Day 9: 07/12/2022

**Today's Progress**:
Lets learn input() function in python

Simply means ask the user to type your choice in the programme, it is workable in console.

disclaimer: its return a string object, if you give number also its return a string only, means data type in a string.

## Day 10: 08/12/2022

**Today's Progress**:
Lets dive into the string

What are the strings?
strings is just a sequence of characters and its an data structure in python, that contains more than two characters and its a sequential data structure means its store value as it is.

we can create a string by enclosing a character in single quotes as well as double quotes in python, both considered the same thing.

It's an immutable data structure means modification is not going to happen here

Strings is an sequential data structure so it support sequence operations :

1. Indexing
2. slicing
3. adding
4. multiplying
5. checking for membership
6. len
7. min
8. max

In python we have multi line string also by enclosing in a triple quotes

'''< multiline string >'''
"""< multiline string >"""
Accessing the string:

1. using indexing (mechanism for accessing each data structure by providing there positions in a integer format, its starts from 0.)
2. using loops specially for loopss

## Day 11: 09/12/2022

**Today's Progress**:
Lets gone through slicing in strings (part of it.)

so string is a combination of characters, so using slicing we can extract some character for ex, 'ashwin' its a 6 letter of word but i want first 3 character, using slicing we can achieve it.

name = 'ashwin'
print(name[0:3]) # indexing start from 0 and slicing second position number is always excluded
so it return ash.

**There are negeative slicing also**
same example, if i want 'in' from 'ashwin' name using negative slicing

name[-2:-1] --> name[len(name) - 2: len(name) -1] == name[4:5]

len is a function in python that helps get the string length.

## Day 12: 10/12/2022

**Today's Progress**:
Lets learn about some string methods

what are string method?, its simply a functions that give some sort of functionality to work with strings.

Main Thing about string is **Strings are the immutable data structure**
Due to immutability we can't do the inplace changes i.e., it return a copy of the string

# String methods

Python provides a set of built-in methods that we can use to alter and modify the strings.

## upper() :

The upper() method converts a string to upper case.

### Example:

```python
str1 = "AbcDEfghIJ"
print(str1.upper())
```

### Output:

```
ABCDEFGHIJ
```

## lower()

The lower() method converts a string to lower case.

### Example:

```python
str1 = "AbcDEfghIJ"
print(str1.lower())
```

### Output:

```
abcdefghij
```

## strip() :

The strip() method removes any white spaces before and after the string.

### Example:

```python
str2 = " Silver Spoon "
print(str2.strip)
```

### Output:

```
Silver Spoon
```

## rstrip() :

the rstrip() removes any trailing characters.
Example:

```python
str3 = "Hello !!!"
print(str3.rstrip("!"))
```

### Output:

```
Hello
```

## replace() :

The replace() method replaces all occurences of a string with another string.
Example:

```python
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
```

### Output:

```
Silver Moon
```

## split() :

The split() method splits the given string at the specified instance and returns the separated strings as list items.

### Example:

```python
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".
```

### Output:

```
['Silver', 'Spoon']
There are various other string methods that we can use to modify our strings.
```

## capitalize() :

The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

### Example:

```python
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
```

### Output:

```
Hello
Hello world
```

## center() :

The center() method aligns the string to the center as per the parameters given by the user.

### Example:

```python
str1 = "Welcome to the Console!!!"
print(str1.center(50))
```

### Output:

```
            Welcome to the Console!!!
```

We can also provide padding character. It will fill the rest of the fill characters provided by the user.

### Example:

```python
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))
```

### Output:

```
............Welcome to the Console!!!.............
```

## count() :

The count() method returns the number of times the given value has occurred within the given string.

### Example:

```python
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)
```

### Output:

```
4
```

## endswith() :

The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

### Example :

```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
```

### Output:

```
True
```

We can even also check for a value in-between the string by providing start and end index positions.

### Example:

```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
```

### Output:

```
True
```

## find() :

The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

### Example:

```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
```

### Output:

```
10
```

As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

### Example:

```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))
```

### Output:

```
-1
```

## index() :

The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

### Example:

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
```

### Output:

```
13
```

As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

### Example:

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))
```

### Output:

```
ValueError: substring not found
```

## isalnum() :

The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

### Example 1:

```python
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
```

Output:

```
True
```

## isalpha() :

The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

### Example :

```python
str1 = "Welcome"
print(str1.isalpha())
```

### Output:

```
True
```

## islower() :

The islower() method returns True if all the characters in the string are lower case, else it returns False.

### Example:

```python
str1 = "hello world"
print(str1.islower())
```

### Output:

```
True
```

## isprintable() :

The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

### Example :

```python
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
```

### Output:

```
True
```

## isspace() :

The isspace() method returns True only and only if the string contains white spaces, else returns False.

### Example:

```python
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
```

### Output:

```
True
True
```

## istitle() :

The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

### Example:

```python
str1 = "World Health Organization"
print(str1.istitle())
```

### Output:

```
True
```

### Example:

```python
str2 = "To kill a Mocking bird"
print(str2.istitle())
```

### Output:

```
False
```

## isupper() :

The isupper() method returns True if all the characters in the string are upper case, else it returns False.

### Example :

```python
str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())
```

### Output:

```
True
```

## startswith() :

The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

### Example :

```python
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))
```

### Output:

```
True
```

## swapcase() :

The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

### Example:

```python
str1 = "Python is a Interpreted Language"
print(str1.swapcase())
```

### Output:

```
pYTHON IS A iNTERPRETED lANGUAGE
```

### title() :

The title() method capitalizes each letter of the word within the string.

### Example:

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
```

### Output:

```
He'S Name Is Dan. Dan Is An Honest Man.
```

## Day 13: 11/12/2022

**Today's Progress**:
Lets learn Conditional/flow control Statements

It helps to anticipate the conditions,
based on the condition act upon it.

```
If something happen:
      Do something
else:
      do another thing
```

**Types of Conditional statements**

1. If consitional statements
2. if_else
3. if - elif - else
4. nested if.

- if conditional statements:<br>
  Just checking the single condition, if false continue with other statements.

- if_else:<br>

Execute the block of code inside if statement. After execution return to the code out of the if??????else block.\

### if the expression evaluates False:

Execute the block of code inside else statement. After execution return to the code out of the if??????else block.

## Example:

```python
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```

## Output:

```
Alexa, do not add Apples to the cart.
```

- elif:<br>
  Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

### Working of an elif statement

Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.\
.\
.\
.\
Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

## Example:

```python
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")
```

## Output:

```
Number is Zero.
```

- nested if:<br>
  We can use if, if-else, elif statements inside other if statements as well. \
  Example:

```python
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
```

Output:

```
Number is between 11-20
```

## Day 14: 12/12/2022

**Today's Progress**:

Exercise: based on time greet the user using time module.

## Day 15: 13/12/2022

**Today's Progress**:
Lets look into the match case newly launched in python3.10

### **Match Case**

So match case is released in python3.10

It similarly a switch cases in c / c++

A match statement will compare a given variable???s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

1. The match keyword
2. One or more case clauses
3. Expression for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

## Syntax:

```python
match variable_name:
            case ???pattern1??? : //statement1
            case ???pattern2??? : //statement2
            ???
            case ???pattern n??? : //statement n
```

## Day 16: 14/12/2022

**Today's Progress**:
Loops

loops means do things in an iterative manner.

In programming also loops do the same things, keep doing it until the condition are met False.

# Introduction to Loops

Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

- for loop
- while loop

# The for Loop

for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

## Example: iterating over a string:

```python
name = 'Abhishek'
for i in name:
    print(i, end=", ")
```

## Output:

A, b, h, i, s, h, e, k,

## Example: iterating over a list:

```python
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
```

## Output:

Red\
Green\
Blue\
Yellow

Similarly, we can use loops for lists, sets and dictionaries.

## range():

What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

## Example:

```python
for k in range(5):
    print(k)
```

## Output:

0\
1\
2\
3\
4\
Here, we can see that the loop starts from 0 by default and increments at each iteration.

But we can also loop over a specific range.

## Example:

```python
for k in range(4,9):
    print(k)
```

## Output:

4\
5\
6\
7\
8

## Quick Quiz

Explore about third parameter of range (ie range(x, y, z))

## Day 17: 15/12/2022

**Today's Progress**:
lets look into the while loop

while loop is one of the loop type in python

When to use for loop and while loop?
when you know the length of the iteration that time use for loop and otherwise when you don't know how many times you want iteration then use while loop.

# Python while Loop

As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

## Example:

```python
count = 5
while (count > 0):
  print(count)
  count = count - 1
```

## Output:

```
5
4
3
2
1
```

Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.

# Else with While Loop

We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

## Example:

```python
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
```

## Output:

```
5
4
3
2
1
counter is 0
```

# Do-While loop in python

do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

# How to emulate do while loop in python?

To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

## Example

```python
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
```

## Output

```
Enter a positive number: 1
1
Enter a positive number: 4
4
Enter a positive number: -1
-1
```

## Explanation

This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.

## Day 18: 16/12/2022

**Today's Progress**:
Break and continue

break and continue are the keywords in python.It helps to control the loop

# break statement

The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

## example

```python '
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")
```

### output

```
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
.
.
.
50 Mississippi
```

## Continue Statement

The continue statement skips the rest of the loop statements and causes the next iteration to occur.

## example

```python
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)
```

## output

```
2
4
6
8
0

```

## Day 19: 17/12/2022

**Today's Progress**:
Functions in Python

What are the functions?
The functions are the reusable code or logic that helps to avoid the code redundency or rewritting the same logic again and again.

**Types of functions**

1. Built-in-Functions
2. User_defined functions

## Built-in functions:

These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

## User-defined functions:

We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

### Syntax:

```python
def function_name(parameters):
  pass
  # Code and Statements
```

- Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
- Any parameters and arguments should be placed within the parentheses.
- Rules to naming function are similar to that of naming variables.
- Any statements and other code within the function should be indented.

### Calling a function:

We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

Example:

```python
def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")
```

Output:

```
Hello, Sam Wilson
```

## Day 20: 18/12/2022

**Today's Progress**:
Function parameters and arguments

Parameters are used when we define the function using def and in paranthesis we tell the function that in future i am passing that much inputs for processing.

Arguments are the used on the time of calling the function.

**Types of Arguments**

1. Positional Arguments (required arguments)
2. Default arguments
3. keyword arguments(named arguments)

### Required arguments:

In case we don???t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

Example 1: when number of arguments passed does not match to the actual function definition.

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")
```

Output:

```
name("Peter", "Quill")\
TypeError: name() missing 1 required positional argument: 'lname'
```

Example 2: when number of arguments passed matches to the actual function definition.

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")
```

Output:

```
Hello, Peter Ego Quill
```

### Default arguments:

We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

Example:

```python
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
```

Output:

```
Hello, Amy Jhon Whatson
```

### Keyword arguments:

We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

Example:

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
```

Output:

```
Hello, Jade Peter Wesker
```

### Variable-length arguments:

Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

#### Arbitrary Arguments:

While creating a function, pass a \* before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

Example:

```python
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
```

Output:

```
Hello, James Buchanan Barnes
```

#### Keyword Arbitrary Arguments:

While creating a function, pass a \* before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

Example:

```python
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")
```

Output:

```
Hello, James Buchanan Barnes
```

# return Statement

The return statement is used to return the value of the expression back to the calling function.

Example:

```python
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
```

Output:

```
Hello, James Buchanan Barnes
```

## Day 21: 19/12/2022

**Today's Progress**:
Python Lists

List are the inbuilt datastructure in python, most used and a mutable type of data structure, and store data in a comma seperated values.

# Python Lists

- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are changeable meaning we can alter them after creation.

Example 1:

```python
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
```

Output:

```
[1, 2, 2, 3, 5, 4, 6]
['Red', 'Green', 'Blue']
```

Example 2:

```python
details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
```

Output:

```
['Abhijeet', 18, 'FYBScIT', 9.8]
```

As we can see, a single list can contain items of different data types.

# List Index

Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

#### Example:

```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
```

# Accessing list items

We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...

## Positive Indexing:

As we have seen that list items have index, as such we can access items using these indexes.

#### Example:

```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])
```

#### Output:

```
Blue
Green
Red
```

## Negative Indexing:

Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

#### Example:

```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])
```

#### Output:

```
Green
Blue
Red
```

## Check whether an item in present in the list?

We can check if a given item is present in the list. This is done using the `in` keyword.

```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
```

#### Output:

```
Yellow is present.
```

```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")
```

#### Output:

```
Orange is absent.
```

## Range of Index:

You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

Syntax:

```python
listName[start : end : jumpIndex]
```

Note: jump Index is optional. We will see this in later examples.

### Example: printing elements within a particular range:

```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'
```

#### Output:

```
['mouse', 'pig', 'horse', 'donkey']
['bat', 'mouse', 'pig', 'horse', 'donkey']
```

Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.

Note: The element of the end index provided will not be included.

### Example: printing all element from a given index till the end

```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes
```

### Output:

```
['pig', 'horse', 'donkey', 'goat', 'cow']
['horse', 'donkey', 'goat', 'cow']
```

When no end index is provided, the interpreter prints all the values till the end.

### Example: printing all elements from start to a given index

```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes
```

#### Output:

```
['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
```

When no start index is provided, the interpreter prints all the values from start up to the end index provided.

### Example: Printing alternate values

```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes
```

### Output:

```
['cat', 'bat', 'pig', 'donkey', 'cow']
['dog', 'mouse', 'horse', 'goat']
```

Here, we have not provided start and index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.

### Example: printing every 3rd consecutive value withing a given range

```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])
```

### Output:

```
['dog', 'pig', 'goat
```

Here, jump index is 3. Hence it prints every 3rd element within given index.

# List Comprehension

List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

## Syntax:

List = [Expression(item) for item in iterable if Condition]

**Expression**: It is the item which is being iterated.

**Iterable**: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

**Condition**: Condition checks if the item should be added to the new list or not.

### Example 1: Accepts items with the small letter ???o??? in the new list

```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
```

### Output:

```
['Milo', 'Bruno', 'Rosa']
```

### Example 2: Accepts items which have more than 4 letters

```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
```

### Output:

```
['Sarah', 'Bruno', 'Anastasia']
```

## Day 22: 20/12/2022

**Today's Progress**:

List methods

# List Methods

## list.sort()

This method sorts the list in ascending order. The original list is updated

### Example 1:

```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
```

### Output:

```
['blue', 'green', 'indigo', 'voilet']\
[1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]

```

What if you want to print the list in descending order?\
We must give reverse=True as a parameter in the sort method.

### Example:

```python
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
```

#### Output:

```
['voilet', 'indigo', 'green', 'blue']
[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]
```

The reverse parameter is set to False by default.

Note: Do not mistake the reverse parameter with the reverse method.

## reverse()

This method reverses the order of the list.

#### Example:

```python
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
```

#### Output:

```
['green', 'blue', 'indigo', 'voilet']
[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]
```

## index()

This method returns the index of the first occurrence of the list item.

#### Example:

```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
```

Output:

```
1
3
```

## count()

Returns the count of the number of items with the given value.

#### Example:

```python
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
```

#### Output:

```
2
3
```

## copy()

Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

#### Example:

```python
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)
```

#### Output:

```
['voilet', 'green', 'indigo', 'blue']
['voilet', 'green', 'indigo', 'blue']
```

## append():

This method appends items to the end of the existing list.

#### Example:

```python
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)
```

#### Output:

```
['voilet', 'indigo', 'blue', 'green']
```

## insert():

This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

#### Example:

```python
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)
```

#### Output:

```
['voilet', 'green', 'indigo', 'blue']
```

## extend():

This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

#### Example 1:

```python
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
```

#### Output:

```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```

## Concatenating two lists:

You can simply concatenate two lists to join two lists.

#### Example:

```python
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
```

#### Output:

```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```

## Day 23: 21/12/2022

**Today's Progress**:

Tuples are the immutable data structure, it store the comma seperated values, it takes less memory than lists because it static in nature.

# Python Tuples

Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

### Example 1:

```python
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
```

### Output:

```
(1, 2, 2, 3, 5, 4, 6)
('Red', 'Green', 'Blue')
```

### Example 2:

```python
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
```

### Output:

```
('Abhijeet', 18, 'FYBScIT', 9.8)
```

# Tuple Indexes

Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.

### Example:

```python
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]
```

## Accessing tuple items:

### I. Positive Indexing:

As we have seen that tuple items have index, as such we can access items using these indexes.

Example:

```python
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]
print(country[0])
print(country[1])
print(country[2])
```

Output:

```
Spain
Italy
India
```

### II. Negative Indexing:

Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

### Example:

```python
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])
```

### Output:

```
Germany
India
Italy
```

## III. Check for item:

We can check if a given item is present in the tuple. This is done using the `in` keyword.

### Example 1:

```python
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
```

### Output:

```
Germany is present.
```

### Example 2:

```python
country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
```

### Output:

```
Russia is absent.
```

### IV. Range of Index:

You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

### Syntax:

```python
Tuple[start : end : jumpIndex]
```

Note: jump Index is optional. We will see this in given examples.

### Example: Printing elements within a particular range:

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes
```

### Output:

```
('mouse', 'pig', 'horse', 'donkey')
('bat', 'mouse', 'pig', 'horse', 'donkey')
```

Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.
Note: The element of the end index provided will not be included.

### Example: Printing all element from a given index till the end

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes
```

### Output:

```
('pig', 'horse', 'donkey', 'goat', 'cow')
('horse', 'donkey', 'goat', 'cow')
```

When no end index is provided, the interpreter prints all the values till the end.

### Example: printing all elements from start to a given index

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes
```

### Output:

```
('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
```

When no start index is provided, the interpreter prints all the values from start up to the end index provided.

### Example: Print alternate values

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes
```

### Output:

```
('cat', 'bat', 'pig', 'donkey', 'cow')
('dog', 'mouse', 'horse', 'goat')
```

Here, we have not provided start and end index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.

### Example: printing every 3rd consecutive withing given range

```python
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])
```

### Output:

```
('dog', 'pig', 'goat')
```

Here, jump index is 3. Hence it prints every 3rd element within given index.

## Day 24: 22/12/2022

**Today's Progress**:

# Manipulating Tuples

Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

#### Example:

```python
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
```

#### Output:

```
('Spain', 'Italy', 'Finland', 'Germany', 'Russia')
```

Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

However, we can directly concatenate two tuples without converting them to list.

#### Example:

```python
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
```

#### Output:

```
('Pakistan', 'Afghanistan', 'Bangladesh', 'ShriLanka', 'Vietnam', 'India', 'China')
```

# Tuple methods

As tuple is immutable type of collection of elements it have limited built in methods.They are explained below

## count() Method

The count() method of Tuple returns the number of times the given element appears in the tuple.

### Syntax:

```python
tuple.count(element)
```

### Example

```python
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
```

### Output

3

# index() method

The Index() method returns the first occurrence of the given element from the tuple.

### Syntax:

```python
tuple.index(element, start, end)
```

Note: This method raises a ValueError if the element is not found in the tuple.

### Example

```python
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)
```

#### Output

3

## Day 25: 23/12/2022

**Today's Progress**:

Lets do fizzbuzz

## Day 26: 24/12/2022

**Today's Progress**:

LEts build kbc

## Day 27: 25/12/2022

**Today's Progress**:

F'string' in python
f-strings in python gives you the more power. while printing in the console.

# String formatting in python

String formatting can be done in python using the format method.

```python
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```

# f-strings in python

It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

## Example

```python
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")
```

## Output:

```
Hello, My name is Tushar and I'm 23 years old.
```

In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them.

We can use it in a single statement as well.

## Example

```python
print(f"{2 * 30})"
```

## Output:

```
60
```

## Day 28: 26/12/2022

**Today's Progress**:

Doc-strings and pep8 (design standards)

# Docstrings in python

Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

## Example

```python
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

```

Here,

'''Takes in a number n, returns the square of n'''
is a docstring which will not appear in output

## Output:

```
25
```

Here is another example:

```python
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
```

## Python Comments vs Docstrings

### Python Comments

Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

### Python docstrings

As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

We can access these docstrings using the **doc** attribute.

## Python **doc** attribute

Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their **doc** attribute. We can later use this attribute to retrieve this docstring.

## Example

```python
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)
```

## Output:

Takes in a number n, returns the square of n

# PEP 8

PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

# The Zen of Python

Long time Pythoneer Tim Peters succinctly channels the BDFL???s guiding principles for Python???s design into 20 aphorisms, only 19 of which have been written down.

```Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Easter egg

```python
import this
```

## Day 29: 27/12/2022

**Today's Progress**:

Recursion In python

What is mean by recursion?<br>
Function call itself with a condition that tells to when to stop(caution: If you do not put condition it will goes into a infinite)

# Recursion in python

Recursion is the process of defining something in terms of itself.

## Python Recursive Function

In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

## Example:

```python
def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

# Driver Code
num = 7;
print("Number: ",num)
print("Factorial: ",factorial(num))
```

## Output:

```
number:  7
Factorial:  5040
```

## Day 30: 28/12/2022

**Today's Progress**:

Sets in Python

sets is a inbuilt unordered data structure that store the unique objects i.e., no duplicates

Ex.

```
info = {"Carla", 19, False, 5.9, 19}
print(info)
```

output:

```
{False, 19, 5.9, 'Carla'}
```

Here you can not access the object in sets by using indexing like in list and tuple, due to unorder in nature you can't do indexing.

_Using a For loop_<br>
You can access items of set using a for loop.

```
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
```

output:

```
False
Carla
19
5.9
```

## Day 31: 29/12/2022

**Today's Progress**:

Sets methods in python

# Joining Sets

Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

## I. union() and update():

The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
```

#### Output:

```
{'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}
```

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)
```

#### Output:

```
{'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'}

```

## II. intersection and intersection_update():

The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
```

#### Output:

```
{'Madrid', 'Tokyo'}
```

#### Example :

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
```

#### Output:

```
{'Tokyo', 'Madrid'}
```

## III. symmetric_difference and symmetric_difference_update():

The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
```

#### Output:

```
{'Seoul', 'Kabul', 'Berlin', 'Delhi'}
```

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
```

#### Output:

```
{'Kabul', 'Delhi', 'Berlin', 'Seoul'}
```

## IV. difference() and difference_update():

The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
```

#### Output:

```
{'Tokyo', 'Madrid', 'Berlin'}
```

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))
```

#### Output:

```
{'Tokyo', 'Berlin', 'Madrid'}
```

# Set Methods

There are several in-built methods used for the manipulation of set.They are explained below

## isdisjoint():

The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))
```

#### Output:

False

## issuperset():

The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))
```

#### Output:

False\
False

## issubset():

The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))
```

#### Output:

True

# add()

If you want to add a single item to the set use the add() method.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
```

#### Output:

{'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}

## update()

If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)
```

#### Output:

{'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}

# remove()/discard()

We can use remove() and discard() methods to remove items form list.

#### Example :

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
```

#### Output:

{'Delhi', 'Berlin', 'Madrid'}

The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)
```

#### Output:

KeyError: 'Seoul'

# pop()

This method removes the last item of the set but the catch is that we don???t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
```

#### Output:

{'Tokyo', 'Delhi', 'Berlin'}
Madrid

## del

del is not a method, rather it is a keyword which deletes the set entirely.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
```

#### Output:

NameError: name 'cities' is not defined
We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

What if we don???t want to delete the entire set, we just want to delete all items within that set?

## clear():

This method clears all items in the set and prints an empty set.

#### Example:

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
```

#### Output:

set()

## Check if item exists

You can also check if an item exists in the set or not.

##### Example

```python
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
```

#### Output:

Carla is present.

## Day 32: 30/12/2022

**Today's Progress**:
Dictionaries

Dictionary is the in-built data structure in python, its a key-value pair of objects that is ordered with a unique keys.

# Python Dictionaries

Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
```

#### Output:

```
{'name': 'Karan', 'age': 19, 'eligible': True}
```

## Accessing Dictionary items:

### I. Accessing single values:

Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
```

#### Output:

```
Karan
True
```

### II. Accessing multiple values:

We can print all the values in the dictionary using values() method.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
```

#### Output:

```
dict_values(['Karan', 19, True])
```

### III. Accessing keys:

We can print all the keys in the dictionary using keys() method.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
```

#### Output:

```
dict_keys(['name', 'age', 'eligible'])
```

### IV. Accessing key-value pairs:

We can print all the key-value pairs in the dictionary using items() method.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
```

#### Output:

```
dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
```

## Day 33: 31/12/2022

**Today's Progress**:

Dictionary methods

# Dictionary Methods

Dictionary uses several built-in methods for manipulation.They are listed below

## update()

The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
```

#### Output:

```
{'name': 'Karan', 'age': 19, 'eligible': True}
{'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}
```

## Removing items from dictionary:

There are a few methods that we can use to remove items from dictionary.

### clear():

The clear() method removes all the items from the list.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)
```

#### Output:

```
{}
```

#### pop():

The pop() method removes the key-value pair whose key is passed as a parameter.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
```

#### Output:

```
{'name': 'Karan', 'age': 19}
```

### popitem():

The popitem() method removes the last key-value pair from the dictionary.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)
```

#### Output:

```
{'name': 'Karan', 'age': 19, 'eligible': True}
```

### del:

we can also use the del keyword to remove a dictionary item.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
```

#### Output:

```
{'name': 'Karan', 'eligible': True, 'DOB': 2003}
```

If key is not provided, then the del keyword will delete the dictionary entirely.

#### Example:

```python
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)
```

#### Output:

```
NameError: name 'info' is not defined
```

## Day 34: 01/01/2023

**Today's Progress**:

Else with loops.

what else does with loops?<br>
when the loop iterated successfully then the else part will be executed. and in any case iteration break then else part will not executed.

# Python - else in Loop

As you have learned before, the else clause is used along with the if statement.

Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

## Syntax

```
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block
```

## Example:

```
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")
```

## Output:

```
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop
```

## Day 35: 02/01/2023

**Today's Progress**:

Exception Handling in Python.

There are 3 types of errors:

1. Compile time Error:<br>
   Where syntax error are occuring.
2. run-time errors:<br>
   Where exceptions are occuring
3. logical errors:<br>
   Expected outputs are not coming

So, exception handling are working on the Run time errors.

# Exception Handling

Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

# Exceptions in Python

Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

# Python try...except

try???.. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

## Syntax:

```python
try:
     #statements which could generate
     #exception
except:
     #Soloution of generated exception
```

## Example:

```python
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
```

## Output:

```
Enter an integer: 6.022
Number entered is not an integer.
```

## Day 36: 03/01/2023

**Today's Progress**:
Finally in try except block

What finally does?<br> it execute finally block at any cost.

# Finally Clause

The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

# Syntax:

```
try:
   #statements which could generate
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to
    #execute in any situation


```

The finally block is executed irrespective of the outcome of try??????except???..else blocks\
One of the important use cases of finally block is in a function which returns a value.

# Example:

```python
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
```

## Output 1:

```
Enter an integer: 19
Integer Accepted.
This block is always executed.
```

## Output 2:

```
Enter an integer: 3.142
Number entered is not an integer.
This block is always executed.
```

## Day 37: 04/01/2023

**Today's Progress**:

## Raising Custom errors

In python, we can raise custom errors by using the `raise` keyword.

```python
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
```

In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

## Defining Custom Exceptions

In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:

```python
class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...
```

This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.

## Day 38: 05/01/2023

**Today's Progress**:

KBC code
