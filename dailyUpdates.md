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

Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

### if the expression evaluates False:

Execute the block of code inside else statement. After execution return to the code out of the if……else block.

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

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

1. The match keyword
2. One or more case clauses
3. Expression for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

## Syntax:

```python
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …
            case ‘pattern n’ : //statement n
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

## Day 17: 16/12/2022

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
