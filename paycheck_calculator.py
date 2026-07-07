shifts = []
keep_going = "yes"
while keep_going == "yes":
    work_day = input("Enter the day of the week: ")
    work_hours = float(input("Enter the amount of hours: "))
    work_rate = float(input("Enter the hourly rate: "))
    user_shift = {"day": work_day, "hours": work_hours, "rate": work_rate}
    shifts.append(user_shift)
    keep_going = input("Do you want to add another shift? (yes/no): ")
total_earnings = 0
for user_shift in shifts:
    total_earnings = float(total_earnings) + user_shift["hours"] * user_shift["rate"]
print("You will earn $" + str(float(total_earnings)))