#Lab 17 - Student Records Handling
students = {
    "101": {"Name": "Aman", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Marks": [74, 80, 82]}
}

def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    marks = student["Marks"]

    total, average = calculate_results(marks)

    print(
        f"Roll No: {roll} | Name: {student['Name']:<10} "
        f"| Marks: {marks} | Total: {total} "
        f"| Average: {average:.2f}%"
    )

def add_student(records, roll, name, marks):

    if roll in records:
        print("Error: Roll Number already exists.")

    else:
        records[roll] = {
            "Name": name,
            "Marks": marks
        }

        print(f"[SUCCESS] Student '{name}' "
              f"(Roll No: {roll}) added successfully.")

while True:

    print("\n================================")
    print("   STUDENT RECORDS MANAGEMENT SYSTEM")
    print("================================")

    print("\nSelect an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("\nEnter choice (1-4): ")

    if choice == "1":

        print("\n--- All Student Records ---")

        if len(students) == 0:
            print("No student records available.")

        else:
            for roll, student in students.items():
                display_student(roll, student)

            print("Total Students:", len(students))

    elif choice == "2":

        print("\n--- Add New Student ---")

        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        try:
            marks = []

            for i in range(3):
                mark = int(input(f"Enter marks for Subject {i+1}: "))
                marks.append(mark)

            if any(mark < 0 or mark > 100 for mark in marks):
                print("Error: Marks must be between 0 and 100.")

            else:
                add_student(students, roll, name, marks)

        except ValueError:
            print("Invalid input! Please enter integer marks.")

    elif choice == "3":

        roll = input("Enter Roll Number to search: ")

        student = students.get(roll)

        if student:
            print("[RECORD FOUND]")
            display_student(roll, student)

        else:
            print(f"[ERROR] No student found with Roll Number '{roll}'.")

    elif choice == "4":

        print("Thank you for using the Student Records System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 4.")