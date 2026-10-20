
from datetime import datetime

inventory = ["Notebook", "Pen", "Eraser", "Ruler"]


def write_log(message):
    with open("log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")


while True:
    print("\n========================================")
    print("       INVENTORY CONTROL SYSTEM")
    print("========================================")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- Current Inventory ---")

        if inventory:
            for i, item in enumerate(inventory, start=1):
                print(f"{i}. {item}")
        else:
            print("Inventory is empty.")

        write_log("Viewed inventory")

    elif choice == "2":
        item = input("Enter item name to add: ").strip()

        if item:
            inventory.append(item)
            print(f'[SUCCESS] "{item}" added to inventory.')
            write_log(f'Added item: "{item}"')
        else:
            print("[ERROR] Item name cannot be empty.")
            write_log("Failed to add item: empty name")

    elif choice == "3":
        item = input("Enter item name to remove: ").strip()

        if item in inventory:
            inventory.remove(item)
            print(f'[SUCCESS] "{item}" removed from inventory.')
            write_log(f'Removed item: "{item}"')
        else:
            print(f'[ERROR] "{item}" not found in inventory.')
            write_log(f'Removal failed: "{item}" not found')

    elif choice == "4":
        inventory.sort(key=str.lower)

        print("\n[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")

        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")

        write_log("Sorted inventory alphabetically")

    elif choice == "5":
        print("Thank you for using the Inventory Control System!")
        write_log("Exited inventory control system")
        break

    else:
        print("[ERROR] Invalid choice! Please enter 1 to 5.")
        write_log(f"Invalid menu choice: {choice}")
write_log("Log file test successful")
print("Log entry written successfully!")