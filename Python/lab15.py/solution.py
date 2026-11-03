#Student information Management System
import os

students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

def write_log(message):
    folder = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(folder, "log.txt")

    with open(log_path, "a", encoding="utf-8") as file:
        file.write(message + "\n")


def show_menu():
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")


def view_students():
    print("\n--- Enrolled Student Records ---")

    if not students:
        print("No student records found.")
    else:
        for roll, details in students.items():
            print(
                f"Roll No: {roll} | Name: {details['Name']} | "
                f"Branch: {details['Branch']} | "
                f"Sem: {details['Semester']} | Marks: {details['Marks']}"
            )

    print("Total Enrolled Students:", len(students))
    write_log("Viewed all student records")


def search_student():
    roll = input("Enter Roll Number to search: ").strip()
    student = students.get(roll)

    if student is None:
        print("[ERROR] Student record not found.")
        write_log(f"Search failed for Roll No: {roll}")
    else:
        print(f"\n[FOUND] Record for Roll No {roll}:")
        print("Name     :", student["Name"])
        print("Branch   :", student["Branch"])
        print("Semester :", student["Semester"])
        print("Marks    :", student["Marks"])
        write_log(f"Searched student Roll No: {roll}")


def register_student():
    print("\n--- Register New Student ---")

    roll = input("Enter Roll Number: ").strip()

    if not roll:
        print("[ERROR] Roll Number cannot be empty.")
        write_log("Student registration failed: Empty roll number")
        return

    if roll in students:
        print("[ERROR] This Roll Number already exists.")
        write_log(f"Registration failed: Roll No {roll} already exists")
        return

    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch (e.g. BCA AI): ").strip()
    semester = input("Enter Semester: ").strip()

    if not name or not branch or not semester:
        print("[ERROR] All fields are required.")
        write_log(f"Registration failed for Roll No: {roll}")
        return

    try:
        semester_number = int(semester)
        if semester_number < 1:
            print("[ERROR] Semester must be at least 1.")
            return

        marks = []
        for i in range(3):
            mark = int(input(f"Enter marks for Subject {i + 1}: "))
            if mark < 0 or mark > 100:
                print("[ERROR] Marks must be between 0 and 100.")
                write_log(f"Registration failed: Invalid marks for Roll No {roll}")
                return
            marks.append(mark)

    except ValueError:
        print("[ERROR] Enter valid numbers for semester and marks.")
        write_log(f"Registration failed: Invalid numeric input for Roll No {roll}")
        return

    students[roll] = {
        "Name": name,
        "Branch": branch,
        "Semester": semester,
        "Marks": marks
    }

    print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")
    write_log(f"Registered student: {name}, Roll No: {roll}")


def update_student():
    roll = input("Enter Roll Number to update: ").strip()

    if roll not in students:
        print("[ERROR] Student record not found.")
        write_log(f"Update failed for Roll No: {roll}")
        return

    student = students[roll]

    print(f"Current details for {student['Name']} (Roll {roll}):")
    print("1. Branch:", student["Branch"])
    print("2. Semester:", student["Semester"])

    choice = input("Choose field to update (1 for Branch, 2 for Semester): ").strip()

    if choice == "1":
        new_branch = input("Enter new branch: ").strip()

        if new_branch:
            student["Branch"] = new_branch
            print("[SUCCESS] Branch updated.")
            write_log(f"Updated branch for Roll No: {roll}")
        else:
            print("[ERROR] Branch cannot be empty.")

    elif choice == "2":
        new_semester = input("Enter new semester: ").strip()

        try:
            if int(new_semester) < 1:
                print("[ERROR] Semester must be at least 1.")
                return

            student["Semester"] = new_semester
            print(f"[SUCCESS] Semester updated to '{new_semester}'.")
            write_log(f"Updated semester for Roll No: {roll}")

        except ValueError:
            print("[ERROR] Enter a valid semester number.")

    else:
        print("[ERROR] Invalid choice.")


def academic_performance():
    roll = input("Enter Roll Number for Academic Performance: ").strip()

    student = students.get(roll)

    if student is None:
        print("[ERROR] Student record not found.")
        write_log(f"Academic report failed for Roll No: {roll}")
        return

    marks = student["Marks"]
    total = sum(marks)
    average = total / len(marks)

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n========== ACADEMIC REPORT ==========")
    print(f"Student Name : {student['Name']} (Roll: {roll})")
    print("Subject Marks:", marks)
    print(f"Total Marks  : {total} / {len(marks) * 100}")
    print(f"Average Marks: {average:.2f}%")
    print("Final Result :", result)
    print("=====================================")

    write_log(f"Viewed academic report for Roll No: {roll}")


def delete_student():
    roll = input("Enter Roll Number to delete: ").strip()

    student = students.pop(roll, None)

    if student is None:
        print("[ERROR] Student record not found.")
        write_log(f"Delete failed for Roll No: {roll}")
    else:
        print(
            f"[SUCCESS] Record for '{student['Name']}' "
            f"(Roll No: {roll}) deleted successfully."
        )
        write_log(f"Deleted student: {student['Name']}, Roll No: {roll}")


def main():
    print("=" * 50)
    print("       STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("=" * 50)

    write_log("Student Information System started")

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            view_students()

        elif choice == "2":
            search_student()

        elif choice == "3":
            register_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            academic_performance()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            print("\nThank you for using Student Information System.")
            print("Goodbye!")
            write_log("Student Information System closed")
            break

        else:
            print("[ERROR] Invalid choice. Please enter a number from 1 to 7.")
            write_log(f"Invalid menu choice: {choice}")


if __name__ == "__main__":
    main()
