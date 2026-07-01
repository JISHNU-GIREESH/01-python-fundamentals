employee_name = input("Enter Your Name: ")
employee_name = employee_name.title()

employee_id = input("Employee Id: ")
employee_id = employee_id.upper()

department = input("Department: ")
department = department.title()

salary = float(input("Enter Your Salary: "))

experience = float(input("Enter Your Experience: "))

performance_rating = int(input("Performance Rate: "))


if experience >= 5 and performance_rating == 5:
    bonus_percentage = 20

elif experience >= 3 and performance_rating >= 4:
    bonus_percentage = 10

else:
    bonus_percentage = 0

bonus = salary * bonus_percentage / 100
final_salary = salary + bonus

print("="*40)
print("BONUS SUMMARY".center(50))
print("="*40)

print("Employee Name    : ",employee_name)
print("Employee ID      : ",employee_id)
print("Department       : ",department)
print(" ")

print("Salary           : ₹", format(salary, ".2f"))
print("Bonus            : ₹", format(bonus, ".2f"))
print("Final Salary     : ₹", format(final_salary, ".2f"))
print(" ")

if bonus_percentage > 0:
    print("Congratulations!")
    print(f"You are eligible for a {bonus_percentage}% Bonus.")
else:
    print("You are not eligible for a Bonus.")

print("="*40)