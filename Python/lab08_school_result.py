
#School Result Processing
print("          SCHOOL RESULT PROCESSING")
name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number : ")
marks = []
print(" Enter Marks for 5 Subjects (0-100)")

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()

    marks.append(mark)
total = sum(marks)
percentage = (total / 500) * 100
if any(mark < 40 for mark in marks):
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
elif percentage >= 90:
    result = "PASS"
    grade = "A+"
    remark = "Outstanding"

elif percentage >= 80:
    result = "PASS"
    grade = "A"
    remark = "Excellent"

elif percentage >= 70:
    result = "PASS"
    grade = "B"
    remark = "Very Good"

elif percentage >= 60:
    result = "PASS"
    grade = "C"
    remark = "Good"

elif percentage >= 50:
    result = "PASS"
    grade = "D"
    remark = "Satisfactory"

elif percentage >= 40:
    result = "PASS"
    grade = "E"
    remark = "Pass"

else:
    result = "FAIL"
    grade = "F"
    remark = "Fail"
print("             STUDENT REPORT CARD")

print(f"Student Name : {name}")
print(f"Roll Number  : {roll_number}")

print(f"Total Marks  : {total} / 500")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remarks      : {remark}")


