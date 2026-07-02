employee_name = input("Enter your name: ")
employee_name = employee_name.title()

employee_id = input("Employee Id: ")
employee_id = employee_id.upper()

department = input("Enter your Department: ")
department = department.title()

salary = float(input("Enter your salary: "))

experience = float(input("Enter your experience (Years): "))

performance_rating = int(input("Performance Rating (1-5): "))

attendance = input("Is Attendance Good (True/False): ")
attendance = attendance.lower() == "true"

if experience >= 5 and performance_rating >= 4:
    promotion_status = "Senior Employee"

elif experience >= 3 or performance_rating == 5:
    promotion_status = "Promotion Review"

else:
    promotion_status = "Not Eligible"


if not attendance:
    attendance_message = "Attendance Warning!"
else:
    attendance_message = "Attendance is Good"


print("=" * 50)
print("PROMOTION SUMMARY".center(50))
print("=" * 50)

print(f"Employee Name        : {employee_name}")
print(f"Employee Id         : {employee_id}")
print(f"Department          : {department}")
print()

print(f"Salary              : ₹{salary:.2f}")
print(f"Experience          : {int(experience)} Years")
print(f"Performance Rating  : {performance_rating}")
print(f"Attendance          : {attendance}")
print()

print(f"Promotion Status    : {promotion_status}")
print(f"Attendance Status   : {attendance_message}")

print("=" * 50)