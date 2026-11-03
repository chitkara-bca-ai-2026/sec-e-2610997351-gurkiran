#Lab 16 - Utility Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    return base ** exp


def format_number(n):
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n


history = []

while True:
    print("\n======================================")
    print("   ENTERPRISE MODULAR UTILITY CALCULATOR")
    print("======================================")

    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == "8":
        print("Calculator closed. Goodbye!")
        break

    elif choice == "7":
        print("\n--- CALCULATION HISTORY ---")

        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            for item in history:
                print(item)

    elif choice in ("1", "2", "3", "4", "5", "6"):

        try:
            a = float(input("Enter first number: "))

            if choice == "6":
                exp = input("Enter exponent (press Enter for default 2): ")

                if exp == "":
                    result = power(a)
                    expression = f"{format_number(a)} ** 2"
                else:
                    exp = float(exp)
                    result = power(a, exp)
                    expression = f"{format_number(a)} ** {format_number(exp)}"

            else:
                b = float(input("Enter second number: "))

                if choice == "1":
                    result = add(a, b)
                    expression = f"{format_number(a)} + {format_number(b)}"

                elif choice == "2":
                    result = subtract(a, b)
                    expression = f"{format_number(a)} - {format_number(b)}"

                elif choice == "3":
                    result = multiply(a, b)
                    expression = f"{format_number(a)} * {format_number(b)}"

                elif choice == "4":
                    result = divide(a, b)
                    expression = f"{format_number(a)} / {format_number(b)}"

                elif choice == "5":
                    result = modulus(a, b)
                    expression = f"{format_number(a)} % {format_number(b)}"

            if result is None:
                print("Error: Division or modulus by zero is not allowed.")

            else:
                result = format_number(result)

                record = f"{expression} = {result}"

                print("[RESULT]", record)

                history.append(record)

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        except OverflowError:
            print("Error: Result is too large.")

    else:
        print("Invalid choice! Please enter a number from 1 to 8.")