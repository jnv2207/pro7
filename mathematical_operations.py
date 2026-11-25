import math


def show_math_menu():
    while True:
        print("\n--- MATHEMATICAL OPERATIONS ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square root")
        print("7. Factorial")
        print("8. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice in {"1", "2", "3", "4", "5"}:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if choice == "1":
                    result = a + b
                elif choice == "2":
                    result = a - b
                elif choice == "3":
                    result = a * b
                elif choice == "4":
                    if b == 0:
                        print("Error: Division by zero is not allowed.")
                        continue
                    result = a / b
                else:
                    result = a ** b
                print("Result:", result)
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == "6":
            try:
                number = float(input("Enter a number: "))
                if number < 0:
                    print("Error: Square root of a negative number is not supported here.")
                else:
                    print("Square root:", math.sqrt(number))
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "7":
            try:
                number = int(input("Enter a non-negative integer: "))
                if number < 0:
                    print("Please enter a non-negative integer.")
                else:
                    print("Factorial:", math.factorial(number))
            except ValueError:
                print("Please enter a whole number.")
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")
