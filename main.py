from datetime_operations import show_datetime_menu
from mathematical_operations import show_math_menu
from random_operations import show_random_menu
from uuid_operations import generate_uuid
from file_operations.file_utils import show_file_menu
from module_explorer import explore_modules


def show_main_menu():
    print("\n" + "=" * 48)
    print("          WELCOME TO MULTI-UTILITY TOOLKIT")
    print("=" * 48)
    print("1. Date and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("=" * 48)


def main():
    while True:
        show_main_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            show_datetime_menu()
        elif choice == "2":
            show_math_menu()
        elif choice == "3":
            show_random_menu()
        elif choice == "4":
            generate_uuid()
        elif choice == "5":
            show_file_menu()
        elif choice == "6":
            explore_modules()
        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
