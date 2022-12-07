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
