# Lab 18 - Mathematics Learning Tool

def factorial(n):

    if n <= 1:
        return 1

    else:
        return n * factorial(n - 1)

def fibonacci(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:

    print("\n================================")
    print("       MATHEMATICS LEARNING TOOL")
    print("================================")

    print("\nSelect an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":

        try:
            n = int(input("Enter a non-negative integer: "))

            if n < 0:
                print("Error: Please enter a non-negative integer.")

            else:
                result = factorial(n)

                print(f"[RESULT] Factorial of {n} ({n}!) = {result}")

        except ValueError:
            print("Invalid input! Please enter an integer.")

    elif choice == "2":

        try:
            terms = int(input("Enter number of terms to generate: "))

            if terms < 0:
                print("Error: Number of terms cannot be negative.")

            else:
                series = []

                for i in range(terms):
                    series.append(fibonacci(i))

                print(f"[RESULT] Fibonacci series ({terms} terms): {series}")

        except ValueError:
            print("Invalid input! Please enter an integer.")

    elif choice == "3":

        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 3.")