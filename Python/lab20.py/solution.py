# Lab 20 - Daily Log Book
import os

filename = "daily_log.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("[01] 09:00 AM - System server startup verified.\n")
        file.write("[02] 10:30 AM - Morning attendance synchronized.\n")
        file.write("[03] 02:15 PM - Network security patch applied.\n")


def append_entry(filename, entry):

    with open(filename, "a") as file:
        file.write(entry + "\n")

    print(f"[SUCCESS] New entry logged to '{filename}'.")

def display_log(filename):

    with open(filename, "r") as file:
        entries = file.readlines()

    print("\n========== DAILY LOG BOOK ==========")

    if len(entries) == 0:
        print("No log entries found.")

    else:
        for i, entry in enumerate(entries, start=1):
            print(entry.strip())

    print("\nTotal Logged Entries:", len(entries))
    print("====================================")

while True:

    print("\n================================")
    print("       OFFICE DAILY LOG BOOK")
    print("================================")

    print("\nSelect an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":

        entry = input("Enter log entry: ")

        append_entry(filename, entry)

    elif choice == "2":

        display_log(filename)

    elif choice == "3":

        print("Thank you for using the Daily Log Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 3.")