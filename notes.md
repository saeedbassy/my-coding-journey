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

## When to use try/except
Use it whenever your program accepts user input or reads from an external source - anywhere something unpredictable could go wrong and crash the programS

## File I/O
What it is: reading from and writing to files so data persists between runs of your program

```python
with open("tasks.txt", "w") as file:
    file.write("Buy groceries\n")
```

```python
with open("tasks.txt", "r") as file:
    contents = file.read()
    print(contents)
```

## File modes
"w" = write: creates the file if it doesn't exist, or overwrites it if it does
"r" = read: reads the contents of an existing file

## FILE WRITING BASICS
- open(filename, "w") opens a file in write mode
- "w" mode OVERWRITES the entire file each time (unlike "a" which appends)
- Since we're rewriting the whole tasks list each time, "w" is correct here
- Using "with open(...) as f:" automatically closes the file when done
- To write each task on its own line, use f.write() and add "\n" at the end of each line
- You'll need a for loop to go through your tasks list and write each one

## DELETING FROM A LIST
- list.pop(index) removes and returns the item at that index
- Lists and indexed are indexed starting at 0, but you'll show tasks to the user starting at 1
- So, if the user picks "task number 2," you need to pop(1) - subtract 1 to convert
- After popping, you still need to rewrite tasks.txt with the updated list (same pattern as your save-after-add code, just reused)
- Always validate the number the user enters is a real index before popping (or you'll crash on a bad input)

## enuerate()
What it is: A function that loops through a list and gives you both the position (index) and the value at the same time, instead of just the value alone.

```python
for index, item in enumerate(["apple", "banana", "cherry"]):
    print(index + 1, item)
```

Common mistake: Forgot that enumerate() starts counting at 0, so mt displayed list was off by one until I added + 1.

## str()

```python
str(5)
```

Common mistake: Tried to combine a number and text with + without converting the number to a string first, which caused a TypeError.

## pop()
What it is: list.pop(index) removes the item at that position from the list and gives it back to you. Since lists start counting at 0 but you show tasks to the user starting at 1, you need to subtract 1 from whatever the number the user types in before calling pop().

```python
sample = ["a", "b", "c"]
sample.pop(1)
```

Common mistake: Forgot to subtract 1 from the user's input before calling pop(), so it deleted the wrong task (one after the one I meant).

## break
What it is: Immediately exits the nearest loop it's inside, skipping any remaining code in that loop and everything afer it in that iteration.

```python
while True:
    print("Quitting...")
    break
```

Common mistake: Printed "Quitting..." but forgot to actually stop the loop, so the menu kept looping forever after choosing to quit.

## Clean testing data before a push
What it is: Before committing, delete any leftover test tasks (like "Do laundry") from tasks.txt so your repo shows a clean, intentional starting state rather than scratch data from testing.

Common mistake: Pushed test data to GitHub without realizing it, so my repo history shows "Do laundry" as if it were a real task.

## Storing tasks as dictionaries
What it is: Right now each task is just a string. To track whether a task is done, each task needs two pieces of info - the text and a done/not-done status - so instead of a string, each task becomes a small dictionary with two keys.

```python
task = {"text": "buy groceries", "done": False}
print(task["text"])
print(task["done"])
```

Common mistake: Tried to keep tasks as plain strings and add a seperate "done" list to match up with them by position - this got confusing fast. Combining both pieces into one dictionary per task keeps everything together.

## Changing a dictionary value
What it is: You can update the value stored under a key in a dictionary the same way you access it - using dictionary[key] = new_value. This overwrites whatever was there before.

```python
task = {"text": "clean room", "done": False}
task["done"] = True
print(task["done"])
```

Common mistake: Tried to create a whole new dictionary just to update one value, when I could have changed just that one key directly.

## Reinforcement: indexing + dictionaries
What it is: A quick recap of the two ideas that caused the most bugs today - using an index to reach into a list (tasks[i]), and using a key to reach into a dictionary (task["key"]), and how they combine (tasks[i]["key"]).

```python
tasks = [{"text": "wake up", "done": False}, {"text": "eat", "done": True}]
print(tasks[0]["text"])
print(tasks[1]["done"])
```

Common mistake: Mixed up when to use [index] (position in a list) versus ["key"] (name in a dictionary) - they look similar but do different things.

## Editing a dictionary value with new input
What it is: Same idea as marking a task complete - find the task by index, then set one of its keys to a new value. The only difference is the new value comes from input() instead of always being True.

```python
task = {"text": "clean room", "done": False}
task["text"] = "clean the whole house"
print(task["text"])
```

Common mistake: Forgot that setting task["text"] to a new value completely replaces the old text - there's no way to get the original back once overwritten.

## sorted() with a key function
What it is: sorted() takes a list and returns a new, sorted version of it. By default it sorts by natural order (numbers small to large, letters A-Z). To sort by something custom - like a dictionary's "done" value - you give it a key, which tells it what to look for each item.

```python
tasks = [{"text": "eat", "done": True}, {"text": "sleep", "done": False}]
sorted_tasks = sorted(tasks, key=lambda t: t["done"])
print(sorted_tasks)
```

Common mistake: Forgot that sorted() returns a new list instead of changing the original - so I need to assign the result to a variable (or reassign tasks) instead of expecting the original list to update on its own.

## Reinforcement: full data flow recap
What it is: A recap of how one task moves through your program - from file, into a dictionary, through the list, and back to file.

```python
# 1. Loading: turn each line into a dictionary
tasks.append({"text": contents.strip(), "done": False})

# 2. Reading: pull a value out by key
print(tasks[0]["text"])

# 3. Updating: find the right task by index, then change one key
tasks[0]["done"] = True

# 4. Saving: turn each dictionary back into a line of text
f.write(user_task["text"] + "\n")
```

Common mistake: Thought of tasks[i] and task["key"] as interchangeable - they're not. One finds a task by position, the other finds a value by name, inside that task.

## Saving multiple pieces of data on one line
What it is: Right now each line in tasks.txt only has the task text. To also save whether it's done, we need a way to store two pieces of info on one line, then split them back apart when loading. A simple way: seperate them with a character that won't normally appear in a task, like |.

```python
f.write(user_task["text"] + "|" + str(user_task["done"]) + "\n")
```

Common mistake: Tried to save user_task["done"] without wrapping it in str() first, since it's True/False (a boolean), not text, and + only works between strings.

## split() - breaking a string into pieces
What it is: .split("|") breaks a string into a list of pieces, using | as the dividing point. So "clean room|False".split("|") gives you ["clean room", "False"] - a list with two items.

```python
line = "clean room|False"
parts = line.split("|")
print(parts[0])
print(parts[1])
```

Common mistake: Forgot that everything from .split() comes back as a string - even "True" or "False" - so comparing it directly with if parts[1] == True doesn't work; it needs to be compared as text: if parts[1] == "True".

