student_name = input("Enter Student Name: ")
student_name = student_name.title()

student_id = input("Enter Student ID: ")
student_id = student_id.upper()

mark_1 = float(input("Enter Subject 1 Score: "))
mark_2 = float(input("Enter Subject 2 Score: "))
mark_3 = float(input("Enter Subject 3 Score: "))
mark_4 = float(input("Enter Subject 4 Score: "))
mark_5 = float(input("Enter Subject 5 Score: "))

total_marks = mark_1 + mark_2 + mark_3 + mark_4 + mark_5
average_marks = total_marks / 5

if average_marks >= 90:
    grade = "A+"

elif average_marks >= 80:
    grade = "A"

elif average_marks >= 70:
    grade = "B"

elif average_marks >= 60:
    grade = "C"

elif average_marks >= 50:
    grade = "D"

else:
    grade = "F"

if average_marks >= 50:
    result = "Pass"
else:
    result = "Fail"

print("=" * 40)
print("STUDENT GRADE REPORT".center(40))
print("=" * 40)


print(f"Student Name: {student_name}")
print(f"Student ID: {student_id}")
print()

print(f"Subject 1 Marks : {mark_1:.2f}")
print(f"Subject 2 Marks : {mark_2:.2f}")
print(f"Subject 3 Marks : {mark_3:.2f}")
print(f"Subject 4 Marks : {mark_4:.2f}")
print(f"Subject 5 Marks : {mark_5:.2f}")

print(f"Total Marks     : {total_marks:.2f}")
print(f"Average Marks   : {average_marks:.2f}")
print(f"Grade           : {grade}")
print(f"Result          : {result}")
print()

print("=" * 40)