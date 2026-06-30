employee_name = input("Enter Employee Name: ")
employee_name = employee_name.title()

employee_id = input("ENter Employee ID: ")
employee_id = employee_id.upper()

department = input("Enter Department: ")
department = department.title()

salary = float(input("Salary: "))
experience = float(input("Enter Your Experience: "))
email = input("Enter Your Email Id: ")
email = email.lower()

print("=" * 40)
print("EMPLOYEE DETAILS".center(40))
print("=" * 40)

print("Employee Name    : ",employee_name)
print("Employee ID      : ",employee_id )
print("Department       : ",department)

print("Salary           : ₹", format(salary, ".2f"))
print("Experience       :",experience,"Years")

print("Email            :",email)

print("=" * 40)
print("      EMPLOYEE REGISTERED SUCCESSFULLY      ")
print("=" * 40)