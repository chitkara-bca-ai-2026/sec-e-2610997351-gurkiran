
# Lab 14 - Library Book Collection

import os

def write_log(message):
    folder = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(folder, "log.txt")

    with open(log_path, "a", encoding="utf-8") as file:
        file.write(message + "\n")

    print("Log saved at:", log_path)

books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering"),
]

library_categories = {category for (_, _, _, category) in books}

student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

def write_log(message):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")


def print_menu():
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")


def view_books():
    print("\n--- Current Library Catalog ---")

    for i, (title, author, year, category) in enumerate(books, start=1):
        print(f'{i}. "{title}" by {author} ({year}) | Genre: {category}')

    print(f"Total Books: {len(books)}")
    write_log("Viewed library catalog")


def add_book():
    print("\n--- Add New Book Record ---")

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()
    category = input("Enter category/genre: ").strip()

    if not title or not author or not year or not category:
        print("\n[ERROR] All fields are required.")
        write_log("Failed to add book: Missing information")
        return

    new_book = (title, author, year, category)
    books.append(new_book)
    library_categories.add(category)

    print(f'\n[SUCCESS] "{title}" added successfully.')
    print(f'[INFO] Category "{category}" added to library categories.')

    write_log(f"Book added: {title} by {author} ({year}) - {category}")


def view_categories():
    print("\n--- Unique Library Categories ---")

    for category in sorted(library_categories):
        print("-", category)

    print(f"Total Unique Genres: {len(library_categories)}")
    write_log("Viewed library categories")


def add_to_wishlist():
    print("\n--- Add Category to Student Wishlist ---")

    category = input("Enter requested genre: ").strip()

    if not category:
        print("\n[ERROR] Genre cannot be empty.")
        write_log("Failed to add wishlist category: Empty input")

    elif category in student_wishlist:
        print(f'\n[INFO] "{category}" is already in the wishlist.')
        write_log(f"Wishlist category already exists: {category}")

    else:
        student_wishlist.add(category)
        print(f'\n[SUCCESS] "{category}" added to the wishlist.')

        write_log(f"Category added to wishlist: {category}")


def gap_analysis():
    print("\n--- Category Gap Analysis ---")

    available = student_wishlist & library_categories
    missing = student_wishlist - library_categories
    unrequested = library_categories - student_wishlist
    everything = student_wishlist | library_categories

    print("\nRequested AND available:")
    print(", ".join(sorted(available)) if available else "None")

    print("\nRequested but NOT in library:")
    print(", ".join(sorted(missing)) if missing else "None")

    print("\nIn library but NOT requested:")
    print(", ".join(sorted(unrequested)) if unrequested else "None")

    print("\nAll genres overall:")
    print(", ".join(sorted(everything)))

    print(f"Total Unique Genres Overall: {len(everything)}")

    write_log("Category gap analysis performed")


def main():
    print("=" * 45)
    print("      LIBRARY BOOK & CATEGORY MANAGER")
    print("=" * 45)

    write_log("Library program started")

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            view_books()

        elif choice == "2":
            add_book()

        elif choice == "3":
            view_categories()

        elif choice == "4":
            add_to_wishlist()

        elif choice == "5":
            gap_analysis()

        elif choice == "6":
            print("\nThank you for using the Library Manager. Goodbye!")
            write_log("Library program closed")
            break

        else:
            print("\n[ERROR] Invalid choice. Please enter 1 to 6.")
            write_log(f"Invalid menu choice: {choice}")


if __name__ == "__main__":
    main()
