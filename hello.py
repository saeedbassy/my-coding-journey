def classify_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    print("That's not a valid number!")

numbers = []
for i in range(1, 6):
    try:
        user_answer = int(input("Enter a number: "))
        numbers.append(user_answer)
    except:
        print("That's not a valid number!")

for number in numbers:
    result = classify_number(number)
    print(result)

print("The amount of numbers you entered is: " + str(len(numbers)))
print("The largest number you entered is: " + str(max(numbers)))
print("The smallest number you entered is: " + str(min(numbers)))