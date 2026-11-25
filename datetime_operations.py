from datetime import datetime, date, time, timedelta
import time as time_module


def show_datetime_menu():
    while True:
        print("\n--- DATE AND TIME OPERATIONS ---")
        print("1. Display current date and time")
        print("2. Display current date")
        print("3. Display current time")
        print("4. Calculate difference between two dates")
        print("5. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Current date and time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        elif choice == "2":
            print("Current date:", date.today().strftime("%d-%m-%Y"))
        elif choice == "3":
            print("Current time:", time_module.strftime("%H:%M:%S"))
        elif choice == "4":
            try:
                first = datetime.strptime(input("Enter first date (DD-MM-YYYY): ").strip(), "%d-%m-%Y").date()
                second = datetime.strptime(input("Enter second date (DD-MM-YYYY): ").strip(), "%d-%m-%Y").date()
                print("Difference:", abs((second - first).days), "days")
            except ValueError:
                print("Invalid date. Please use DD-MM-YYYY.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
