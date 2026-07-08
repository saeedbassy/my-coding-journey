shifts = []
keep_going = "yes"
while keep_going == "yes":
    valid_days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
    work_day = input("Enter the day of the week: ")
    if work_day.lower() in valid_days.lower():
        work_hours = float(input("Enter the amount of hours: "))
        work_rate = float(input("Enter the hourly rate: "))
        user_shift = {"day": work_day, "hours": work_hours, "rate": work_rate}
        shifts.append(user_shift)
        keep_going = input("Do you want to add another shift? (yes/no): ")
    else:
        print("Invalid day of the week")
total_earnings = 0
for user_shift in shifts:
    total_earnings = float(total_earnings) + user_shift["hours"] * user_shift["rate"]
print(f"You will earn ${total_earnings}")