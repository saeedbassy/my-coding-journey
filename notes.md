## Variables
What it is: a labeled box that holds a value

```python
name = "Saeed"
```

Note: text values need quotes around them; numbers don't

## print()
What it is: displays a value on the screen

```python
print(name)
```

## input()
What it is: pauses the program and asks the user to type something, then stores what they typed into a variable

```python
user_name = input("What is your name? ")
```

Mistake to avoid: none this time - first try success

## if / else
What it is: lets the program make a decision and run different code depending on whether something is true or false

```python
age = 16
if age >= 16:
    print("You can work")
else:
    print("You are too young to work")
```

## = vs ==
= assigns a value to a variable (stores something)
== compares two values and check if they are equal (true or false)

## for loops
What it is: repears a block of code a fixed number of times

```python
for i in range(1, 6):
    print(i)
```

i = the current value of the loop during each pass

## combining if/else with for loops
What it is: putting a decision (if/else) inside a loop, so the decision runs fresh on every repetition

```python
for i in range(1, 6):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")
```

## i % 2 == 0
Checks if there is no remainder when dividing i by 2 (meaning i is even)

## counting inside a loop
What it is: using a varibale that starts at 0 before the loop, then adding 1 to it each time something happens inside the loop

```python
even_count = 0
for i in range(1, 6):
    if i % 2 == 0:
        even_count = even_count + 1
print(even_count)
```

## even_count = even_count + 1
even_count appears on both sides because you take the current count and add 1 to it, then save that new total back into the same variable

## lists
What it is: a container that holds multiple values in one variable, in order

```python
numbers = []
numbers.append(5)
numbers.append(10)
print(numbers)
```

## numbers = []
Creates an empty list

## ()len and max()
len(list) tells you how many times are in a list
max(list) tells you the largest item in a list

```python
numbers = [3, 7, 2, 9, 5]
print(len(numbers))
print(max(numbers))
```

len() returns the amount of items in a list
max() returns the greatest value in a list

## min()
What it is: returns the smallest value in a list (opposite of max())

```python
numbers = [3, 7, 2, 9, 5]
print(min(numbers))
```

## len() and the actual values
len() only counts items, it doesn't care what the values are
A list of 5 huge numbers and a list 5 tiny numbers both return 5 from len()

## .sort()
What it is: rearranges a list's items in order, smallest to largest by default

```python
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
```

## sort() and print() order matters
If print() comes before .sort() in your code, you'll see the original, unsorted order - Python runs top to bottom

## while loops
What it is: repeats code as long as a condition stays true, instead of running a fixed number of times like a for loop

```python
keep_going = "yes"
while keep_going == "yes":
    print("Looping!")
    keep_going = input("Keep going? (yes/no): ")
```

## for vs while
for loop: runs a fixed, known number of times
while loop: keeps looping until its condition becomes false (you don't know in advance how many times it will run)

## while loop with a counter
You can also use a number instead of yes/no to control a while loop

```python
attempts = 0
while attempts < 3:
    print("Attempt number " + str(attempts + 1))
    attempts = attempts + 1
```

## Infinite loop
What it is: a loop that never stops because its condition never becomes false (e.g. forgetting to increase the counter)

Why it's dangerous: the program runs forever, freezing the terminal and using up resources until you force-stop it (Ctrl+C)

## functions
What it is: a resuable block of code that you define once and can call as many times as you want, optionally with inputs

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Saeed")
greet("Kayden")
```

## Why use functions
- Saves you from rewriting the same code over and over
- If you need to fix or change the logic, you only update it in one place instead of every copy

## return vs print inside a function
print() just displays something - it doesn't give the value back
return hands the value back to whoever called the function, so you can store it or use it elsewhere

```python
def square(number):
    return number * number

result = square(5)
print(result)
```

## Unused return values
If a function returns a value but nothing stores it or prints it, the value just disappears - the function still ran, but the result is never used

## functions with multiple parameters
A function can take more than one input, seperated by commas

```python
def add_numbers(a, b):
    return a + b

total = add_numbers(3, 7)
print(total)
```

## parameters vs arguments
Parameter: a placeholder name in the function's definition
Argument: the real, actual value passed in when calling the function

Example: def add(a, b) - a and b are parameters
add (3, 7) - 3 and 7 are the arguments

## using parameters and arguments together
Each time you call a function with different arguments, the parameters take on those new values for that one call only

```python
def greet(name, age):
    print(name + " is " + str(age) + " years old")

greet("Saeed", 16)
greet("Kayden", 17)
```

## parameters hold arguments during a call
When you call grade_letter(85), score (the parameter) holds the value 85 (the argument) for the duration of that call

## combining everything: a function that uses a loop
Functions can contain loops inside them, just like any other code

```python
def count_to(n):
    for i in range(1, n + 1):
        print(i)

count_to(5)
```

## return stops the function immediately
The moment Python hits a return statement, the function exits right there - it doesn't keep running the rest of the code below it, even if that's still inside a loop

## Project: Number Analyzer
Goal: combine functions, loops, lists, and conditionals into one working program

This will use:
- a function with a parameter and return
- a for loop
- a list (build, append)
- if/else
- len(), max(), min()

## try / except
What it is: lets your program handle errors gracefully instead of crashing

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("That wasn't a valid number!")
```

## try/except crash behavior
Without try/except: an error crashes the whole program immediately
With try/except: the error is caught, the except block runs instead, and the program keeps going

## looping through two lists together
You can store related data in seperate lists, then loop through them in sync using their shared index

```python
names = ["Alice", "Bob"]
ages = [30, 25]
for i in range(len(names)):
    print(names[i] + " is " + str(ages[i]) + " years old")
```

## dictionaries
What it is: stores data in key-value pairs, instead of a list's plain ordered sequence

```python
ages = {"Saeed": 16, "Kayden": 17}
print(ages["Saeed"])
```

## looping over a dictionary
for question in quiz: loops through each key in the dictionary, one at a time, calling it "question" for that pass
quiz[question] looks up the value paired with that key

## play again loop
Wrap the entire quiz in a while loop so it repeats whenever the user wants to play again, resetting the score each time

```python
keep_playing = "yes"
while keep_playing == "yes":
    # quiz code goes here
    keep_playing = input("Play again? (yes/no): ")
```

