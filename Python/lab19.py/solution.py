# Lab 19 - Student Notes Management System
import os

def write_notes(filename, content):

    with open(filename, "w") as file:
        file.write(content)

    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")

def read_notes(filename):

    if os.path.exists(filename):

        with open(filename, "r") as file:
            content = file.read()

        return content

    else:
        return "No notes file exists yet."

while True:

    print("\n================================")
    print("    STUDENT NOTES MANAGEMENT SYSTEM")
    print("================================")

    print("\nSelect an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":

        notes = input("Enter notes to save: ")

        write_notes("notes.txt", notes)

    elif choice == "2":

        content = read_notes("notes.txt")

        print("\n--- Notes Content (notes.txt) ---")
        print(content)

    elif choice == "3":

        print("Thank you for using the Notes Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 3.")