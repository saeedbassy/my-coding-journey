# My Coding Notes

## Table of Contents
1. [Fundamentals](#fundamentals)
2. [Loops](#loops)
3. [Lists](#lists)
4. [Functions](#functions)
5. [Dictionaries](#dictionaries)
6. [Lists of Dictionaries](#lists-of-dictionaries)
7. [Error Handling](#error-handling)
8. [File I/O](#file-io)
9. [Strings & Type Conversion](#strings--type-conversion)
10. [Workflow Habits](#workflow-habits)
11. [Project: To-Do List Manager](#project-to-do-list-manager)
12. [Project: Budget Tracker](#project-budget-tracker)

---

## Fundamentals

### Variables
**What it is:** A labeled box that holds a value.

```python
name = "Saeed"
```

Note: text values need quotes around them; numbers don't.

### print()
**What it is:** Displays a value on the screen.

```python
print(name)
```

### input()
**What it is:** Pauses the program and asks the user to type something, then stores what they typed into a variable.

```python
user_name = input("What is your name? ")
```

### = vs ==
`=` assigns a value to a variable (stores something).
`==` compares two values and checks if they are equal (gives back `True` or `False`).

### if / else
**What it is:** Lets the program make a decision and run different code depending on whether something is true or false.

```python
age = 16
if age >= 16:
    print("You can work")
else:
    print("You are too young to work")
```

---

## Loops

### for loops
**What it is:** Repeats a block of code a fixed number of times.

```python
for i in range(1, 6):
    print(i)
```

`i` = the current value of the loop during each pass.

### Combining if/else with for loops
**What it is:** Putting a decision (if/else) inside a loop, so the decision runs fresh on every repetition.

```python
for i in range(1, 6):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")
```

`i % 2 == 0` checks if there is no remainder when dividing `i` by 2 (meaning `i` is even).

### Counting inside a loop
**What it is:** Using a variable that starts at 0 before the loop, then adding 1 to it each time something happens inside the loop. The variable appears on both sides of `=` because you take the current count, add 1, then save that new total back into the same variable.

```python
even_count = 0
for i in range(1, 6):
    if i % 2 == 0:
        even_count = even_count + 1
print(even_count)
```

### while loops
**What it is:** Repeats code as long as a condition stays true, instead of running a fixed number of times like a for loop.

```python
keep_going = "yes"
while keep_going == "yes":
    print("Looping!")
    keep_going = input("Keep going? (yes/no): ")
```

### for vs while
**for loop:** runs a fixed, known number of times.
**while loop:** keeps looping until its condition becomes false (you don't know in advance how many times it will run).

### while loop with a counter
**What it is:** You can also use a number instead of yes/no to control a while loop.

```python
attempts = 0
while attempts < 3:
    print("Attempt number " + str(attempts + 1))
    attempts = attempts + 1
```

### Infinite loop
**What it is:** A loop that never stops because its condition never becomes false (e.g. forgetting to increase the counter).

Why it's dangerous: the program runs forever, freezing the terminal and using up resources until you force-stop it (Ctrl+C).

### break
**What it is:** Immediately exits the nearest loop it's inside, skipping any remaining code in that loop and everything after it in that iteration.

```python
while True:
    print("Quitting...")
    break
```

### "Play again" loop pattern
**What it is:** Wrap an entire program in a while loop so it repeats whenever the user wants to go again, resetting anything (like a score) each time.

```python
keep_playing = "yes"
while keep_playing == "yes":
    # program code goes here
    keep_playing = input("Play again? (yes/no): ")
```

---

## Lists

### lists
**What it is:** A container that holds multiple values in one variable, in order.

```python
numbers = []
numbers.append(5)
numbers.append(10)
print(numbers)
```

`numbers = []` creates an empty list.

### len(), max(), and min()
**What it is:** `len(list)` returns how many items are in a list. `max(list)` returns the largest item. `min(list)` returns the smallest item.

```python
numbers = [3, 7, 2, 9, 5]
print(len(numbers))
print(max(numbers))
print(min(numbers))
```

Note: `len()` only counts items, it doesn't care what the values are — a list of 5 huge numbers and a list of 5 tiny numbers both return 5 from `len()`.

### .sort()
**What it is:** Rearranges a list's items in order, smallest to largest by default.

```python
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)
```

### Looping through two lists together
**What it is:** You can store related data in separate lists, then loop through them in sync using their shared index.

```python
names = ["Alice", "Bob"]
ages = [30, 25]
for i in range(len(names)):
    print(names[i] + " is " + str(ages[i]) + " years old")
```

### enumerate()
**What it is:** A function that loops through a list and gives you both the position (index) and the value at the same time, instead of just the value alone.

```python
for index, item in enumerate(["apple", "banana", "cherry"]):
    print(index + 1, item)
```

### pop()
**What it is:** `list.pop(index)` removes the item at that position from the list and gives it back to you. Since lists start counting at 0 but you show items to the user starting at 1, you need to subtract 1 from whatever number the user types in before calling `pop()`.

```python
sample = ["a", "b", "c"]
sample.pop(1)
```

### sorted() with a key function
**What it is:** `sorted()` takes a list and returns a **new**, sorted version of it. By default it sorts by natural order (numbers small to large, letters A-Z). To sort by something custom — like a dictionary's `"done"` value — you give it a `key`, which tells it what to look at for each item.

```python
tasks = [{"text": "eat", "done": True}, {"text": "sleep", "done": False}]
sorted_tasks = sorted(tasks, key=lambda t: t["done"])
print(sorted_tasks)
```

---

## Functions

### functions
**What it is:** A reusable block of code that you define once and can call as many times as you want, optionally with inputs.

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Saeed")
greet("Kayden")
```

**Why use functions:**
- Saves you from rewriting the same code over and over
- If you need to fix or change the logic, you only update it in one place instead of every copy

### return vs print inside a function
**What it is:** `print()` just displays something — it doesn't give the value back. `return` hands the value back to whoever called the function, so you can store it or use it elsewhere.

```python
def square(number):
    return number * number

result = square(5)
print(result)
```

### Functions with multiple parameters
**What it is:** A function can take more than one input, separated by commas.

```python
def add_numbers(a, b):
    return a + b

total = add_numbers(3, 7)
print(total)
```

### Parameters vs arguments
**Parameter:** a placeholder name in the function's definition.
**Argument:** the real, actual value passed in when calling the function.

Example: `def add(a, b)` — `a` and `b` are parameters. `add(3, 7)` — `3` and `7` are the arguments.

### Using parameters and arguments together
**What it is:** Each time you call a function with different arguments, the parameters take on those new values for that one call only.

```python
def greet(name, age):
    print(name + " is " + str(age) + " years old")

greet("Saeed", 16)
greet("Kayden", 17)
```

When `greet("Saeed", 16)` is called, `name` and `age` (the parameters) hold `"Saeed"` and `16` (the arguments) for the duration of that call only.

### Combining everything: a function that uses a loop
**What it is:** Functions can contain loops inside them, just like any other code.

```python
def count_to(n):
    for i in range(1, n + 1):
        print(i)

count_to(5)
```

### return stops the function immediately
**What it is:** The moment Python hits a `return` statement, the function exits right there — it doesn't keep running the rest of the code below it, even if that's still inside a loop.

---

## Dictionaries

### dictionaries
**What it is:** Stores data in key-value pairs, instead of a list's plain ordered sequence.

```python
ages = {"Saeed": 16, "Kayden": 17}
print(ages["Saeed"])
```

### Looping over a dictionary
**What it is:** `for key in dictionary:` loops through each key in the dictionary, one at a time. `dictionary[key]` looks up the value paired with that key.

```python
quiz = {"2+2": "4", "capital of France": "Paris"}
for question in quiz:
    print(question, "->", quiz[question])
```

### Storing multiple pieces of data together (as a dictionary)
**What it is:** If one item needs more than one piece of info (e.g. a task's text and whether it's done), a plain value isn't enough — combine both pieces into one dictionary with multiple keys.

```python
task = {"text": "buy groceries", "done": False}
print(task["text"])
print(task["done"])
```

### Changing a dictionary value
**What it is:** You can update the value stored under a key in a dictionary the same way you access it — using `dictionary[key] = new_value`. This overwrites whatever was there before.

```python
task = {"text": "clean room", "done": False}
task["done"] = True
print(task["done"])
```

### Editing a dictionary value with new input
**What it is:** Same idea as above — find the item by index, then set one of its keys to a new value. The difference is the new value comes from `input()` instead of a fixed value like `True`.

```python
task = {"text": "clean room", "done": False}
task["text"] = "clean the whole house"
print(task["text"])
```

### Adding a new key to an existing dictionary structure
**What it is:** Same pattern as adding any key — just one more piece added when the dictionary is first created (e.g. adding `"priority"` alongside `"text"` and `"done"`).

```python
task = {"text": "clean room", "done": False, "priority": "High"}
print(task["priority"])
```

---

## Lists of Dictionaries

Everything in this section builds on the same idea: a list holds multiple dictionaries, and you loop through the list to reach each one.

### Combining index and key access
**What it is:** Using an index to reach into a list (`tasks[i]`) and a key to reach into a dictionary (`task["key"]`) are two different things — but they combine when a list holds dictionaries: `tasks[i]["key"]`.

```python
tasks = [{"text": "wake up", "done": False}, {"text": "eat", "done": True}]
print(tasks[0]["text"])
print(tasks[1]["done"])
```

### Looping through a list of dictionaries
**What it is:** Loop through the list with `enumerate()` so you get both a number and the dictionary itself, then pull out the values you want using the keys.

```python
expenses = [{"amount": 12.50, "category": "food"}, {"amount": 5.00, "category": "gas"}]
for index, expense in enumerate(expenses, start=1):
    print(index, expense["amount"], expense["category"])
```

### Displaying an extra dictionary value
**What it is:** Same pattern as showing one piece of data, just adding another piece pulled from the same dictionary onto the `print()` line.

```python
task = {"text": "clean room", "priority": "high"}
print(task["text"] + " (" + task["priority"] + ")")
```

### Filtering a list with a condition
**What it is:** Looping through a list and only acting on items that match some condition, instead of every item.

```python
tasks = [{"text": "call Kayden", "priority": "high"}, {"text": "read Quran", "priority": "low"}]
for task in tasks:
    if task["priority"] == "high":
        print(task["text"])
```

### Priority + filtering recap
**What it is:** A recap connecting priority storage, display, and filtering.

```python
task = {"text": "call Kayden", "done": False, "priority": "high"}

# Storing: priority comes from input() at creation time
# Displaying: pull it out and show it alongside text
print(task["text"] + " (" + task["priority"] + ")")

# Filtering: compare user input against stored priority, case-insensitively
user_choice = "High"
if task["priority"].lower() == user_choice.lower():
    print(task["text"])
```

### Counting matches in a list
**What it is:** Looping through a list and using a counter to track how many items meet a condition — same pattern as counting evens in a list of numbers, just applied to dictionaries now.

```python
tasks = [{"done": True}, {"done": False}, {"done": True}]
completed_count = 0
for task in tasks:
    if task["done"] == True:
        completed_count = completed_count + 1
print(completed_count)
```

### Searching a list by partial text match
**What it is:** Checking whether one string appears somewhere inside another, using the `in` keyword — useful for search, since the user won't always type the exact full task text.

```python
tasks = [{"text": "call Kayden"}, {"text": "read Quran"}]
search_term = "kayden"
for task in tasks:
    if search_term in task["text"].lower():
        print(task["text"])
```

### Building a running total per category
**What it is:** Instead of one grand total, keep a running total for each category separately, using a dictionary where each category name is a key and its total is the value.

```python
category_totals = {}
for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]
    if category not in category_totals:
        category_totals[category] = 0
    category_totals[category] = category_totals[category] + amount
```

### Reading a saved file into a list at startup
**What it is:** When your program starts, you check if a save file exists and load its contents back into your list, so you pick up where you left off instead of starting empty every time. Wrapping it in `try`/`except` handles the first run, when the file doesn't exist yet.

```python
expenses = []

try:
    with open("expenses.txt", "r") as file:
        for line in file.readlines():
            parts = line.strip().split("|")
            expenses.append({"amount": float(parts[0]), "category": parts[1]})
except:
    pass
```

---

## Error Handling

### try / except
**What it is:** Lets your program handle errors gracefully instead of crashing.

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("That wasn't a valid number!")
```

Without `try`/`except`: an error crashes the whole program immediately. With it: the error is caught, the `except` block runs instead, and the program keeps going.

**When to use it:** Whenever your program accepts user input or reads from an external source — anywhere something unpredictable could go wrong and crash the program.

---

## File I/O

### File I/O basics
**What it is:** Reading from and writing to files so data persists between runs of your program.

```python
with open("tasks.txt", "w") as file:
    file.write("Buy groceries\n")
```

```python
with open("tasks.txt", "r") as file:
    contents = file.read()
    print(contents)
```

### File modes
`"w"` = write: creates the file if it doesn't exist, or **overwrites** it if it does (unlike `"a"`, which appends).
`"r"` = read: reads the contents of an existing file.

### Writing multiple items with a loop
**What it is:** `open(filename, "w")` opens a file in write mode. Using `with open(...) as f:` automatically closes the file when done. To write each item on its own line, loop through your list and call `f.write()` with `"\n"` at the end of each line.

```python
with open("tasks.txt", "w") as f:
    for task in tasks:
        f.write(task + "\n")
```

### Saving multiple pieces of data on one line
**What it is:** If each item is a dictionary with more than one piece of data, separate the pieces with a character that won't normally appear in the data (like `|`), then split them back apart when loading.

```python
f.write(user_task["text"] + "|" + str(user_task["done"]) + "\n")
```

---

## Strings & Type Conversion

### str()
**What it is:** Converts a number (or other value) into a string so it can be joined with text using `+`.

```python
str(5)
```

### float()
**What it is:** Converts a string into a decimal number, so you can do math with it. Similar to `int()`, but keeps decimal places (like 12.50) instead of rounding to a whole number.

```python
price = float("12.50")
print(price + 1)
```

### split() — breaking a string into pieces
**What it is:** `.split("|")` breaks a string into a list of pieces, using `|` as the dividing point.

```python
line = "clean room|False"
parts = line.split("|")
print(parts[0])
print(parts[1])
```

### .lower()
**What it is:** Converts every letter in a string to lowercase, without changing the original string (it returns a new one).

```python
text = "High"
print(text.lower())
```

---

## Workflow Habits

### Clean testing data before a push
**What it is:** Before committing, delete any leftover test data from your save files (like `tasks.txt`) so your repo shows a clean, intentional starting state rather than scratch data from testing.

---

## Project: To-Do List Manager

A condensed look at how these pieces work together — loading, sorting, and saving a task with multiple pieces of data:

```python
# Loading: split a saved line back into its pieces, rebuild the dictionary
parts = contents.strip().split("|")
tasks.append({"text": parts[0], "done": parts[1] == "True"})

# Reading: pull one value out by key
print(tasks[0]["text"])

# Updating: find the right task by index, then change one key
tasks[0]["done"] = True

# Sorting: reorder a list without changing the original
sorted_tasks = sorted(tasks, key=lambda t: t["done"])

# Saving: turn each dictionary back into one line of text
f.write(user_task["text"] + "|" + str(user_task["done"]) + "\n")
```

The core idea to remember: `tasks[i]` finds an item by **position**, `task["key"]` finds a value by **name** inside that item, and `tasks[i]["key"]` combines both.

---

## Project: Budget Tracker

**What it is:** A program to log expenses (amount + category) and show a running total, applying the same dictionary and file I/O skills from the To-Do app to a new problem.

```python
expense = {"amount": 12.50, "category": "food"}
print(expense["amount"])
```

See [Lists of Dictionaries](#lists-of-dictionaries) for the enumerate/loop pattern used for viewing expenses, the running-total-per-category pattern used for the category breakdown feature, and the file-loading pattern used to make expenses persist between runs. See [float()](#strings--type-conversion) for why expense amounts need to be converted before doing math with them.

## random.choice()

What it is:
Picks one random item out of a list (or string) each time it's called. To use it, you first need import random at the very top of your file - Python keeps random-related tools in a seperate module you have to bring in yourself.

```python
import random

letters = ["a", "b", "c", "d"]
print(random.choice(letters))
```

## "".join()

What it is:
Combines every item in a list into a single string, with nothing (or what ever you put in the quotes) between each item. Since random_password is currently a list of seperate characters, join() glues them all together into one password string.

```python
letters = ["a", "B", "3", "!"]
password = "".join(letters)
print(password)
```

This prints aB3! - one combined string instead of a list with commas and brackets.

### f-strings
**What it is:** A cleaner way to build strings with variables mixed in, using `f"..."` and `{variable}` placeholders - no more `+` and `str()` chains.

```python
name = "Saeed"
age = 16
print(f"{name} is {age} years old")
```

### f-string format specifiers (:.2f)
**What it is:** Adding `:.2f` after a variable inside an f-string rounds it to exactly 2 decimal places - useful for money, so `$12.5` displays as `$12.50`.

```python
price = 12.5
print(f"${price:.2f}")
```

### List comprehensions
**What it is:** A compact way to create a new list by looping through an existing one, all in a single line - instead if writing a full `for` loop with `.append()`.

```python
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)
```

### Sets
**What it is:** A collection like a list, but it automatically removes duplicates and doesn't preserve order. Created with `{}` (like a dictionary) but without key-value pairs - just values.

```python
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)
print(unique_numbers)
```

### Checking membership with `in` and a set
**What it is:** Checking if a value exists inside a set of allowed options, using `in`. Sets are faster than lists for this kind of check, and they're a natural fit when you have a fixed group of valid choices.

```python
valid_colors = {"red", "green", "blue"}
color = "green"
if color in valid_colors:
    print("Valid choice")
else:
    print("Not a valid choice")
```

### Nested dictionaries
**What it is:** A dictionary where a value is itself another dictionary - useful for grouping related pieces of information together under one key.

```python
contact = {"name": "Kayden", "info": {"phone": "555-1234", "city": "Monroeville"}}
print(contact["info"]["phone"])
```

### Tuples
**What it is:** Like a list, but immutable - once created, you can't change, add, or remove items. Written each with parentheses `()` instead of square brackets `[]`. Useful for fixed pairs or groups of values that shouldn't change, like coordinates.

```python
point = (3, 5)
print(point[0])
print(point[1])
```

### Functions returning multiple values
**What it is:** A function can return more than one value at once, seperated by commas. Python packages them into a tuple automatically, and you can unpack them into seperate variables when you call the function.

```python
def get_name_and_age():
    return "Saeed", 16

name, age = get_name_and_age()
print(name)
print(age)
```

### .title()
**What it is:** Converts the first letter of each word in a string to uppercase, and the rest to lowercase - the opposite direction of `.lower()`. Useful for matching user input against data stored with specific capitalization.

```python
text = "monday"
print(text.title())
```